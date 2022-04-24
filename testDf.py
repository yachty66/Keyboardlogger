import pandas as pd

#df = pd.read_csv("testDf.csv")

#test = df.iloc[-2, 2:].sum()


# open both files
with open('testDf.csv','r') as firstfile, open('testbackup.txt','a') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # append content to second file
             secondfile.write(line)
