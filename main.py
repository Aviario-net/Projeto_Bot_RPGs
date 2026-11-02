import discord
import random
import re
import os

from dotenv import load_dotenv

from discord.ext import commands
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
bot = commands.Bot(command_prefix= "-", intents=permissoes)

@bot.event
async def on_ready():
    print(f"Estou on BB!!! Bora botar pra quebrar {bot.user}")

@bot.command()
async def ola(ctx:commands.Context):
    canal = ctx.channel
    await ctx.send(f"Eai, tudo bem?\n{canal.name}")

@bot.command()
async def soma(ctx:commands.Context, num1:int, num2:int):
    sum = num1 + num2
    await ctx.reply(sum)

@bot.event
async def on_message(message):
    # Não responder às mensagens de outros bots
    if message.author.bot:
        return

    expressao = message.content.strip().lower()

    # Reconhecer expressões:
    # 1d20
    # 2d20+5
    # 2#d20
    # 2#d20+5
    resultado = re.fullmatch(
        r"(\d+)([#d])d?(\d+)(?:([+-])(\d+))?",
        expressao
    )

    if not resultado:
        return

    quantidade_texto, operador, lados_texto, sinal, modificador_texto = resultado.groups()

    quantidade = int(quantidade_texto)
    lados = int(lados_texto)

    # Calcular modificador
    modificador = int(modificador_texto) if modificador_texto else 0

    if sinal == "-":
        modificador *= -1

    # Impedir entradas inválidas ou excessivas
    if quantidade < 1 or quantidade > 100:
        await message.channel.send(
            "A quantidade de dados deve estar entre 1 e 100."
        )
        return

    if lados < 2 or lados > 100000:
        await message.channel.send(
            "O dado deve ter entre 2 e 100000 lados."
        )
        return

    # Rolar os dados
    resultados = [
        random.randint(1, lados)
        for _ in range(quantidade)
    ]

    # Modo individual (#)
    if operador == "#":

        resultados_finais = [
            valor + modificador
            for valor in resultados
        ]

        valores = []

        for i in range(quantidade):
            if modificador != 0:
                valores.append(
                    f"{resultados[i]} {'+' if modificador > 0 else '-'} {abs(modificador)} = **{resultados_finais[i]}**"
                )
            else:
                valores.append(
                    f"**{resultados[i]}**"
                )

        resposta = (
            f"🎲 **Rolagem: {quantidade}#d{lados}**\n"
            + "\n".join(
                f"Resultado {i+1}: {valores[i]}"
                for i in range(quantidade)
            )
        )

    # Modo agrupado (d)
    else:

        total_dados = sum(resultados)
        total = total_dados + modificador

        valores = " + ".join(map(str, resultados))

        if modificador != 0:
            operacao = (
                f"{valores} {'+' if modificador > 0 else '-'} {abs(modificador)}"
            )
        else:
            operacao = valores

        resposta = (
            f"🎲 **Rolagem: {valores}**\n"
            f"**Total: {total}**"
        )

    await message.channel.send(resposta)

load_dotenv()

token = os.getenv("DISCORD_TOLKIEN")

bot.run(token)
