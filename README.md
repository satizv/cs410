# CS410 Final Project - Movie Review Analysis
######                        Abdulkarim Atek
######                        Satish Venkiteswaran

## Introduction
Sentiment analysis in the realm of movie reviews is an important discourse that has been brought up in several papers with some discussion. Natural language processing is the core utility function that is used in these types of analysis’ placing a weight on the sentiment of a movie critic. The sentiment varies widely from very negative to very positive, and an overall score is given to a review to measure whether it exceeded a given threshold, meaning if it was overall a positive or negative review, with an accompanying score. The approach we are taking with critic sentiment, is applying it to how well a movie did in the box office based on how well it was received by critics. The question we are trying to answer is a critically acclaimed movie a hit in the box office?

## Installation
Download all the files in the github folder

Install Python Packages. Use Command line to install packages using pip.


###### Ensure your pip is up to date
```
pip install --upgrade pip
``` 
###### Install Beautiful Soup
``` 
pip install beautifulsoup4
``` 
For issues – Refer https://www.crummy.com/software/BeautifulSoup/bs4/doc/

###### Install Vader Sentiment 
```
pip install vaderSentiment
```
For issues – Refer https://github.com/cjhutto/vaderSentiment

###### Install NLTK 
```
pip install -U nltk
```
For issues – Refer http://www.nltk.org/install.html 


## Execution Steps

###### The crawling scripts (crawlbasic.py, crawlrt.py, mergefiles.py) have been executed and the input and review files are already available in the github folder
```
movieinput.txt
reviewfiles Folder
```

###### Calculate Sentiment Scores using Sentiment_Analysis.py   
```
python Sentiment_Analysis.py
```

On execution of the above script 30 review results and a movieoutput.txt would be generated.

###### Review Results file Example
```
coco_2017_critics_results.txt
coco_2017_user_results.txt
```

###### Review Results file Example
```
movieoutput.txt
```

###### Generate Html Output file
```
python htmlgenerator.py
```

On execution of the above script multiple html files would be generated. 

###### Open index.html in a browser to view the results of the sentiment analysis
```
Open index.html
```

## Architecture

###### Getting Box office Results for the weekend

```
Script Name – crawlbasic.py
Input – None
Output - movienumbers.txt
```

www.the-numbers.com is a website that provides the weekend box office results. 
The crawlbasic.py script crawls the top 15 movies of the weekend from the following url “http://www.the-numbers.com/weekend-box-office-chart” using Beautiful Soup package and creates a output text file movienumbers.txt. Following are the fields in the output file for each of the top 15 movies
a.	Movie Name as in the numbers website
b.	Gross Revenue for the current weekend
c.	Revenue Change from last week in percent
d.	Total Gross Revenue for the movie
e.	No. of week since movie release
f.	Tag links of the numbers website for future reference

Timing – This script can be executed independently. However, the website is updated with the weekend box office information normally on Mondays or early Tuesdays. So the script needs to be executed post the update of the results.  


###### 	Downloading the reviews for Top 15 Movies

```
Script Name – crawlrt.py
Input – None
Output - moviertlist.txt, 30 movie critics and user review csv files for top 15 movies 
```

www.rottentomatoes.com is a website that captures reviews from critics and users. 
The crawlrt.py script crawls the critics and user reviews for the top 15 movies of the weekend from the following url “https://www.rottentomatoes.com/browse/in-theaters/” using Beautiful Soup package. The scripts creates individual pipe separated text files containing the reviews from the critics and users. The script also creates a list of movies for which the reviews have been downloaded. 

Timing – This script can be executed independently. However, the rotten tomatoes website is updated with the current weekend movies normally on Mondays. So the script needs to be executed post the update of the results.  


###### 	Creating an Input file for Sentiment Analysis
```
Script Name – mergefiles.py
Input – movienumbers.txt, moviertlist.txt
Output - movieinput.txt
```

In order to review the timing dependency of both the websites, a merge process to create an input file to create the top 15 movies from both the websites. 
The mergefiles.py script combines the top 15 movies from both the websites into one text file movieinput.txt. The review of this input file helps validating any timing dependencies of both the crawlbasic.py and crawlrt.py scripts. 

Timing – This script needs to be executed after crawlbasic.py and crawlrt.py scripts.


###### 	Running Sentiment Analysis
```
Script Name - Sentiment Analysis.py
Input - movieinput.txt, 30 Movie reviews (critics and user) from top 15 movies
Output - movieoutput.txt, 30 movie critics and user review scores
```

The Sentiment Analysis.py script takes movieinput.txt file and the review files as input and generates the score using vader sentiment package for the individual reviews. The script also generates consolidated results for each movie and creates an output file. The output file movieoutput.txt contains the following fields 
a.	Movie Name in rotten tomatoes
b.	Movie Name in the numbers site
c.	Gross Revenue for the current weekend
d.	Revenue Change from last week in percent
e.	Total Gross Revenue for the movie
f.	No. of week since movie release
g.	Tag links of the numbers website for future reference
h.	Avg. Sentiment Score for critics review
i.	Avg. Sentiment Score for user review
j.	Min. Score of critics reviews
k.	Max. Score of  critics reviews
l.	Min. Score of user reviews
m.	Max. Score of user reviews
n.	No. of positive score for critics reviews 
o.	No. of negative score for critics reviews 
p.	No. of positive score for user reviews 
q.	No. of negative score for user reviews


###### 	Generating UI based on Output File
```
Script Name – htmlgenerator.py
Input – movieoutput.txt, 30 movie critics and user review scores
Output – index.html, Critics Review Score html Pages, User Review Score html Pages, 
         Revenue projection and consolidated Score html page
```

The htmlgenerator.py script would generate the following html files
a.	Index Page – The main html that list the top 15 movies for the week and list the average sentiment score.
b.	Critics Review Score Pages – Html page for each movie listing the critics review and the sentiment score for each of the review.
c.	User Review Score Pages – Html page for each movie listing the user review and the sentiment score for each of the review. 
d.	Revenue projection and consolidated Score page – Html page showing the revenue graph from the-numbers website for the movie and the showing the consolidated values for each movie.

