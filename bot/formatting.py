import bot.random_team.random_team as rt
import bot.random_team.random_team_lane as rtl

def _parse_players(jogadores):
    players = [p.strip() for p in jogadores.split(",") if p.strip()]

    if len(set(players)) < 10:
        raise ValueError("São necessários 10 jogadores únicos, separados por vírgula.")

    return players

def formatar_time_lane(jogadores):
    lista_time_lane_a = []
    lista_time_lane_b = []

    players = _parse_players(jogadores)

    time_a, time_b = rtl.select_team_lane(players)
    for i in time_a.items():
        lista_time_lane_a.append(f"{i[0]} - {i[1]}")

    for i in time_b.items():
        lista_time_lane_b.append(f"{i[0]} - {i[1]}")

    return lista_time_lane_a, lista_time_lane_b

def formatar_time(jogadores):
    lista_time_a = []
    lista_time_b = []

    players = _parse_players(jogadores)

    time_a, time_b = rt.select_players(players)
    for i in time_a:
        lista_time_a.append(f" {i} ")

    for i in time_b:
        lista_time_b.append(f" {i} ")

    return lista_time_a, lista_time_b