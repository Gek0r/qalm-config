import pandas as pd

def cleanrawjson(sheet : pd.DataFrame):

    #this works under an assumption of normality between all sheets using the current settings
    firstRowGone = False
    secondRowGone = False
    
    for row in sheet:

        if secondRowGone == False and firstRowGone == True:
            #print("second row removing " + data)
            sheet.pop(row)   
            secondRowGone = True
        if firstRowGone == False:
            #print("first row removing " + data)
            sheet.pop(row)
            firstRowGone = True
    
    i = 1
    for data in sheet:
        if i % 3 == 0:
            sheet.pop(row)
        i = i + 1
        
    return(sheet)


