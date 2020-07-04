#scrapeProccessor.py Used to procces information returned from the webscrapers
#Will call indeedScraper, LinkedinScraper etc and be returned an object or standerdized item.
#Then I will use the items inside filterScore to determine the best match and sort method before
#returning or saving the complete list
import indeedScrape as indeed
import re, collections
from collections import namedtuple

headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

#jobTitle, company

#Print out the list of word Frequencies
def printWordFrequencyAnalysis(strippedDesc):
    for count, word in wordFrequencyAnalysis(strippedDesc).items():
        print(word,count)

#Takes a string and returns the Frequency of each word
def wordFrequencyAnalysis(strippedDesc):
    return collections.Counter(word for word in strippedDesc.split())

# Used to find each unique word in a posting
def uniqueWordList(strippedDesc):
    return {word for word in strippedDesc.split()}   


# Filters out jobs not fit to display.
#ie: 10 years experience, None Tech jobs etc
def badFilters():
    pass

def filterScore():
    pass

#will control what filters to apply to postings
def filterController():
    pass

def displayList(jobPostings):
    for post in jobPostings:
        print(post.jobTitle + '\n' + post.companyName + '\n' + post.jobURL + '\n\n' + post.jobDesc)
        print("\n--------------------------\n")

def main():
    jobPostings = indeed.main(headers) #Gets list of namedtuple of all jobs found by indeedscrape
    
    displayList(jobPostings)
    
   


if __name__ == "__main__":
    main()


#Named tuple will be used to store all the postings, faster than object 

#jobPostings = namedtuple("Job", "jobTitle companyName jobURL easilyApply jobDesc softSkills technicalSkills")

#designer = Job(jobTitle="designer", companyName="Apple", jobURL="www.apple.com...", easilyApply=True,
#               jobDesc="lorem ipsum dolor...", softSkills="...", technicalSkills="...")
#
#    print(designer)