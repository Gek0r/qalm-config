import pandas as pd
from tkinter import filedialog
import jsonclean as jsc
file_path = filedialog.askopenfilename()
file_parts = file_path.split('/')
fileToParse = file_parts[len(file_parts) - 1]

pd.set_option("display.max_rows", None, "display.max_columns", None)

# defines the Excel sheet
xl = pd.ExcelFile(fileToParse)
# reads the sheet names
readinFile = xl.sheet_names

#loop to create a json for each sheet
for name in readinFile:
    sheet = pd.read_excel(fileToParse, sheet_name = name)
    prunedJson = jsc.cleanrawjson(sheet)
    release = prunedJson.to_json(indent=4)
    
    with open(name + ".json", 'w') as outfile:
        outfile.write(release)
