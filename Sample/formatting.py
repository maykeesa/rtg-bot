import sample.randomTeam.randomTeam as rt
import sample.randomTeam.randomTeamLane as rtl

def formatarTimeLane(jogadores):
    listaTimeLaneA = []
    listaTimeLaneB = []

    players = jogadores.split(",")

    timeA, timeB = rtl.select_team_lane(players)
    for i in timeA.items():
        listaTimeLaneA.append(f"{i[0]} - {i[1]}")

    for i in timeB.items():
        listaTimeLaneB.append(f"{i[0]} - {i[1]}")

    return listaTimeLaneA, listaTimeLaneB

def formatarTime(jogadores):
    listaTimeA = []
    listaTimeB = []

    players = jogadores.split(",")             

    timeA, timeB = rt.select_players(players)
    for i in timeA:
        listaTimeA.append(f" {i} ")

    for i in timeB:
        listaTimeB.append(f" {i} ")

    return listaTimeA, listaTimeB