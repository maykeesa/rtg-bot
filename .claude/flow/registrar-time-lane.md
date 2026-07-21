# Fluxo: /registrar-time-lane

Sorteia dois times de 5 jogadores com lanes fixas atribuídas (top/jungle/mid/adc/sup).

## Entrada

- `jogadores` (opcional): string com exatamente 10 nomes únicos separados por vírgula.
- Omitido → [inscrição via reação](inscricao.md).

## Passos

Idêntico ao [registrar-time](registrar-time.md), trocando:

- `formatting.formatar_time` → `formatting.formatar_time_lane` (ou `formatar_time_lane_lista` no modo reação).
- `random_team.select_players` → `random_team_lane.select_team_lane`, que retorna `(time_azul, time_vermelho)` como dicts `{emoji_da_lane: jogador}`, lanes na ordem top/jungle/mid/adc/sup.
- Formatação de cada jogador: `"{emoji_da_lane} - {nome}"`.
- Embed enviado por `embed.time_lane` (título "Time e Lanes aleatórias").

Depois segue o [fluxo da partida](partida.md).
