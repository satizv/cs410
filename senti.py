filemovie = open("movie.txt",'r+')
for i in filemovie:
    print(i)
    filemovie.write("1")

filemovie.close()
