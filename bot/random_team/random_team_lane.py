from random import choice

from bot.constants import JOGADORES_POR_TIME

def select_team_lane(players):
  lanes = ('<:toplane:977045895394783232>', '<:jglane:977045966026842134>', '<:midlane:977046034079424549>', '<:adclane:977046079616983080>', '<:suplane:977046147485020170>')
  time_azul = {}
  time_vermelho = {}
  i, j = 0, 0

  while len(time_azul) != JOGADORES_POR_TIME:
    player = choice(players)
    if player not in time_azul.values():
      time_azul[lanes[i]] = player
      i += 1

  while len(time_vermelho) != JOGADORES_POR_TIME:
    player = choice(players)
    if player not in time_vermelho.values() and player not in time_azul.values():
      time_vermelho[lanes[j]] = player
      j += 1

  return time_azul, time_vermelho
