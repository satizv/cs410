def moviepage(filemoviename,moviename):
    filemovienip = filemoviename + ".txt"
    filemovienop = filemoviename + ".html"
    filereviewresults = open(filemovienip,'r')
    filereviewhtml = open(filemovienop, 'w')

    filereviewhtml.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Movie Analysis</title>\n")
    filereviewhtml.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>\n</head>\n")
    filereviewhtml.write(
        "<body>\n<div>\n<ul>\n<li> <a href=\"about.html\">About</a></li>\n<li> <a href=\"index.html\">Home</a></li>\n</ul>\n<br>\n</div>\n")
    filereviewhtml.write(
        "<div class=\"section\" id=\"section2\">\n<div class=\"pg3title\">" + moviename +"<br><br></div><div id=\"pg3table\"></div>\n")
    filereviewhtml.write("<table width=\"800\"><tr><td><b>Review</b></td><td><b>Sentiment Score</b></td></tr>")

    print(filemovienip)
    for i in filereviewresults:
        filereviewhtml.write("<tr>\n")
        filereviewhtml.write("<td>" + i.split("|")[0] + "</td>\n")
        filereviewhtml.write("<td>" + i.split("|")[1] + "</td>\n")
        filereviewhtml.write("</tr>\n")

    filereviewhtml.write("</table></div>\n</body>\n</html>")
    filereviewresults.close()
    filereviewhtml.close()


fileoutput = open("movieoutput.txt",'r')
fileindex = open("index.html",'w')
fileindex.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Movie Analysis</title>\n")
fileindex.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>\n</head>\n")
fileindex.write("<body>\n<div>\n<ul>\n<li> <a href=\"about.html\">About</a></li>\n<li> <a href=\"index.html\">Home</a></li>\n</ul>\n<br>\n</div>\n")
fileindex.write("<div class=\"section\" id=\"section2\">\n<div class=\"pg3title\">Top Movies for the week <br><br></div><div id=\"pg3table\"></div>\n")
fileindex.write("<table><tr><td><b>Movie Name</b></td><td><b>Gross</b></td><td><b>Change Pcnt</b></td><td><b>Total Gross</b></td><td><b>Week</b></td><td><b>Avg. Critics Review Score</b></td><td><b>Avg. User Review Score</b></td></tr>")

for i in fileoutput:
    movieuser = i.split("|")[0] + "_user_results"
    moviecritics = i.split("|")[0] + "_critics_results"
    movienumbers = i.split("|")[0] + "_numbers.html"
    fileindex.write("<tr>\n")
    fileindex.write("<td> <a href=\"" + movienumbers + "\">" + i.split("|")[1] + "</a></td>\n")
    fileindex.write("<td>" + i.split("|")[2] + "</td>\n")
    fileindex.write("<td>" + i.split("|")[3] + "</td>\n")
    fileindex.write("<td>" + i.split("|")[4] + "</td>\n")
    fileindex.write("<td>" + i.split("|")[5] + "</td>\n")
    fileindex.write("<td> <a href=\""+ moviecritics + ".html" + "\">" + i.split("|")[7] + "</a></td>\n")
    fileindex.write("<td><a href=\""+ movieuser + ".html" + "\">" + i.split("|")[8] + "</a></td>\n")
    fileindex.write("</tr>\n")

    movieuser = i.split("|")[0] + "_user_results"
    moviecritics = i.split("|")[0] + "_critics_results"
    moviepage(movieuser,i.split("|")[1])
    moviepage(moviecritics, i.split("|")[1])


    linkvar = i.split("|")[6]
    link = "http://www.the-numbers.com/movie/box-office-iframe/" + (linkvar.split("#")[0]).split("/")[2]
    print(link)
    filenumbers = open(movienumbers, 'w')
    filenumbers.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Movie Analysis</title>\n")
    filenumbers.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>\n</head>\n")
    filenumbers.write("<body>\n<div>\n<ul>\n<li> <a href=\"about.html\">About</a></li>\n<li> <a href=\"index.html\">Home</a></li>\n</ul>\n<br>\n</div>\n")
    filenumbers.write("<div class =\"section\" id=\"section2\" ><div class =\"pg3title\">" + i.split("|")[1] + "<br><br></div>\n")
    filenumbers.write("<div class=\"pg3floatleft\" >\n")
    filenumbers.write("<iframe src=\"" + link + "\" frameborder=0 height=370 width=600 scrolling=\"no\" class=\"pg3floatleft\" id=\"charthead1\">You need a Frames Capable browser to view this content.</iframe>\n</div>")
    filenumbers.write("<div class=\"pg3floatright\" style=\"float: right;\">\n<table>")
    filenumbers.write("<tr><td>&nbsp</td><td>Critics</td><td>User</td></tr>")
    filenumbers.write("<tr><td>No of Positive Review Scores</td><td>" + i.split("|")[13] + "</td><td>" + i.split("|")[15] + "</td></tr>")
    filenumbers.write("<tr><td>No of Negative Review Scores</td><td>" + i.split("|")[14] + "</td><td>" + i.split("|")[16] + "</td></tr>")
    filenumbers.write("<tr><td>Lowest Review Score</td><td>" + i.split("|")[9] + "</td><td>" + i.split("|")[11] + "</td></tr>")
    filenumbers.write("<tr><td>Highest Review Score</td><td>" + i.split("|")[10] + "</td><td>" + i.split("|")[12] + "</td></tr>")
    filenumbers.write("<tr><td>Avg. Review Score</td><td>" + i.split("|")[7] + "</td><td>" + i.split("|")[8] + "</td></tr>")
    filenumbers.write("</table>\n</div>\n</body>\n</html>")
    filenumbers.close()





fileindex.write("</table></div>\n</body>\n</html>")



fileoutput.close()
fileindex.close()


