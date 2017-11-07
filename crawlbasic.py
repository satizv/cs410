from bs4 import BeautifulSoup
import requests
import re
response = requests.get('http://www.the-numbers.com/weekend-box-office-chart')
html =  response.text.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

moviename = []
movielink = []
for wrapper in soup.find_all(href=re.compile("tab=box-office")):
    movielink.append(wrapper.get('href'))
#    print wrapper.get('href')
    moviename.append(wrapper.text)

# Class name data has the 8 fields - Number, Week, Gross, Change, Theatres, Gross per theatre, Total Gross and Week
moviedata = []
for datapr in soup.find_all('td',class_="data"):
#    print datapr.text
    moviedata.append(datapr.text)

#print moviedata[2] --
#print moviedata[3]
#print moviedata[6]
#print moviedata[7]

fi = open("movienumbers.txt","w")
# Pipe Separated  file with 6 fields - Movie Name|Gross|Change pcnt|Total Gross|Week|link
#0*8+2
i=0
while (i < 5):
    filetext = moviename[i].encode('ascii', 'ignore') + "|" + moviedata[i*8+2].strip()+ "|" + moviedata[i*8+3].strip()+ "|" + moviedata[i*8+6].strip()+ "|" + moviedata[i*8+7].strip()+ "|" + movielink[i].strip()
    fi.write(filetext)
    fi.write('\n')
    print filetext
    i=i+1

fi.close()


