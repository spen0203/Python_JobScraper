#exportHtmlResults.py Saves the Results to an Html Document
from bs4 import BeautifulSoup
import datetime

#Creates or reWrites Html Document Containing results from the scraping
def createListingSaveHTML():
    Html_file = open("jobListings.html","w", encoding='utf-8')
    Html_file.write('<html>')
    Html_file.write('<body>')
    html_str = "<h1 style=\"text-align: center\"> POSTINGS FOUND ON: " + str(datetime.datetime.now()) + "</h1>" 
    Html_file.write(html_str)
    
def saveListofPostings(jobTitle, companyName, jobURL, easilyApply, jobDesc, softSkillList, techSkillList):
    Html_file = open("jobListings.html","a", encoding='utf-8')
    html_str = "<hr><h1>EA\t" if easilyApply else "<hr><h1>"
    html_str = html_str + jobTitle.getText().strip() + "</h1><h2>EA\t" + companyName.getText().strip() + "</h2> <a href=\"" + str(jobURL) + "\"> URL LINK </a><br>" + jobDesc.prettify()  + "<h3 style=\"color:green\"><b>TechSkills:</b> <br/> {} </h3> ".format(techSkillList) + "<h3 style=\"color:orange\"><b>SoftSkills:</b> <br/> {} </h3> ".format(softSkillList)
    Html_file.write(html_str)
    Html_file = open("jobListings.html","a", encoding='utf-8')
    Html_file.write(html_str)

#appends ending tags to Joblisting.html after postings are added
def endSaveHTML(totalPostings):
    Html_file = open("jobListings.html","a", encoding='utf-8')
    html_str = "<h1 style=\"text-align: center\"> END OF POSTINGS, FOUND: " + str(totalPostings) + "</h1></body></html>" 
    Html_file.write(html_str)
    Html_file.close()   

def main():
    pass

if __name__ == "__main__":
    main()