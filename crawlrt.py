from bs4 import BeautifulSoup
import requests
import re
import ast
import time

#response = requests.get('https://www.rottentomatoes.com/m/blade_runner_2049/')
#html =  response.text.encode('utf-8')
#soup = BeautifulSoup(html, 'html.parser')

#for datapr in soup.find_all('p',class_="comment clamp clamp-6"):
#    print datapr.text

#response = requests.get('https://www.rottentomatoes.com/m/blade_runner_2049/reviews/')
#html =  response.text.encode('utf-8')
#soup = BeautifulSoup(html, 'html.parser')

#for datapr in soup.find_all('div',class_="the_review"):
#    print datapr.text

# Input - Movie Name, Url, Reviewtype
# Output - Create a text file with the review content
def crawl_review(filename,newurl,reviewtype):
    fi = open(filename, "w")
    newurlresponse = requests.get(newurl)
    newurlhtml = newurlresponse.text.encode('utf-8')
    newurlsoup = BeautifulSoup(newurlhtml, 'html.parser')
    for newurldata in newurlsoup.find_all('div', class_=reviewtype):
        fi.write(newurldata.text.encode('ascii', 'ignore'))
        fi.write('|')
        print newurldata.text
    fi.close()
    time.sleep(2)

# Main Crawling job to get the list of movies in theaters
response = requests.get('https://www.rottentomatoes.com/browse/in-theaters/')
html =  response.text.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

# Rotten Tomatoes has a jsonLdSchema json containing the url of each of its movie
datapr = soup.find(id="jsonLdSchema").text
#print datapr

#converting a unicode to a dict datatype
dict1 = ast.literal_eval(datapr)

#Extracting a list of movies from the dict

movielist =  dict1.get('itemListElement')
#print type(dict1.get('itemListElement'))

# The loop structure executes 15 times to call the crawl_review fn to generate separate txt files for critic and user review for each movie
# Critic review are present with "the_review" class and the user review are present in the user_review tag in the RT website

filist = open("moviertlist.txt","w")

i=0
while (i<5):
    print movielist[i].get('url')[3:]
    filetext = movielist[i].get('url')[3:]
    print filetext
    filist.write(filetext)
    filist.write('\n')
    criticsurl = "https://www.rottentomatoes.com" + movielist[i].get('url') + "/reviews"
    userurl = criticsurl + "/?type=user"
    crawl_review(filetext + "_critics.csv",criticsurl,"the_review")
    crawl_review(filetext + "_user.csv",userurl,"user_review")
    i=i+1
    print(i)

filist.close()