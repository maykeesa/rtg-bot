# Fluxo: partida (pós-sorteio)

Fluxo interativo comum aos dois comandos, implementado em `bot/views.py`. Todas as telas são a **mesma mensagem** do sorteio, editada a cada transição. Em todas as views, só o autor do comando pode clicar (`_AutorOnlyView.interaction_check`); os demais recebem aviso efêmero.

## Telas

```
[Sorteio] --Iniciar Partida--> [Confirmação Sim/Não] --Sim--> [Em andamento] --botão--> [Resultado]
    ^                              |       |
    |------------Não/timeout 2min--+       +--(nenhum clique em 2h30)--> [Expirada]
```

1. **Sorteio** (`IniciarPartidaView`, sem timeout): botão "▶️ Iniciar Partida". Ao clicar, o embed original é deep-copiado, a thumbnail é re-normalizada para `attachment://` (ver pegadinhas no CLAUDE.md) e ganha o campo "Confirmação" com prazo `<t:...:R>`.
2. **Confirmação** (`ConfirmarPartidaView`, timeout 2min):
   - "✅ Sim" → `stop()`, monta `embed.partida_em_andamento` (campo "Início" com `<t:...:R>`, thumbnail `blitz_happy.png`) via `defer()` + `edit_original_response(attachments=...)`.
   - "✖️ Não" ou timeout → `stop()`/`on_timeout`, restaura o embed original e a `IniciarPartidaView`.
3. **Em andamento** (`PartidaEmAndamentoView`, timeout 2h30 = `PARTIDA_TIMEOUT`): botões "Time Azul venceu" (primary), "Time Vermelho venceu" (danger), "Cancelar partida" (secondary).
4. **Resultado** (`embed.partida_resultado`, sem view):
   - Vitória: mostra só o campo do time vencedor; cor/imagem do resultado (`blitz_love.png`).
   - "cancelada"/"expirada": mostra os dois times, cor neutra, `blitz_broken.png`.

## Estado

Sem persistência: tudo vive nos atributos das views (autor_id, listas dos times, `message`), passado de view em view a cada transição. Reiniciar o bot perde partidas em aberto.
