import pandas as pd
import overwatchvalues as owv


# The interval for away team data is 8, starting at cell spot 15
# The interval for home team data is 7, starting at cell spot 16
# Extra score in spot 65
# Roster is always 3 to at least 8, range should include out to 13 just in case


def cleanmatch(away : pd.DataFrame, home : pd.DataFrame, week):
    match = {}
    builtMaps = []
    counter = 0
    awayTeamName = ""
    homeTeamName = ""
    finalHomeScore = 0
    finalAwayScore = 0
    finalTieScore = 0
    finalWinner = ""
    homeRoster = []
    awayRoster = []
    maps = []
    mapWinners = []
    awayMapScores = []
    homeMapScores = []
    homePlayers = []
    awayPlayers = []

    names = getnames(away)

    awayTeamName = names[0]
    homeTeamName = names[1]

    awayRoster = getRoster(away)
    homeRoster = getRoster(home)

    maps = getMaps(away)

    mapTypes = getMapTypes(maps)

    homePlayers = getPlayers(home)
    awayPlayers = getPlayers(away)

    awayMapScores = getScores(away)
    homeMapScores = getScores(home)

    mapWinners = getMapWinner(awayMapScores, homeMapScores)

    finalHomeScore, finalAwayScore, finalTieScore = getFinalScores(awayMapScores, homeMapScores)

    finalWinner = getFinalWinner(finalHomeScore, finalAwayScore, homeTeamName, awayTeamName)
    

    for game in maps:
        builtMaps.append({"name": maps[counter], "type": mapTypes[counter], "home_players": homePlayers[counter], "away_players": awayPlayers[counter],
                         "home_score": homeMapScores[counter], "away_score": awayMapScores[counter], "map_winner": mapWinners[counter]})
        counter = counter + 1

    match = {"week" : week, "home" : homeTeamName, "away" : awayTeamName, "final_home_score" : finalHomeScore, "final_away_score" : finalAwayScore, "final_winner" : finalWinner, "home_roster" : homeRoster, "away_roster" : awayRoster, "maps" : builtMaps}
    return match


def getnames(home):
    for cell in home:
        return cell.split(" VS ")


def getRoster(column):
    roster = []
    rosterKey = 3
    for x in range(rosterKey, 13):
        player = column[x]
        if isinstance(player, str):
            roster.append(player)
    return roster



def getMaps(column):
    maps = []
    mapKey = 15
    counter = 0
    for x in range(mapKey, 55, 10):
        mapName = column[x]
        if isinstance(mapName, str):
            maps.append(mapName)
            counter = counter + 1
    if counter < 4:
        return []
        
    return maps


def getPlayers(column):
    players = []
    mapPlayers = []
    playerKey = 16
    z = 22
    for x in range(playerKey, 56, 10):
        for y in range(x, z):
            player = column[y]
            if isinstance(player, str):
                print(y)
                mapPlayers.append(player)
        players.append(mapPlayers)
        z = x + 5
    return players


def getScores(column):
    scores = []
    scoreKey = 22
    for x in range(scoreKey, 62, 10):
        score = column[x]
        scores.append(score)
    return scores


def getMapWinner(awayArr, homeArr):
    winner = []
    counter = 0
    for score in awayArr:
        if score> homeArr[counter]:
            winner.append("AWAY")
        if score < homeArr[counter]:
            winner.append("HOME")
        if score == homeArr[counter]:
            winner.append("TIE")
        counter = counter + 1
    return winner

def getFinalScores(awayArr, homeArr):
    home = 0
    away = 0
    tie = 0
    counter = 0
    for score in awayArr:
        if score > homeArr[counter]:
            away = away + 1
        if score < homeArr[counter]:
            home = home + 1
        if score == homeArr[counter]:
            tie = tie + 1
        counter = counter + 1
    return home, away, tie


def getMapTypes(maps):
    print(maps)
    types = []
    for name in maps:
        types.append(owv.MAP_INFO[name].upper())
    return types

def getFinalWinner(home, away, homeName, awayName):
    if home > away:
        return homeName
    if home < away:
        return awayName