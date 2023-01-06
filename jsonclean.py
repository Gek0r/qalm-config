import pandas as pd

def cleanrawjson(sheet : pd.DataFrame):

    #this works under an assumption of normality
    firstRowGone = False
    secondRowGone = False
    
    for data in sheet:

        if secondRowGone == False and firstRowGone == True:
            print("second row removing " + data)
            sheet.pop(data)   
            secondRowGone = True
        if firstRowGone == False:
            print("first row removing " + data)
            sheet.pop(data)
            firstRowGone = True
    
    i = 1
    for data in sheet:
        if i % 3 == 0:
            sheet.pop(data)
        i = i + 1
        
    return(sheet)


