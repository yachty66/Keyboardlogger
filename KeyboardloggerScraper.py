#imports
import os
from datetime import datetime
import pandas as pd
from IPython.display import display, HTML

listWithDailyKeystrokes = []

todaysDate = datetime.today().strftime('%Y-%m-%d')

#if len(index)==0 set header to Date, sum other wise just read file
df = pd.read_csv("/Users/maxhager/Projects/Keyboardlogger/LogData/KeystrokeRecords.csv")
if(len(df)==0):
    df.columns = ["Date", "sum"]

#if row with current date does not exist (in csv) add row with current date in column "Date" and set every other cell in row to zero
def addDailyRow():
    #index of last row 
    indexCurrentRow = len(df)
    #insert on position of last row todays row
    df.loc[indexCurrentRow, "Date"] = todaysDate
    #added in jeder row
    #soll a
    df.iloc[-1 , 1:] = 0
    print(df)

def saveToCsv():
    df.to_csv("/Users/maxhager/Projects/Keyboardlogger/LogData/KeystrokeRecords.csv", index=False)

def getCharacterFromKeystrokeCollector():
    with open("/Users/maxhager/Projects/Keyboardlogger/LogData/KeystrokeCollector.txt", "r") as f:
        for i in f:
            listWithDailyKeystrokes.append(i.split(" ")[2].strip())

def addKeystrokes():
    for i in listWithDailyKeystrokes:
        if i not in df:
            df[i] = 0
        
def keyStrokeCounter():
    counter = 2
    for cell in df.iloc[-1,2:]:
        colname = df.columns[counter]
        print(colname)
        occurenceColnameInlistWithKeystrokes = listWithDailyKeystrokes.count(colname)
        df.iloc[-1, df.columns.get_loc(colname)] = occurenceColnameInlistWithKeystrokes
        counter += 1
    #set sum
    df.iloc[-1, 1]=df.iloc[-1, 2:].sum()

def KeyboardloggerDataTransfer():
    #transfer data from keystrokeCollector to keystrokecollectorbackup 
    with open('/Users/maxhager/Projects/Keyboardlogger/LogData/KeystrokeCollector.txt','r') as firstfile, open('/Users/maxhager/Projects/Keyboardlogger/LogData/KeystrokeCollectorBackup.txt','a') as secondfile:
        for line in firstfile:   
            secondfile.write(line)

#daily deletion of daily collected keystrokes
def KeyboardloggerDataDeletion():
    open('/Users/maxhager/Projects/Keyboardlogger/LogData/KeystrokeCollector.txt', 'w').close()
    
addDailyRow()    
getCharacterFromKeystrokeCollector()
addKeystrokes()
keyStrokeCounter()
saveToCsv()
KeyboardloggerDataTransfer()
KeyboardloggerDataDeletion()

