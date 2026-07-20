# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é

Bot de Discord (discord.py) que sorteia dois times de 5 jogadores para partidas customizadas de League of Legends, opcionalmente com lanes atribuídas. Escrito em português (nomes de funções, variáveis e mensagens).

## Setup e execução

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # preencher TOKEN (e GUILD_ID para sync instantâneo em dev)
python main.py
```

Não há testes automatizados nem configuração de lint/formatter no projeto.

## Configuração via `.env`

- `TOKEN`: token do bot no Discord Developer Portal (obrigatório).
- `GUILD_ID`: guild usada para sync instantâneo dos slash commands durante o desenvolvimento (usada apenas se `SYNC_GLOBAL` não for `true`).
- `SYNC_GLOBAL`: `true` sincroniza os comandos globalmente (propagação de até 1h); do contrário sincroniza só no `GUILD_ID`.

## Arquitetura

Fluxo de um comando, de ponta a ponta:

1. **`main.py`** — cria o `RtgBot`, carrega a cog `bot.cogs.team_commands` e sincroniza os slash commands conforme `SYNC_GLOBAL`/`GUILD_ID`.
2. **`bot/cogs/team_commands.py`** — define os `hybrid_command`s (`registrar-time-lane`, `registrar-time`), que recebem a string bruta de jogadores, chamam `bot/formatting.py` e capturam `ValueError` para responder erros de validação ao usuário.
3. **`bot/formatting.py`** — parseia a string de jogadores (`_parse_players`, exige 10 nomes únicos separados por vírgula) e delega o sorteio para `bot/random_team/`, formatando o resultado em listas de strings prontas para o embed.
4. **`bot/random_team/random_team.py`** e **`random_team_lane.py`** — lógica pura de sorteio (sem I/O): dividem os 10 jogadores em dois times de 5, e no caso de `random_team_lane`, também atribuem lanes fixas (top/jungle/mid/adc/sup) por ordem de sorteio.
5. **`bot/embed.py`** — monta o `discord.Embed` de resposta (anexa o ícone local `imgs/lolIcon.png` via `attachment://`, adiciona uma piada de `bot/jokes.py`) e envia via `ctx.send`.

Novos comandos de sorteio devem seguir esse mesmo pipeline: cog → formatting (validação + parsing) → random_team (lógica pura) → embed (apresentação).
