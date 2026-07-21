# Fluxo: inscrição via reação

Acionado quando `/registrar-time` ou `/registrar-time-lane` é usado **sem** o parâmetro `jogadores`. Implementado em `bot/signup.py` (`coletar_jogadores`).

## Passos

1. Envia o embed "Inscrições abertas" (`embed.inscricao`) com prazo de 2min (`INSCRICAO_TIMEOUT`), mostrado como `<t:...:R>` (contagem ao vivo no cliente), e o bot adiciona a própria reação ✅ como afordância.
2. Loop de `bot.wait_for("raw_reaction_add")` filtrando: mesma mensagem, emoji ✅, não-bot, sem repetição por `user_id`.
3. A cada jogador aceito, o embed é editado com a lista atualizada (`JOGADORES (X/10)`), usando `member.display_name`.
4. Ao juntar `TOTAL_JOGADORES` (10): nomes duplicados ganham sufixo `(2)`, `(3)`... (`_nomes_unicos`) — nomes idênticos quebrariam o sorteio — e a lista é retornada para a cog.
5. Se o prazo vence antes: lança `InscricaoExpiradaError` carregando a mensagem de inscrição (`mensagem_origem`); `embed.erro` **edita** essa mensagem para o embed de erro (em vez de enviar mensagem nova).

## Observações

- O dict interno `inscritos` mapeia `user_id → display_name`; os IDs estão disponíveis ali para features futuras (ex: estatísticas por jogador).
- O emoji precisa ser o caractere unicode `"✅"` — shortcode `:white_check_mark:` não funciona em `add_reaction` nem na comparação com `payload.emoji`.
