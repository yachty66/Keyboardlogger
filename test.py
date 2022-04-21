'''
1. should create csv file with every possible keyboardletter as an column header
    1. create header sum and date
    1. if row with current date does not exist (in csv) add row with current date and set every cell to 0
    2. go in keystroke script, go through every line starting in first line. 
    take character between '' 
    3. go in csv --> if character does not exist in header add him as header and set in todays row a one
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


todaysDate = datetime.today().strftime('%Y-%m-%d')



def createFileWithHeaderDateAndSum():
    data_file = os.path.join('KeystrokeRecords.csv')
    df = pd.read_csv('KeystrokeRecords.csv')
    df.columns = ["Date", "Sum"]

#with open(data_file, 'w') as f:
#    f.write('Date, Sum\n')  # Column names
    
df.
df = pd.read_csv('KeystrokeRecords.csv')
df.columns = ["Date", "Sum"]
#df.append(todaysDate, ignore_index=True)
df.loc[len(df.index)] = todaysDate
df.to_csv("KeystrokeRecords.csv")
#df.loc[0, "Date"] = todaysDate
display(df)
  


    

'''with open("../LogData/KeystrokeCollector.txt", "r") as f:

    for i in f:
        print(i.split(" ")[2]) 
        #split at space
        #take third elem '''