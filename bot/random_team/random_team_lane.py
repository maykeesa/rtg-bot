from random import choice

def select_team_lane(players):
  lanes = ('<:toplane:977045895394783232>', '<:jglane:977045966026842134>', '<:midlane:977046034079424549>', '<:adclane:977046079616983080>', '<:suplane:977046147485020170>')
  time_vermelho = {}
  time_azul = {}
  i, j = 0, 0

  while len(time_vermelho) != 5:
    player = choice(players)
    if player not in time_vermelho.values():
      time_vermelho[lanes[i]] = player
      i += 1

  while len(time_azul) != 5:
    player = choice(players)
    if player not in time_azul.values() and player not in time_vermelho.values():
      time_azul[lanes[j]] = player
      j += 1

  return time_vermelho, time_azul
