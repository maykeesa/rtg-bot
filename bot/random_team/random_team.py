from random import choice

def select_players(players):
  time_a = []
  time_b = []

  while len(time_a) != 5:
    player = choice(players)
    if player not in time_a:
      time_a.append(player)

  while len(time_b) != 5:
    player = choice(players)
    if player not in time_b and player not in time_a:
      time_b.append(player)

  return time_a, time_b