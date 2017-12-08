filert = open("moviertlist.txt", "r")
filenumb = open("movienumbers.txt", "r")
filemovie = open("movieinput.txt", "w")

# This script reads the crawl output from crawlbasic.py and crawlrt.py and creates a input file for sentiment analysis
# Input - moviertlist.txt file and movienumbers file
# output - movieinput
i=0
while (i < 15):
    textrt = filert.readline().rstrip('\n')
    textnumb = filenumb.readline().rstrip('\n')
#    print textrt
#    print textnumb
    textmovie = textrt + '|' + textnumb + '\n'
    filemovie.write(textmovie)
#    print textmovie
    i = i + 1

filert.close()
filenumb.close()
filemovie.close()