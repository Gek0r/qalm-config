
import pandas as pd
import csv
from tkinter import filedialog
import sort as gd
import funclib as fl

file_path = filedialog.askopenfilename()
file_parts = file_path.split('/')
fileToParse = file_parts[len(file_parts) - 1]
print('Enter the season being processed')
season = input()
print('Enter the tier for the season being processed, NaN for none(Season 1-2)')
tier = input()
matchID = 10000 * season
csv_columns = ['match_id', 'season', 'week', 'map_name', 'map type', 'player_name', 'team_name', 'team_score',
               'player_tier']
# defines the Excel sheet
xl = pd.ExcelFile(fileToParse)
# reads the sheet names
readinFile = xl.sheet_names
pd.set_option("display.max_rows", None, "display.max_columns", None)
# for each sheet in the Excel
# generate a match id for the rest of the loop for the teams
# grab the first person of the first team
# check down the line if they appear
# once name appears, check the line it is on, then match to related map and mode
# input team and append to temporary data frame
# once one match is done, append to the final dataframe and export


sortedData = []
completeSet = []
if season == 2:
    for sheet in readinFile:
        mapNames = []
        mapTypes = []
        awayName = []
        homeName = []
        validMatch = False
        gatheredMaps = False
        gotAway = False
        columnNum = 0
        awayTeam = 3
        gotHome = False
        inputFrame = pd.read_excel(xl, sheet)
        for column in inputFrame:
            columnNum = columnNum + 1
            if not gatheredMaps:
                mapList = gd.getmaps(inputFrame[column])
                mapNames = list(mapList.keys())
                mapTypes = list(mapList.values())
                gatheredMaps = True
            if columnNum % 3 == 0:
                teams = fl.splitstring(column, ' @ ')
                homeName = teams[0]
                awayName = teams[1]
            # home loop
            # gather players for the map, the team score
            if gotHome:
                playerInfo, mapScores = gd.getmatchinfo(inputFrame[column])
                sortedData = gd.sortmatchinfo(matchID, season, sheet, mapNames, mapTypes, playerInfo, awayName, mapScores,
                                            tier)
                completeSet.append(sortedData)
                matchID = matchID + 1
                gotHome = False
            if columnNum % 3 == 0:
                playerInfo, mapScores = gd.getmatchinfo(inputFrame[column])
                sortedData = gd.sortmatchinfo(matchID, season, sheet, mapNames, mapTypes, playerInfo, homeName, mapScores,
                                            tier)
                completeSet.append(sortedData)
                gotHome = True

    csv_file = "playerinfo.csv"

    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in completeSet:
                for info in data:
                    writer.writerow(info)
    except IOError:
        print("I/O error")
