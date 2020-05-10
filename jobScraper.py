import requests
from bs4 import BeautifulSoup


#specific to machine allows connection - google "my user agent" and paste in.
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

g = 0
while g < 100:
    #URL to be scraped on indeed it goes by 10 per page default
    URL = 'https://ca.indeed.com/jobs?q=Software+%2450%2C000&l=Ottawa%2C+ON&radius=5&jt=fulltime&start=' + str(g)
    print("***********  ", URL, "  ***********")
    g = g + 10

    #returns all the information from the URL
    page = requests.get(URL, headers=headers)

    #Pass the page data to beatiful soup for parsing (soup now contains entire html page)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Collect all job titles from the url
    allJobTitle = soup.findAll(class_="jobtitle")
    allCompanyName = soup.findAll(class_="company")

    y = len(allJobTitle)
    x=0
    for jobTitle in allJobTitle:
        companyName = allCompanyName[x]
        x=x+1
        print("\n----------- Job #", x,"/", y," -----------")
        print(jobTitle.getText().strip())
        print(companyName.getText().strip())