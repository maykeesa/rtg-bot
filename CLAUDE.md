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
2. **`bot/cogs/team_commands.py`** — define os `hybrid_command`s (`registrar-time-lane`, `registrar-time`), que recebem a string bruta de jogadores, chamam `bot/formatting.py`, capturam `ValidacaoError` (`bot/exceptions/`) para responder erros ao usuário, e anexam uma `views.IniciarPartidaView` ao embed do sorteio.
3. **`bot/formatting.py`** — parseia a string de jogadores (`_parse_players`, exige exatamente 10 nomes únicos separados por vírgula, lançando `JogadoresInsuficientesError`/`JogadoresExcedentesError` conforme o caso) e delega o sorteio para `bot/random_team/`, formatando o resultado em listas de strings prontas para o embed.
4. **`bot/random_team/random_team.py`** e **`random_team_lane.py`** — lógica pura de sorteio (sem I/O): dividem os 10 jogadores em dois times de 5, e no caso de `random_team_lane`, também atribuem lanes fixas (top/jungle/mid/adc/sup) por ordem de sorteio.
5. **`bot/embed.py`** — monta os `discord.Embed`s de resposta (ícones locais em `imgs/`, anexados via `attachment://`) e piadas de `bot/jokes.py`. `time`/`time_lane` enviam a mensagem (`ctx.send`, aceitam `view=` opcional e retornam a `discord.Message`); `partida_em_andamento`/`partida_resultado` só constroem e retornam `(embed, file)` para quem chamar (uma `View`) editar a mensagem.
6. **`bot/views.py`** — fluxo interativo pós-sorteio via `discord.ui.View`: botão "Iniciar Partida" → confirmação Sim/Não (expira em 2min) → partida em andamento com botões de resultado (expira em 2h30). Só o autor do comando pode interagir (`_AutorOnlyView.interaction_check`).

Novos comandos de sorteio devem seguir esse mesmo pipeline: cog → formatting (validação + parsing) → random_team (lógica pura) → embed (apresentação).

## Pegadinhas de discord.py descobertas na prática

Relevantes para qualquer código futuro que edite mensagens com embed + anexo de imagem via botões/Views:

- **`discord.Embed.copy()` é raso**: a lista `fields` é compartilhada entre original e cópia — `copy_da.add_field(...)` também muta o original. Use `copy.deepcopy(embed)` quando precisar mesmo de independência.
- **`attachment://arquivo.png` no thumbnail só existe até o Discord responder**: depois de enviada, `message.embeds[0].thumbnail.url` já vem resolvido pra uma URL de CDN, não mais `attachment://...`. Se você reusar esse embed (ex: copiar pra reverter/editar depois) sem chamar `.set_thumbnail(url="attachment://arquivo.png")` de novo, o arquivo físico anexado fica "órfão" (nada mais referencia ele) e o Discord o exibe solto, fora do embed.
- **Trocar o arquivo anexado via `interaction.response.edit_message(attachments=[...])` não é confiável**: para trocar a imagem de uma mensagem a partir do clique de um botão, prefira `await interaction.response.defer()` seguido de `await interaction.edit_original_response(attachments=[...])` (edição via webhook).
- **`View(timeout=...)` continua rodando mesmo depois de você trocar a `view=` da mensagem por outra**: se o usuário avança de uma tela pra outra antes do timeout da tela anterior disparar, chame `self.stop()` explicitamente nos callbacks de transição — senão o `on_timeout` da view antiga dispara sozinho minutos depois e sobrescreve a tela atual (foi a causa de imagens "vazando" pra fora do embed sem ninguém clicar em nada).
