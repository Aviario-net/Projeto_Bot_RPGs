# 🐺 Wolframium

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/discord.py-5865F2?style=for-the-badge&amp;logo=discord&amp;logoColor=white" alt="discord.py" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&amp;logo=pydantic&amp;logoColor=white" alt="Pydantic" />
  <img src="https://img.shields.io/badge/License-AGPL%20v3-blue?style=for-the-badge" alt="License AGPL v3" />
  <img src="https://img.shields.io/badge/Status-MVP%20em%20andamento-yellow?style=for-the-badge" alt="Status: MVP em andamento" />
  <p><strong>Uma caixa de ferramentas completa para RPG de mesa no Discord.</strong><br />
  Fichas dinâmicas · Rolagens inteligentes · Combate automatizado · Geração de conteúdo · Imersão sonora · Play-Solo</p>
</div>

---

## 👥 Desenvolvido por
<div align="center">
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/MarcosMakosu">
        <img src="https://github.com/MarcosMakosu.png" width="100px;" alt="MarcosMakosu"/><br />
        <sub><b>MarcosMakosu</b></sub>
      </a><br />
      <a href="https://github.com/MarcosMakosu">
        <img src="https://img.shields.io/badge/GitHub-MarcosMakosu-181717?style=flat-square&logo=github" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/junny11">
        <img src="https://github.com/junny11.png" width="100px;" alt="junny11"/><br />
        <sub><b>junny11</b></sub>
      </a><br />
      <a href="https://github.com/junny11">
        <img src="https://img.shields.io/badge/GitHub-junny11-181717?style=flat-square&logo=github" />
      </a>
    </td>
  </tr>
</table>
</div>

---

## 📖 Sobre o Projeto
**Wolframium** é um bot de Discord pensado para ser o *canivete suíço* de mestres e jogadores de RPG de mesa. Ele centraliza fichas, rolagens, combate, inventário, geração aleatória e imersão em um único lugar — eliminando planilhas externas e reduzindo erros durante a sessão.
Construído em **Python** com arquitetura modular (cogs + features + rules puros), priorizando **evolução incremental**: um MVP sólido primeiro, recursos avançados depois. Tudo é desenhado para escalar de "uma mesa de amigos" para "várias campanhas simultâneas" sem refatoração.

---

## 🚦 Status atual
O projeto está em **desenvolvimento ativo**, na fase de MVP. O que já funciona hoje:

| Módulo | Status |
|----|----|
| 🎲 Rolagem de dados (`/roll`, `/sorte`) | ✅ Funcionando |
| 📜 Ficha de personagem (JSON + embed) | ✅ Funcionando (campos básicos) |
| ✏️ Edição de ficha via modal | ✅ Funcionando |
| ❤️ Ajuste de HP (`/hp`) | ✅ Funcionando |
| 🧪 Testes automatizados | ✅ 14 testes no motor de dados |
| 🗄️ Persistência em SQLite | 🚧 Planejado (hoje: JSON) |
| 📄 Exportação em PDF | 🚧 Planejado (WeasyPrint) |
| ⚔️ Combate com iniciativa | 📅 Roadmap |
| 🧙 Ferramentas do mestre | 📅 Roadmap |
| 🎨 Áudio e imersão | 📅 Roadmap |

> ⚠️ **Transparência**: as funcionalidades descritas nas seções abaixo são a **visão completa** do projeto. As marcadas como 🚧 ou 📅 **ainda não estão implementadas** — estão listadas para orientar o desenvolvimento e permitir contribuições.
---
## 🎯 Objetivos Principais
| # | Objetivo | Descrição |
|---|----------|-----------|
| 1 | 📝 **Fichas Automatizadas** | Criação, edição, arquivamento e exportação (PDF/JSON) por campanha |
| 2 | 🎲 **Rolagens Inteligentes** | Dados complexos que aplicam bônus da ficha automaticamente |
| 3 | 🕓 **Histórico de Alterações** | Rastreabilidade total: quem mudou o quê e quando |

---
## ✨ Funcionalidades (visão completa)
### 📝 Fichas e Personagens
- ✅ Ficha básica de D&D 5e (nome, raça, classe, nível, atributos, HP)
- ✅ Persistência em JSON (exportável e legível)
- ✅ Edição via modal do Discord
- 🚧 Templates por sistema: **D&D 5e, Tormenta20, Ordem Paranormal, Cyberpunk RED**
- 🚧 Exportação em PDF com layout profissional
- 🚧 Embed resumido com botões: *Rolar Ataque · Tomar Dano · Descansar · Usar Item*
- 📅 Histórico de alterações com autoria e data
- 📅 Múltiplos personagens por usuário · 1 ficha ativa por campanha
### 🎲 Dados e Rolagens
- ✅ Rolagens simples: `1d20`, `2d6+3`, `d20`, `1d6-2`
- ✅ Calculadora de probabilidade (`/sorte`)
- 🚧 Vantagem, desvantagem, keep-highest (`2d20kh1`), drop-lowest (`4d6dl1`)
- 🚧 Dados explosivos, sucessos e falhas críticas
- 🚧 Macros de ataque (ataque + dano + crítico em um clique)
- 🚧 Rolagens secretas para o mestre (GM Rolls)
- 📅 Suporte a dados especiais: Fome (Vampiro), Sanidade (OP), Caos (Tormenta)
### ⚔️ Combate e Iniciativa
- 📅 Iniciativa automática com ordenação e turno atual
- 📅 Painel com PV, condições, buffs/debuffs e duração
- 📅 Botões: *Próximo Turno · Dano · Cura · Adicionar/Remover Condição*
- 📅 HP temporário, morte, ferimentos, exaustão
- 📅 Modo "esconder PV dos inimigos" · Log de combate exportável
### 🧙 Ferramentas do Mestre
- 📅 Criação/importação de NPCs e monstros com statblock
- 📅 Geradores: encontros por nível, loot, tesouro, nomes, tavernas, rumores, quests, masmorras, clima
- 📅 Notas de campanha (`/lore [nome]`)
- 📅 Facções, reputação, favores e relacionamentos
- 📅 Linha do tempo, pistas reveladas e NPCs conhecidos
- 📅 Agendamento de sessões, presença, lembretes e recaps automáticos
### 🎒 Ferramentas do Jogador
- 📅 Inventário com peso, moedas, itens mágicos e charges
- 📅 Controle de spell slots, ki, fúria, superioridade, munição
- 📅 Descanso curto/longo com recuperação automática
- 📅 Diário do personagem · Assistente de level up
- 📅 Sistema de downtime
### 🏰 Campanha e Sessão
- 📅 Canais por campanha: **IC · OOC · Fichas · Combate · Handouts**
- 📅 Quadro de missões com status e recompensas
- 📅 Calendário, logs e resumo automático da sessão
- 📅 Multi-campanha por servidor
- 📅 Backup e restauração
### 🎨 Imersão
- 📅 Playlists e trilhas sonoras por cena (seletor por lugar × tensão)
- 📅 Efeitos sonoros: espada, magia, monstro, taverna
- 📅 Comandos narrativos: `/descrever`, `/clima`, `/som`
### 🎭 Play-Solo
- 📅 **Mythic GME** · **CRGE** · **One Page Solo Engine**
### 🔌 Integrações
- 📅 APIs: **Open5e · D&D 5e API · Pathfinder**
- 📅 VTTs: **Roll20 · Foundry · Owlbear Rodeo**

## 🛠️ Stack Técnica

🐍 Python 3.11+ → Linguagem principal  
🤖 discord.py 2.7+ → Interface Discord (cogs + slash + modals)  
📦 Pydantic 2.14+ → Modelos e validação de fichas  
⚙️ pydantic-settings → Configuração via .env  
🧪 pytest → Testes automatizados  
🔍 ruff → Linting e formatação  
📄 WeasyPrint + Jinja2 → Exportação em PDF (planejado)  
🗄️ SQLAlchemy + aiosqlite → Banco relacional (planejado, hoje: JSON)  
🎵 FFmpeg + yt-dlp → Áudio (planejado)

---
## 🚀 Roadmap
- [x] 🎯 Definição de escopo e arquitetura
- [x] 🧱 Estrutura base (`src/` layout, config tipada, venv isolado)
- [x] 🎲 Motor de dados com testes (`rules/dice.py`)
- [x] 🤖 Bot online com sync de slash commands
- [x] 📝 Ficha básica de D&D 5e (JSON + embed + modal)
- [ ] 📊 **MVP completo**: ficha expandida + PDF + SQLite
- [ ] ⚔️ Sistema de combate e iniciativa
- [ ] 🧙 Ferramentas do mestre (geradores + lore)
- [ ] 🎒 Inventário, economia e downtime
- [ ] 🎨 Módulo de áudio e imersão
- [ ] 🎭 Suporte a Play-Solo
- [ ] 🔌 Integrações externas (APIs, VTTs)
---
## 🚀 Instalação (para desenvolvimento)
### Pré-requisitos
- **Python 3.11+**
- **Git**
- Bibliotecas nativas (Linux/Arch): `pango cairo harfbuzz gdk-pixbuf2 libffi openssl`
### Passo a passo

```bash
# 1. Clonar
git clone https://github.com/Aviario-net/Projeto_Bot_RPGs.git
cd Wolframium
# 2. Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate.fish    # fish
# ou: source .venv/bin/activate    # bash/zsh
# 3. Instalar dependências (dev)
pip install -e ".[dev]"
# 4. Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com:
#   DISCORD_TOKEN=...
#   DISCORD_OWNER_ID=...
#   DEV_GUILD_ID=...
# 5. Rodar o bot
python -m rpgbot.main 
```

### Testes

```bash
pytest -v
ruff check src/rpgbot
```

---

## 🗂️ Estrutura do Projeto

```text

src/rpgbot/
├── rules/              # Lógica pura (dados, fórmulas) — sem Discord, sem banco
├── features/           # Domínio (character, campaign, combat...)
├── interface/          # Tudo que importa discord (cogs, views, modals)
├── infrastructure/     # Mundo externo (DB, PDF, APIs)
├── config.py           # Único ponto que lê .env
├── bot.py              # Classe RPGbot
└── main.py             # Entry point
tests/                  # Testes automatizados
templates/              # Templates Jinja2 (PDF, futuro)
data/                   # Banco local, PDFs gerados (gitignored)
plugins/                # Pacotes de dados para comunidade (futuro)
```

**Regra de arquitetura**: `rules/` nunca importa `discord`. `features/` nunca importa `interface/`. Isso permite testar tudo sem subir Discord.

---

## 📚 Referências e Inspirações

- [Donjon](https://donjon.bin.sh/) · Tome of Adventure Design
- UNE (The Universal NPC Emulator) · The Mother of All Encounter Tables
- [World Anvil](https://www.worldanvil.com/) · [Kanka.io](https://kanka.io/) · LegendKeeper · Notion

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para abrir _issues_, sugerir sistemas/templates ou enviar _pull requests_.

1. Faça um **fork** do projeto
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit (`git commit -m 'feat: adiciona X'`)
4. Push (`git push origin feature/minha-feature`)
5. Abra um **Pull Request**

**Antes de enviar um PR**:

- Rode `pytest -v` (tudo verde)
- Rode `ruff check src/rpgbot` (sem erros)
- Siga [Conventional Commits](https://www.conventionalcommits.org/pt-br/) (`feat:`, `fix:`, `docs:`, `chore:`)

---

## 📄 Licença

Distribuído sob a **GNU Affero General Public License v3.0 (AGPL-3.0-only)**.  
Veja [`LICENSE`](https://license/) para o texto completo e [`NOTICE`](https://notice/) para informações de copyright.

> **O que isso significa**: você pode usar, modificar e distribuir este software livremente, **desde que** qualquer versão modificada (incluindo serviços de rede) permaneça sob a mesma licença e com código-fonte aberto.

---

<div align="center">

**🐺 Wolframium** — _Role o dado. O resto é com a gente._

Desenvolvido com 💙 por [**MarcosMakosu**](https://github.com/MarcosMakosu) e [**junny11**](https://github.com/junny11)

⭐ Se este projeto te ajuda, considere dar uma estrela!

</div>

---

## 🏆 Contributors

<div align="center">
  <a href="https://github.com/Aviario-net/Projeto_Bot_RPGs/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=Aviario-net/Projeto_Bot_RPGs" alt="Contributors" />
  </a>
  <br />
  <a href="https://github.com/Aviario-net/Projeto_Bot_RPGs/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Aviario-net/Projeto_Bot_RPGs?style=for-the-badge&amp;color=blue" alt="Contributors" />
  </a>
  <a href="https://github.com/Aviario-net/Projeto_Bot_RPGs/commits/">
    <img src="https://img.shields.io/github/last-commit/Aviario-net/Projeto_Bot_RPGs?style=for-the-badge&amp;color=green" alt="Last commit" />
  </a>
  <a href="https://github.com/Aviario-net/Projeto_Bot_RPGs/issues">
    <img src="https://img.shields.io/github/issues/Aviario-net/Projeto_Bot_RPGs?style=for-the-badge&amp;color=orange" alt="Issues" />
  </a>
  <a href="https://github.com/Aviario-net/Projeto_Bot_RPGs/stargazers">
    <img src="https://img.shields.io/github/stars/Aviario-net/Projeto_Bot_RPGs?style=for-the-badge&amp;color=yellow" alt="Stars" />
  </a>
  <a href="https://github.com/Aviario-net/Projeto_Bot_RPGs/network/members">
    <img src="https://img.shields.io/github/forks/Aviario-net/Projeto_Bot_RPGs?style=for-the-badge&amp;color=purple" alt="Forks" />
  </a>
</div> 
