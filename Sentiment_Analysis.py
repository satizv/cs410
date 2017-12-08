from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer
import csv

# input - File name
# Output - Create a csv file for each movie review page
# Output - Calculate Total Score,Min score,Max score,number of positive score,no of negative score

def sentiment(filename):
    filenameip = 'reviewfiles/' + filename + ".csv"
    filenameop = filename + "_results.txt"
    fileop = open(filenameop,'w')
    tot = 0.0
    minval = 9999
    maxval = -9999
    nopos = 0
    noneg = 0
    with open(filenameip) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            sentences = row
            for sentence in sentences:
                analyzer = SentimentIntensityAnalyzer()
                vs = analyzer.polarity_scores(sentence)
                stringVS= str(vs)
#                print(stringVS)
                data = stringVS.split("'compound': ")[1]
#                print((sentence, data))
                if (sentence != ""):
                    fileop.write(sentence + "|" + data.rstrip('}') + '\n')
                    tot = tot + float(data.rstrip('}'))
                    if (float(data.rstrip('}')) < minval):
                        minval = float(data.rstrip('}'))
                    if (float(data.rstrip('}')) > maxval):
                        maxval = float(data.rstrip('}'))
                    if (float(data.rstrip('}')) > 0):
                        nopos = nopos + 1
                    else:
                        noneg = noneg + 1
            fileop.close()
    #print(tot)
    return tot,minval,maxval,nopos,noneg
#               newdata = sentence, data




fileinput = open("movieinput.txt",'r')
fileoutput = open("movieoutput.txt",'w')
# Read the input file and create an output file with the review scores
for i in fileinput:
#    print(i)
#    print(i.split("|")[0])
    critictot,criticmin,criticmax,criticsnopos,criticsnoneg = sentiment(i.split("|")[0] + "_critics")
    usertot,usermin,usermax,usernopos,usernoneg = sentiment(i.split("|")[0] + "_user")
    criticavg = critictot / (criticsnopos + criticsnoneg)
    useravg = usertot / (usernopos + usernoneg)
#    print(critictot)
#    print(criticavg)
#    print(useravg)
    fileoutput.write(i.rstrip('\n') + '|' + str(criticavg)  + '|' + str(useravg) + '|'  + str(criticmin)  + '|' + str(criticmax)  + '|' + str(usermin)  + '|' + str(usermax) + '|' + str(criticsnopos)  + '|' + str(criticsnoneg) + '|' + str(usernopos)  + '|' + str(usernoneg) + '\n' )


fileinput.close()
fileoutput.close()