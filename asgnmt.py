import operator
import sys
import string


def queries():
    INPUT_FILE_PATH = "./India.txt"
    x = input("Enter a number: ")
    n = int(x)
    OUTFILE = r'C:\Users\Ujwal\Desktop\tweepy\TopUsers'
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as my_File:
        inputfile=my_File.readlines()
    #MaximumUsers
    Result = {}
    for data in inputfile:
       
        fileTemp1 = data.split()
        if fileTemp1[0] in Result:
            Result[fileTemp1[0]] +=1
        else:
            Result[fileTemp1[0]] = 1
    Result = sorted(Result.items(), key = operator.itemgetter(1), reverse = True)
 
    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    output_File.write("The top "+ x +" users who have tweeted the most in the timeframe: \n")
    for i in range (0,n):
        output_File.write("User Name " + Result[i][0] + "\n\n")
        
    output_File.close
    
    #MaxFollowers
    
    MaxFollowers = {}
    for data in inputfile:
        fTemp = data.split()
        if fTemp[0] not in Result:
            MaxFollowers[fTemp[0]] = (fTemp[-2])

    MaxFollowers = sorted(MaxFollowers.items(), key = operator.itemgetter(1), reverse = True)
    OUTFILE = r'C:\Users\Ujwal\Desktop\tweepy\maxFollowers'
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
    output_File.write("The top "+ str(x) +" users who have the maximum followers: " + "\n\n\n")

    for i in range (0, n):
        output_File.write(str(i+1) + ". UserName: " + MaxFollowers[i][0] + " - Number of followers are: " + str(MaxFollowers[i][1]) + "\n\n\n")
    output_File.close

    #MaxRetweets

    MaxRetweets = {}
    for data in inputfile:
  
        fTmp = data.split()
        y = len(fTmp)-2
        tweet = "\""
        for x in range (4, y):
            tweet += fTmp[x] + " "
        tweet += " ::::;:::: " + fTmp[0]
        if tweet not in Result:
            MaxRetweets[tweet] = (fTmp[-1]) 
    MaxRetweets = sorted(MaxRetweets.items(), key = operator.itemgetter(1), reverse = True)
    OUTFILE = r'C:\Users\Ujwal\Desktop\tweepy\maxRetweets'
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
    output_File.write("The top 10 tweets who has the max number of retweets : " +"\n\n\n")

    for x in range (0,n):
        output_File.write(str(x+1) + ". Username: " + MaxRetweets[x][0].split()[-1] + "\n number of retweets: " + str(MaxRetweets[x][1]) + "\n\n\n")
    output_File.close

    #MostUsersEveryHour
    MostUsersEveryHour = {}
    for data in inputfile:
        fTmp = data.split()
        fTmp1 = fTmp[1].split(":")
        twitterTmp = fTmp[0] + " " + fTmp1[1]
        if twitterTmp in Result:
            MostUsersEveryHour[twitterTmp]+=1
        else:
            MostUsersEveryHour[twitterTmp]=1
    MostUsersEveryHour = sorted(MostUsersEveryHour.items(), key = operator.itemgetter(1), reverse = True)
    tp = {}
    totalNumPostsInFile = 0
    for data in MostUsersEveryHour:
        totalNumPostsInFile+=1
        if(data[0].split()[1]) in tp:
            tp[daat[0].split()[1]]+=1
    else:
            tp[data[0].split()[1]]=1
    tp = sorted(tp.items(), key = operator.itemgetter(1))

    totalEntriesToPrint = 10*len(tp)
    OUTFILE = r'C:\Users\Ujwal\Desktop\tweepy\MostUsersEveryHour'
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
    for x in range (0,len(tp)):
   
        k = 10 
        for data in MostUsersEveryHour:
            if k == 0:
                break
            if data[0].split()[1] == tp[x][0]:
                output_File.write("Username: " + data[0].split()[0] + "\n")
                k-=1
    output_File.close
queries()
