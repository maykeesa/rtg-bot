from random import choice

def select_team_lane(players):
  lanes = ('<:toplane:977045895394783232>', '<:jglane:977045966026842134>', '<:midlane:977046034079424549>', '<:adclane:977046079616983080>', '<:suplane:977046147485020170>')
  timeA = {}
  timeB = {}
  i, j = 0, 0

  while len(timeA) != 5:
    player = choice(players)
    if player not in timeA.values():
      timeA[lanes[i]] = player
      i += 1

  while len(timeB) != 5:
    player = choice(players)
    if player not in timeB.values() and player not in timeA.values():
      timeB[lanes[j]] = player
      j += 1

  return timeA, timeB
