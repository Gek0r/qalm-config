import pandas as pd
from tkinter import filedialog
import jsonclean as jsc
import cleanmatch as cm
import json

file_path = filedialog.askopenfilename()
file_parts = file_path.split('/')
fileToParse = file_parts[len(file_parts) - 1]

pd.set_option("display.max_rows", None, "display.max_columns", None)

# defines the Excel sheet
xl = pd.ExcelFile(fileToParse)
# reads the sheet names
readinFile = xl.sheet_names

outputfile = {}

outputfile.update({"season" : 8, "tier" : "discord"})
matches = []

homecolumn = {}
awaycolumn = {}
gotAway = False
justUsed = False
newMatch = False
#loop to create a json for each sheet
for name in readinFile:

    sheetname = name.split(" - ")
    week = sheetname[1]

    sheet = pd.read_excel(fileToParse, sheet_name = name)

    prunedJson = jsc.cleanrawjson(sheet)
    for column in prunedJson:
        if gotAway == True:
            homecolumn = prunedJson[column]
            matches.append(cm.cleanmatch(awaycolumn, homecolumn, week))
            gotAway = False
            justUsed = True
            newMatch = False

        if gotAway == False and justUsed == False:
            awaycolumn = prunedJson[column]
            gotAway = True
            newMatch = True

        if justUsed == True and newMatch == False:
            justUsed = False
            newMatch = False

outputfile.update({"matches" : matches})
with open("FINAL.json", 'w') as outfile:
    json.dump(outputfile, outfile)
