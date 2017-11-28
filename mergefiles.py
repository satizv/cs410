filert = open("moviertlist.txt", "r")
filenumb = open("movienumbers.txt", "r")
filemovie = open("movieinput.txt", "w")

i=0
while (i < 4):
    textrt = filert.readline().rstrip('\n')
    textnumb = filenumb.readline().rstrip('\n')
#    print textrt
#    print textnumb
    textmovie = textrt + '|' + textnumb + '\n'
    filemovie.write(textmovie)
    print textmovie
    i = i + 1

filert.close()
filenumb.close()
filemovie.close()