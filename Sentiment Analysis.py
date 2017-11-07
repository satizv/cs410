from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer
import csv


def sentiment(filename):
    filenameip = filename + ".csv"
    filenameop = filename + "_results.txt"
    fileop = open(filenameop,'w')
    tot = 0.0
    with open(filenameip) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            sentences = row
            for sentence in sentences:
                analyzer = SentimentIntensityAnalyzer()
                vs = analyzer.polarity_scores(sentence)
                stringVS= str(vs)
                data = stringVS.split("'compound': ")[1]
                print((sentence, data))
                fileop.write(sentence + "|" + data.rstrip('}') + '\n')
                tot = tot + float(data.rstrip('}'))
            fileop.close()
    #print(tot)
    return tot
#               newdata = sentence, data



fileinput = open("movieinput.txt",'r')
fileoutput = open("movieoutput.txt",'w')
for i in fileinput:
    print(i)
    print(i.split("|")[0])
    critictot = sentiment(i.split("|")[0] + "_critics")
    usertot = sentiment(i.split("|")[0] + "_user")
    print(critictot)
    fileoutput.write(i.rstrip('\n') + '|' + str(critictot)  + '|' + str(usertot) + '\n' )


fileinput.close()
fileoutput.close()
