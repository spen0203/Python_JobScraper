#indeedScrape.py Used to scrape details from indeed
import requests
from bs4 import BeautifulSoup
from collections import namedtuple

#Print out jobDetails to the console.
def printPosting(jobTitle, companyName, jobURL, easilyApply, jobDesc):
    print("\n ----------------------------------------------------------")
    if(easilyApply == True):
        print("Æ\t", jobTitle)
        print("Æ\t", companyName)
    else:
        print("\t", jobTitle)
        print("\t", companyName)
    print(jobURL)
    print("\n", jobDesc.getText().strip())



#Scrapes the specific posting for title, company, jobdesc and returns details found
def scrapeJobPosting(jobPosting,headers, jobID):
    indeedposting = namedtuple("Job", "jobTitle companyName jobURL easilyApply jobDesc")

    jobTitle, companyName, jobDesc = '', '', ''
    jobURL = "https://ca.indeed.com" + str(jobPosting.find('a', class_="jobtitle").get('href'))
    page = requests.get(jobURL, headers=headers) #new soup object of specific job page
    soup = BeautifulSoup(page.content, 'html.parser')
    if (jobPosting.find(class_="jobtitle") and jobPosting.find(class_="company") and soup.find(class_="jobsearch-jobDescriptionText")):
        jobTitle, companyName, jobDesc = jobPosting.find(class_="jobtitle").getText().strip() , jobPosting.find(class_="company").getText().strip() ,soup.find(class_="jobsearch-jobDescriptionText") 
    easilyApply = True if jobPosting.find(class_="iaLabel") else False #ternariry operator
    
    posting = indeedposting(jobTitle, companyName, jobURL, easilyApply, jobDesc)
    
    return posting



#Scraped the specific URL passing each JobPosting per page
def scrapeIndeedPage(pageURL,headers):
    page = requests.get(pageURL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #indeedposting = namedtuple("JobID", "jobTitle companyName jobURL easilyApply jobDesc")
    jobPostings = []

    for posting in soup.findAll(class_="jobsearch-SerpJobCard"): 
        indeedposting = scrapeJobPosting(posting,headers, len(jobPostings))
        jobPostings.append(indeedposting)
    #print(jobPostings)
    return jobPostings  
    
#Create the indeed URL to be scraped and begin scraping
def main(headers, maxpages):
    jobPostings = []
    pageNumber, pageUrlNumber, maxPages = 0, 0, maxpages
    while pageNumber < maxPages:
        print("\n\nPage: ", pageNumber)
        URL = 'https://ca.indeed.com/jobs?q=Software+%2450%2C000&l=Ottawa%2C+ON&radius=5&jt=fulltime&start=' + str(pageUrlNumber)
        print("\n******************************************************\n  ", URL, "\n******************************************************")
        pageUrlNumber += 10
        jobPostings += scrapeIndeedPage(URL, headers)
        pageNumber += 1
    return jobPostings

