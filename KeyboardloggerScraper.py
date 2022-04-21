'''
1. should create csv file with every possible keyboardletter as an column header
    1. create header sum and date
    1. if row with current date does not exist (in csv) add row with current date and set every cell to 0
    2. go in keystroke script, go through every line starting in first line. 
    take character between '' 
    getCharacterFromKeystrokeCollector()
    4. if exist in header go to row of current day and increase amount um 1


2. executes script every day 12:00 night synced with time zone
    1. in header "daily sum" add sum of all numbers from todays row 
    #should count occurence of every keyboard letter and than add occurrence to respective keyboard letter
    2. take all the content from collector script and copy the content to txt file "KeystrokeArchive"
    3 remove all the 
    2. reset keystroke collector script (delete all its content)
    I could reset the script also every day (store data in another script)
'''
#imports
import os
from datetime import datetime
import pandas as pd
from IPython.display import display, HTML

listWithDailyKeystrokes = []

todaysDate = datetime.today().strftime('%Y-%m-%d')

#create file
#dataFile = os.path.join('KeystrokeRecords.csv')

#read file as df and add header
df = pd.read_csv("KeystrokeRecords.csv", sep='\t', names=["Date", "Sum"])
print(df)

#if row with current date does not exist (in csv) add row with current date in column "Date" and set every other cell in row to zero
def addDailyRow():
    indexCurrentRow = len(df)
    df.loc[indexCurrentRow, "Date"] = todaysDate
    df.loc[indexCurrentRow, 1:] = 0 
    print(df)

def saveToCsv():
    df.to_csv("KeystrokeRecords.csv")

def getCharacterFromKeystrokeCollector():
    with open("../LogData/KeystrokeCollector.txt", "r") as f:
        for i in f:
            listWithDailyKeystrokes.append(i.split(" ")[2].strip())
            #split at space
            #take third elem

def addKeystrokes():
    #4. if exist in header go to row of current day and increase amount um 1
    for i in listWithDailyKeystrokes:
        if i not in df:
            df[i] = 0



        #if i is not in header add to header and increase in last row at this header column ONE. set all other rows to zero
        #else increase counter in column with same headername by ONE
        
        


#addHeader()
addDailyRow()
saveToCsv()
getCharacterFromKeystrokeCollector()
addKeystrokes()
print(df)
#print(listWithDailyKeystrokes)