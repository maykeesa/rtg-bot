from random import choice

from bot.constants import JOGADORES_POR_TIME

def select_players(players):
  time_azul = []
  time_vermelho = []

  while len(time_azul) != JOGADORES_POR_TIME:
    player = choice(players)
    if player not in time_azul:
      time_azul.append(player)

  while len(time_vermelho) != JOGADORES_POR_TIME:
    player = choice(players)
    if player not in time_vermelho and player not in time_azul:
      time_vermelho.append(player)

  return time_azul, time_vermelho
