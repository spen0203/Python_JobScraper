import requests
from bs4 import BeautifulSoup
import re
import datetime

#specific to machine allows connection - google "my user agent" and paste in.
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

x = 0


## jobCardScrape
# Takes the jobPost Div and continues to strip information from its description.
def jobCardScrape(jobPost):   
    jobTitle = jobPost.find(class_="jobtitle")
    companyName = jobPost.find(class_="company")
    companyLink = "https://ca.indeed.com" + str(jobPost.find('a', class_="jobtitle").get('href'))
    if (jobPost.find(class_="iaLabel") ):
        easilyApply = 1
    else:
        easilyApply =0
    
    details_scrape(jobTitle, companyName,  companyLink, easilyApply)

def details_scrape(jobTitle, companyName, jobURL, easilyApply):
    #print("\nJOB DETAILS:")
     #returns all the information from the URL
    page = requests.get(jobURL, headers=headers)
    #Pass the page data to beatiful soup for parsing (soup now contains entire html page)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Collect all contents of the job description (This will need to be parsed for key words, requirments and skills)
    jobDescription = soup.find(class_="jobsearch-jobDescriptionText")

    #Then i will have to decide on a filtering system to decide what jobs should then be emailed or updated to a spreadsheet for me to apply.
    #I could then look into potential ranking, automated resume editing and automated resume submissions to make finding my future career an easier task.
    filterScore(jobTitle, companyName, jobURL, jobDescription, easilyApply)


def filterScore(jobTitle, companyName, jobURL, jobDesc, easilyApply):
    #Start by filtering out minimum years experience
    badFiltersFile = open("BadFilter.txt", "r")
    badFiltersContent = badFiltersFile.readlines()
    minExperienceLimit = int(badFiltersContent[2][15])
    #print(minExperienceLimit)
    badMatchFlag = 0 #Flag set to 1 if a match <= minExperienceLimit
    #Use Regex now to try and find any mention of minimum __ years experience, ( ie. 7 , anything 7 or GT would be discarded)
    while((minExperienceLimit <= 30) & (badMatchFlag == 0)):
        minExperienceRegex = re.compile(r"(?:min(?:imum)? )?" + str(minExperienceLimit) +  "\+? (?:year(?:s)?)? ?(?:of)? ?(?:experience)? ?(?:required)?")
        if minExperienceRegex.search(jobDesc.getText().strip()):#check for match
            #print("minimum experience beyond cutoff") #regex correctly takes value from file
            badMatchFlag = 1 #set Flag if match found
        minExperienceLimit = minExperienceLimit + 1 #increment minExperience limit
    if(badMatchFlag == 0):
        # printPosting(jobTitle, companyName, jobURL, easilyApply, jobDesc)
        wordFrequencyAnalysis(jobDesc)
        #printWordsList()
        saveListofPostings(jobTitle, companyName, jobURL, easilyApply, jobDesc)


def printPosting(jobTitle, companyName, jobURL, easilyApply, jobDesc):
    print("\n----------- Job #", x," -----------")
    if(easilyApply == 1):
        print("Æ\t", jobTitle.getText().strip())
        print("Æ\t", companyName.getText().strip())
    else:
        print("\t", jobTitle.getText().strip())
        print("\t", companyName.getText().strip())
    print(jobURL)
    print("\n", jobDesc.getText().strip())

#reWrites Joblisting.html and formate basic html
def createSaveHTML():
    Html_file= open("jobListings.html","w", encoding='utf-8')
    Html_file.write('<html>')
    Html_file.write('<body>')
    html_str = "<h1 style=\"text-align: center\"> POSTINGS FOUND ON: " + str(datetime.datetime.now()) + "</h1>" 
    Html_file.write(html_str)


#appends ending tags to Joblisting.html after postings are added
def endSaveHTML():
    global x 
    Html_file = open("jobListings.html","a", encoding='utf-8')
    html_str = "<h1 style=\"text-align: center\"> END OF POSTINGS, FOUND: " + str(x) + "</h1>" 
    Html_file.write(html_str)
    Html_file.write('</body>')
    Html_file.write('</html>')
    Html_file.close()   

#appends each job posting to the html page
def saveListofPostings(jobTitle, companyName, jobURL, easilyApply, jobDesc):
    global x 
    x = x + 1
    if(easilyApply == 1):
        html_str = "<hr><h1>EA\t" + jobTitle.getText().strip() + "</h1><h2>EA\t" + companyName.getText().strip() + "</h2> <a href=\"" + str(jobURL) + "\"> URL LINK </a><br>" + jobDesc.prettify() 

    else:
        html_str = "<hr><h1>\t" + jobTitle.getText().strip() + "</h1><h2>\t" + companyName.getText().strip() + "</h2> <a href=\"" + str(jobURL) + "\"> URL LINK </a><br>" + jobDesc.prettify() 
    Html_file = open("jobListings.html","a", encoding='utf-8')
    Html_file.write(html_str)
   

# wordFrequencyAnalysis()
# Reads every job description counting each unique word.
wordsList = ["the"]
wordsCountList = [0]
def wordFrequencyAnalysis(jobDesc):
    global wordsList
    global wordsCountList
    regexTextStrip = re.compile('[^a-zA-Z]') #if its not text its not a keyword (years arent required)
    newjobDesc = regexTextStrip.sub(' ', jobDesc.getText()) #Strip none chars
    for newWord in newjobDesc.lower().split(): 
        for existingWord in wordsList:
            matchFlag = 0
            if newWord.strip().lower() == existingWord: 
            	wordIndex = wordsList.index(newWord)
            	wordsCountList[wordIndex] = wordsCountList[wordIndex] + 1
            	matchFlag = 1
            	break
        if matchFlag == 0:
                wordsList.append(newWord)
                wordsCountList.append(1)

# Sorts the WordsList by most used word
# wordFrequencyAnalysis
def sortWordsList():
    global wordsList
    global wordsCountList
     #Sort words by assoaciated count, tutorial: https://kite.com/python/answers/how-to-sort-two-lists-together-in-python
    zipList = zip(wordsCountList, wordsList) #merge lists togethor
    sortList = sorted(zipList) #sort list
    tupleList = zip(*sortList)
    wordsList, wordsCountList = [list(tuple) for tuple in tupleList]

#Prints list from wordFrequencyAnalysis()
def printWordsList():
    global wordsList
    global wordsCountList
    sortWordsList()
    wordCount = 0
    while wordCount < len(wordsList):
        print(wordsList[wordCount], " - " , wordsCountList[wordCount] )         
        wordCount = wordCount + 1 

#Saves list from wordFrequencyAnalysis()
def saveWordsList():
    global wordsList
    global wordsCountList
    sortWordsList()
    keyWordfile = open("keywordsList.txt","w", encoding='utf-8')
    wordCount = 0
    while wordCount < len(wordsList):
        newLine = str(wordsList[wordCount]) + " - " + str(wordsCountList[wordCount]) + str(" \n")
        keyWordfile.write(newLine)
        wordCount = wordCount + 1 
    keyWordfile.close()


createSaveHTML() #rewrites the html document for newest scrape

urlCount = 0 # Start count at 0 first results page
urlCountMax = 10 #works in increments of 10 (every 10 is 1 page)
while urlCount < urlCountMax:
    #URL to be scraped on indeed it goes by 10 per page default
    print("\n\nPage: ", (urlCount/10)+1 )
    URL = 'https://ca.indeed.com/jobs?q=Software+%2450%2C000&l=Ottawa%2C+ON&radius=5&jt=fulltime&start=' + str(urlCount)
    print("\n******************************************************\n  ", URL, "\n******************************************************")
    urlCount = urlCount + 10 #after creating URL to be used increment by 10 for next page.

    #returns all the information from the URL
    page = requests.get(URL, headers=headers)

    #Pass the page data to beatiful soup for parsing (soup now contains entire html page)
    soup = BeautifulSoup(page.content, 'html.parser')

    allJobPosts = soup.findAll(class_="jobsearch-SerpJobCard") #get each posting based off the class

    totalPageListings = len(allJobPosts) #total results returned per page


    for jobPost in allJobPosts:
        jobCardScrape(jobPost) #send jobPost to be scraped for more specific details

endSaveHTML()
print("\n\n Total Jobs Presented: " , x , " \n\n") 
#printWordsList() 
saveWordsList()


# 
#                       * how can i optionally make this 9?
#(?:min(?:imum)?)? ?(?:[6-9]|[0-9]\d)\+? (?:year(?:s)?)? ?(?:of)? ?(?:experience)? ?(?:required)?
#         minExperienceRegex = re.compile(r"(?:min(?:imum)?)? ?(?:["+ str(minExperienceLimit) + "-9]|[0-9]\d)\+? (?:year(?:s)?)? ?(?:of)? ?(?:experience)? ?(?:required)?")


#Solution
# (?:min(?:imum)? )?6\+? (?:year(?:s)?)? ?(?:of)? ?(?:experience)? ?(?:required)?
# "(?:min(?:imum)? )?" + str(minExperienceLimit) +  "\+? (?:year(?:s)?)? ?(?:of)? ?(?:experience)? ?(?:required)?"