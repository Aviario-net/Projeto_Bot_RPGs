# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Parser e rolador de dados de RPG.

Sintaxe suportada:
    NdM         N dados de M lados       (ex: 2d6)
    dM          equivale a 1dM            (ex: d20)
    NdM+B       com modificador positivo  (ex: 2d6+3)
    NdM-B       com modificador negativo  (ex: 1d20-2)

O módulo é Python puro: NÃO importa discord nem toca em banco.
depois tu dá uma inclementada com o que tu fizestes
"""
import random  # r
import re  # r-e
from dataclasses import dataclass  # d

_DICE_PATTERN = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$")


@dataclass(frozen=True)
class RollResult:
    """Resultado de uma rolagem."""

    expression: str
    rolls: list[int]
    modifier: int

    @property
    def total(self) -> int:
        """Soma dos dados individuais + modificador."""
        return sum(self.rolls) + self.modifier


def parse(expression: str) -> tuple[int, int, int]:
    """Parsea 'NdM+mod' em (quantidade, faces, modificador).

    Raises:
        ValueError: se a expressão for inválida.
    """
    expression = expression.strip().lower()
    match = _DICE_PATTERN.fullmatch(expression)
    if not match:
        raise ValueError(f"Expressão inválida: {expression!r}")

    quantity_str, faces_str, modifier_str = match.groups()

    quantity = int(quantity_str) if quantity_str else 1
    if quantity < 1:
        raise ValueError(f"Quantidade de dados inválida: {quantity}")

    faces = int(faces_str)
    if faces < 1:
        raise ValueError(f"Faces de dado inválidas: {faces}")

    modifier = int(modifier_str) if modifier_str else 0

    return quantity, faces, modifier


def roll(expression: str) -> RollResult:
    """Rola dados segundo a expressão.

    Examples:
        >>> r = roll("2d6+3")
        >>> 5 <= r.total <= 15
        True

    Raises:
        ValueError: se a expressão for inválida.
    """
    quantity, faces, modifier = parse(expression)

    rolls = [random.randint(1, faces) for _ in range(quantity)]

    return RollResult(
        expression=expression,
        rolls=rolls,
        modifier=modifier,
    )


def format_result(result: RollResult) -> str:
    """Formata o resultado para exibição.

    Exemplo:
        '2d6+3 → [4, 6] + 3 = 13'
    """
    rolls_str = ", ".join(str(r) for r in result.rolls)
    if result.modifier > 0:
        return f"{result.expression} → [{rolls_str}] + {result.modifier} = {result.total}"
    if result.modifier < 0:
        return f"{result.expression} → [{rolls_str}] - {abs(result.modifier)} = {result.total}"
    return f"{result.expression} → [{rolls_str}] = {result.total}"