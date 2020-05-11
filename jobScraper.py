import requests
from bs4 import BeautifulSoup

#specific to machine allows connection - google "my user agent" and paste in.
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}



## jobCardScrape
# Takes the jobPost Div and continues to strip information from its description.
def jobCardScrape(jobPost):   
    jobTitle = jobPost.find(class_="jobtitle")
    companyName = jobPost.find(class_="company")
    companyLink = "https://ca.indeed.com" + str(jobPost.find('a', class_="jobtitle").get('href'))
    if (jobPost.find(class_="iaLabel") ):
        print("Æ\t", jobTitle.getText().strip() ," Æ")
    else:
        print("Æ\t", jobTitle.getText().strip())
    print("Æ\t", companyName.getText().strip())
    print(companyLink)
    details_scrape(companyLink)

def details_scrape(jobURL):
    print("\nJOB DETAILS:")
     #returns all the information from the URL
    page = requests.get(jobURL, headers=headers)
    #Pass the page data to beatiful soup for parsing (soup now contains entire html page)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Collect all contents of the job description (This will need to be parsed for key words, requirments and skills)
    jobDescription = soup.find(class_="jobsearch-jobDescriptionText")

    #Then i will have to decide on a filtering system to decide what jobs should then be emailed or updated to a spreadsheet for me to apply.
    #I could then look into potential ranking, automated resume editing and automated resume submissions to make finding my future career an easier task.

    print(jobDescription.getText().strip())









totalJobs = 0
urlCount = 0 # Start count at 0 first results page
urlCountMax = 20 #works in increments of 10 (every 10 is 1 page)
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


    x = 0
    for jobPost in allJobPosts:
        x=x+1
        print("\n----------- Job #", x,"/", totalPageListings," -----------")
        jobCardScrape(jobPost) #send jobPost to be scraped for more specific details
        totalJobs = totalJobs + 1

print("\n\n Total Jobs Presented: " , totalJobs , " \n\n") 
