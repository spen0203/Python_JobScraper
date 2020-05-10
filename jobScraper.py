import requests
from bs4 import BeautifulSoup

#specific to machine allows connection - google "my user agent" and paste in.
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

totalJobs = 0

def filter():
    badFiltersFile = open("BadFilter.txt", "r")
    badFiltersContent = badFiltersFile.readlines()
    minExperienceLimit = badFiltersContent[2][15]
    print("exclude >=", minExperienceLimit, "years minimum experience")

#After the main program scrapes a job link it will open it here to scrape for more details specific to the position.
def details_scrape(jobURL):
    print("\tJOB DETAILS:")
     #returns all the information from the URL
    page = requests.get(jobURL, headers=headers)

    #Pass the page data to beatiful soup for parsing (soup now contains entire html page)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Collect all contents of the job description (This will need to be parsed for key words, requirments and skills)
    jobDescription = soup.find(class_="jobsearch-jobDescriptionText")

    print(jobDescription.getText().strip())

filter()
g = 0
while g < 100:
    #URL to be scraped on indeed it goes by 10 per page default
    URL = 'https://ca.indeed.com/jobs?q=Software+%2450%2C000&l=Ottawa%2C+ON&radius=5&jt=fulltime&start=' + str(g)
    print("\n\n\n******************************************************\n  ", URL, "\n******************************************************")
    g = g + 10

    #returns all the information from the URL
    page = requests.get(URL, headers=headers)

    #Pass the page data to beatiful soup for parsing (soup now contains entire html page)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Collect all job titles from the url
    allJobTitle = soup.findAll(class_="jobtitle")
    allCompanyName = soup.findAll(class_="company")
    allCompanyLinks = soup.findAll('a', class_="jobtitle")
    y = len(allJobTitle)
    x=0
    for jobTitle in allJobTitle:
        companyName = allCompanyName[x]
        companyLink = "https://ca.indeed.com" + allCompanyLinks[x].get('href')
        x=x+1
        print("\n----------- Job #", x,"/", y," -----------")
        print(jobTitle.getText().strip())
        print(companyName.getText().strip())
        print(companyLink)
        details_scrape(companyLink)
        totalJobs = totalJobs + 1
        
print("\n\n Total Jobs Presented: " , totalJobs , " \n\n") 
        #Now i will have to call a method to scrape the specific URL of each job for its requirments, skills and few potential keywords

        #Then i will have to decide on a filtering system to decide what jobs should then be emailed or updated to a spreadsheet for me to apply.

        #I could then look into potential ranking, automated resume editing and automated resume submissions to make finding my future career an easier task.