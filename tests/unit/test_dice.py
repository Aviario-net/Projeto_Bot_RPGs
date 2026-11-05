# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Testes do parser/rolador de dados (rules/dice.py)."""

import pytest

from rpgbot.rules.dice import roll


class TestRollBasico:
    """Testes de expressões válidas."""

    def test_1d20_retorna_entre_1_e_20(self):
        for _ in range(20):
            result = roll("1d20")
            assert 1 <= result.total <= 20

    def test_2d6_retorna_entre_2_e_12(self):
        for _ in range(20):
            result = roll("2d6")
            assert 2 <= result.total <= 12

    def test_d20_sem_quantidade_e_equivalente_a_1d20(self):
        for _ in range(20):
            result = roll("d20")
            assert 1 <= result.total <= 20

    def test_modificador_positivo(self):
        for _ in range(20):
            result = roll("1d6+5")
            assert 6 <= result.total <= 11

    def test_modificador_negativo(self):
        for _ in range(20):
            result = roll("1d6-2")
            assert -1 <= result.total <= 4

    def test_quantidade_um_aparece_um_dado(self):
        result = roll("1d20")
        assert len(result.rolls) == 1

    def test_quantidade_tres_aparece_tres_dados(self):
        result = roll("3d6")
        assert len(result.rolls) == 3


class TestRollInvalido:
    """Expressões que devem falhar com ValueError."""

    @pytest.mark.parametrize("expressao", [
        "",
        "abc",
        "2x6",
        "d",
        "1d",
        "1d20+",
        "1d20++5",
    ])
    def test_expressao_invalida_levanta_erro(self, expressao):
        with pytest.raises(ValueError):
            roll(expressao)