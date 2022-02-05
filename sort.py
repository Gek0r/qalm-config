import funclib as fl

def getMaps(mapList):
    mapInfo = {"BUSAN" : "CONTROL", "ILIOS" : "CONTROL", "LIJIANG TOWER" : "CONTROL", 
			"NEPAL" : "CONTROL", "OASIS" : "CONTROL", "DORADO" : "ESCORT", 
			"JUNKERTOWN" : "ESCORT", "RIALTO" : "ESCORT", "ROUTE 66" : "ESCORT", 	
			"WATCHPOINT: GIBRALTAR" : "ESCORT", "BLIZZARD WORLD" : "HYBIRD", "EICHENWALDE" : "HYBIRD", 
			"HOLLYWOOD" : "HYBIRD", "KING'S ROW" : "HYBIRD", "VOLSKAYA INDUSTRIES" : "ASSAULT", 
			"WATCHPOINT GIBRALTAR" : "ESCORT", "KINGS ROW" : "HYBIRD", 
			"NUMBANI" : "HYBIRD", "HANAMURA" : "ASSAULT", "HORIZON LUNAR COLONY" : "ASSAULT", 
			"PARIS" : "ASSAULT", "TEMPLE OF ANUBIS" : "ASSAULT", "VOLSKATA INDUSTRIES" : "ASSAULT"}

    nullThings = ['-', "FORFIET", "FORFEIT", ":", "/"]

    seriesList = {}

    for item in mapList:
      if isinstance(item, str):
                mapString = item.upper()
                for map in mapInfo:
                    if map in mapString:
                        seriesList.update({ map : mapInfo[map]})
    return seriesList

def getMatchInfo(column):
    players = []
    matchInfo = {}
    currCell = 0
    mapNum = 1
    scores = []
    cellStart = 13   
    #for each cell, check for players/names
    #TODO - Make sure maps and players match, maybe an index of what location they are in excel???
    #TODO - Add excel support for other layouts and seasons
    for cell in column:
        if currCell == cellStart:
            #if its a player add their name as is to a list
            if isinstance(cell, str):
                if(len(cell) > 1):
                    tempName = fl.detag(cell)
                    players.append(tempName)
            #if its the score add as is to the list
            if isinstance(cell, int):
                scores.append(cell)
                mapNum = mapNum + 1
            if len(players) == 6:
                temp = {mapNum : players}
                matchInfo.update(temp)
                players = [] 
        else:
            currCell = currCell + 1
    return matchInfo, scores                   
    

def sortMatchInfo(matchid, season, week, maps, gamemodes, players, team, scores, tier):
    x = 0
    sortedData = []
    for map in players:
        for player in players[map]:
            name = player
            mapTemp = maps[x]
            typeTemp = gamemodes[x]
            scoreTemp = scores[x]
            tempDict = {'match_id' : matchid,'season' : season, 'week' : week,'map_name' : mapTemp, 'map type' : typeTemp,'player_name' : name,'team_name' : team, 'team_score' : scoreTemp,'player_tier' : tier}
            sortedData.append(tempDict)
        x = x + 1
    return sortedData