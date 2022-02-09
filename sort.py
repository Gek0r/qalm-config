import funclib as fl


def getmaps(map_list):
    map_info = {"BUSAN": "CONTROL", "ILIOS": "CONTROL", "LIJIANG TOWER": "CONTROL",
                "NEPAL": "CONTROL", "OASIS": "CONTROL", "DORADO": "ESCORT",
                "JUNKERTOWN": "ESCORT", "RIALTO": "ESCORT", "ROUTE 66": "ESCORT",
                "WATCHPOINT: GIBRALTAR": "ESCORT", "BLIZZARD WORLD": "HYBIRD", "EICHENWALDE": "HYBIRD",
                "HOLLYWOOD": "HYBIRD", "KING'S ROW": "HYBIRD", "VOLSKAYA INDUSTRIES": "ASSAULT",
                "WATCHPOINT GIBRALTAR": "ESCORT", "KINGS ROW": "HYBIRD",
                "NUMBANI": "HYBIRD", "HANAMURA": "ASSAULT", "HORIZON LUNAR COLONY": "ASSAULT",
                "PARIS": "ASSAULT", "TEMPLE OF ANUBIS": "ASSAULT", "VOLSKATA INDUSTRIES": "ASSAULT"}

    series_list = {}

    for cell in map_list:
        if isinstance(cell, str):
            mapString = cell.upper()
            for x in map_info:
                if x in mapString:
                    series_list.update({x: map_info[x]})
    return series_list


def getmatchinfo(column):
    players = []
    match_info = {}
    curr_cell = 0
    map_num = 1
    scores = []
    cell_start = 13
    # for each cell, check for players/names
    # TODO - Make sure maps and players match, maybe an index of what location they are in excel???
    # TODO - Add excel support for other layouts and seasons
    for cell in column:
        if curr_cell == cell_start:
            # if it's a player add their name as is to a list
            if isinstance(cell, str):
                if len(cell) > 1:
                    temp_name = fl.detag(cell)
                    players.append(temp_name)
            # if it's the score add as is to the list
            if isinstance(cell, int):
                scores.append(cell)
                map_num = map_num + 1
            if len(players) == 6:
                temp = {map_num: players}
                match_info.update(temp)
                players = []
        else:
            curr_cell = curr_cell + 1
    return match_info, scores


def sortmatchinfo(matchid, season, week, maps, gamemodes, players, team, scores, tier):
    x = 0
    sorted_data = []
    for series in players:
        for player in players[series]:
            name = player
            map_temp = maps[x]
            type_temp = gamemodes[x]
            score_temp = scores[x]
            temp_dict = {'match_id': matchid, 'season': season, 'week': week, 'map_name': map_temp,
                         'map type': type_temp,
                         'player_name': name, 'team_name': team, 'team_score': score_temp, 'player_tier': tier}
            sorted_data.append(temp_dict)
        x = x + 1
    return sorted_data



#first 13 cells ignored
#then get next 6 cells
#check if they have strings
#after that next cell will be score if players decteced
#if empty, ignore addition and mark the number that was not grabbed(map 3, map4, ect)
#Iterate until bottom, 5 regular season, semi finals and onward 7
#if the users are not listed for home or away, check to see if any maps were not passed
#If a may throws a non fill, pop/ignore that map and game for BOTH teams(prevent lopsided data)
#finally append data to CSV file
#loop 13
#   then for next 6
#       push cell into arrary
#   if array empty or has missing cells\
#       Mark map as incomplete
#   else
#       get score
#       Append array to final push
#       return data, caught exceptions
#
#for seasons beyond 2, map is below score
#DO NOT grab maps, part of gather data loop
#