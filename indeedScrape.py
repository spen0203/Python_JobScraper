#indeedScrape.py Used to scrape details from indeed
import requests
from bs4 import BeautifulSoup

#Print out jobDetails to the console.
def printPosting(jobNum, jobTitle, companyName, jobURL, easilyApply, jobDesc):
    print("\n----------- Job #", jobNum," -----------")
    if(easilyApply == True):
        print("Æ\t", jobTitle.getText().strip())
        print("Æ\t", companyName.getText().strip())
    else:
        print("\t", jobTitle.getText().strip())
        print("\t", companyName.getText().strip())
    print(jobURL)
    print("\n", jobDesc.getText().strip())



#Scrapes the specific posting for title, company, jobdesc
def scrapeJobPosting(jobPosting):
    for scrapeTag in ['jobtitle','company','jobsearch-jobDescriptionText']
        scrapeTag = jobPosting.find(class_=scrapeTag)
    jobTitle, companyName, jobDescription = jobPosting.find(class_="jobtitle"), jobPost.find(class_="company"),soup.find(class_="jobsearch-jobDescriptionText") 
    companyLink = "https://ca.indeed.com" + str(jobPosting.find('a', class_="jobtitle").get('href'))
    easilyApply = True if jobPosting.find(class_="iaLabel") else False #ternariry operator
    jobDescription = soup.find(class_="jobsearch-jobDescriptionText")
    #Need to figure out what todo with this, should i create an object? Json? 


#Scraped the specific URL passing each JobPosting per page
def scrapeIndeedPage(pageURL):
    page = requests.get(pageURL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    for posting in soup.findAll(class_="jobsearch-SerpJobCard"):
        scrapeJobPosting(posting)
    
#Create the indeed URL to be scraped and begin scraping
def main():
    def __init__(self):
        pageNumber, pageUrlNumber, maxPages = 0, 0, 5
        jobCount = 0
        while pageNumber < maxPages:
            print("\n\nPage: ", pageNumber)
            URL = 'https://ca.indeed.com/jobs?q=Software+%2450%2C000&l=Ottawa%2C+ON&radius=5&jt=fulltime&start=' + str(pageUrlNumber)
            print("\n******************************************************\n  ", URL, "\n******************************************************")
            pageUrlNumber =+ 10
            scrapeIndeedPage(URL)

if __name__ == "__main__":
    main()