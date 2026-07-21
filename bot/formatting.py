import bot.random_team.random_team as rt
import bot.random_team.random_team_lane as rtl

from bot.constants import TOTAL_JOGADORES
from bot.exceptions import JogadoresInsuficientesError, JogadoresExcedentesError

def _parse_players(jogadores):
    players = [p.strip() for p in jogadores.split(",") if p.strip()]
    unicos = set(players)

    if len(unicos) < TOTAL_JOGADORES:
        raise JogadoresInsuficientesError(TOTAL_JOGADORES, len(unicos))

    if len(unicos) > TOTAL_JOGADORES:
        raise JogadoresExcedentesError(TOTAL_JOGADORES, len(unicos))

    return players

def formatar_time_lane(jogadores):
    return formatar_time_lane_lista(_parse_players(jogadores))

def formatar_time_lane_lista(players):
    lista_time_azul = []
    lista_time_vermelho = []

    time_azul, time_vermelho = rtl.select_team_lane(players)
    for i in time_azul.items():
        lista_time_azul.append(f"{i[0]} - {i[1]}")

    for i in time_vermelho.items():
        lista_time_vermelho.append(f"{i[0]} - {i[1]}")

    return lista_time_azul, lista_time_vermelho

def formatar_time(jogadores):
    return formatar_time_lista(_parse_players(jogadores))

def formatar_time_lista(players):
    lista_time_azul = []
    lista_time_vermelho = []

    time_azul, time_vermelho = rt.select_players(players)
    for i in time_azul:
        lista_time_azul.append(f" {i} ")

    for i in time_vermelho:
        lista_time_vermelho.append(f" {i} ")

    return lista_time_azul, lista_time_vermelho
