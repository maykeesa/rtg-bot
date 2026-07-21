# Fluxo: /registrar-time

Sorteia dois times de 5 jogadores, sem lanes.

## Entrada

- `jogadores` (opcional): string com exatamente 10 nomes únicos separados por vírgula.
- Omitido → [inscrição via reação](inscricao.md).

## Passos (jogadores informados)

1. `TeamCommands.registrar_time` (`bot/cogs/team_commands.py`) recebe a string.
2. `formatting.formatar_time` → `_parse_players` valida (10 únicos; senão `JogadoresInsuficientesError`/`JogadoresExcedentesError` → `embed.erro` responde e encerra).
3. `random_team.select_players` divide aleatoriamente em `(time_azul, time_vermelho)` — azul sempre primeiro.
4. `formatting.formatar_time_lista` formata cada nome como `" nome "`.
5. `embed.time` envia o embed do sorteio (campos TIME AZUL / TIME VERMELHO, piada de `jokes.py`, thumbnail `blitz_angry.png`) com a `IniciarPartidaView` anexada.
6. Segue o [fluxo da partida](partida.md).

## Passos (via reação)

1. `signup.coletar_jogadores` roda a [inscrição](inscricao.md); devolve a lista de 10 display names.
2. `formatting.formatar_time_lista` (sem parse) → passo 5 acima.
