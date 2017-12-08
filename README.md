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









