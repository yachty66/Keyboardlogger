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
            #split at space
            #take third elem

def addKeystrokes():
    #iterate over columns from daily row
    #count occurence of current cell object in listWithDailyKeystrokes and add this value to the current cell object
    #4. if exist in header go to row of current day and increase amount um 1
    for i in listWithDailyKeystrokes:
        if i not in df:
            df[i] = 0
        #if i is not in header add to header and increase in last row at this header column ONE. set all other rows to zero
        #else increase counter in column with same headername by ONE
        
def keyStrokeCounter():
    #iterate over columns from daily row
    #count occurence of current cell object in listWithDailyKeystrokes and add this value to the current cell object
    '''
    now I need to make a plan for the next steps


    before clearing everything 12:00 every day call the keyboardlogger script to add a new line

    clear KeystrokeCollector.txt function. every day 12:00 night synced with time zone

    can just add this script to crontab. need to fix problem that to every row which is not last row all values are set to 0.

    STEPS

        check if script works. i.e. 


        https://crontab.guru/#*_*_1_*_* for this script
        auslagern von dateien mit sensiblen daten von github
        transfer data from KeystrokeCollector.txt to KeystrokeCollectorBackup.txt
        delete data from KeystrokeCollector.txt
        
        execution diagram:
            1. add row in KeystrokeRecords with daily date as an entry and rest zeros
            2. get all daily characters 
            3. if daily chracter does not appear in df add him in header and set whole column to 0
            4. count occurence of each character from daily keystrokes and add this number to adequate column
            5. transfer data from daily keystrokecollector to backup file 
            6. delete daily keystroke collector 

            Note:
                it is important that this gets executed exactly in that order. the script gets executed every 24 hours. 
                everything is fully functional. just need to test if daily date entry works. general does the execution with crontab work?

                1. configure crontab for one minute
                    check if entries are made  
                2. set crontab to 24h
                2. technically done. define next steps for finally completing the project.

            Next steps: 
                1. check if it worked
                2. send me every sunday an mail with the diagram 


        send every sunday email with diagram of keystrokes
    '''
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
    #function needs to be last one which gets exectuted to ensure to dont delete before i make the analysis
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

