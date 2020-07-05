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
# Defined in BadFilter.txt
#ie: Minimum 10 years experience
def badFilters(jobPost):
    print(jobPost)
    if jobPost.jobTitle == '' or jobPost.companyName == '' or jobPost.jobDesc.getText().strip() == '':
        return True
    #Start by filtering out minimum years experience
    badFiltersFile = open("TextFilters/BadFilter.txt", "r")
    badFiltersContent = badFiltersFile.readlines()
    minExperienceLimit = int(re.sub('[^0-9]','',badFiltersContent[2][14:18])) 
    for i in range(minExperienceLimit,100):
        minExperienceRegex = re.compile(r"(?:min(?:imum)? )?" + str(i) +  "\+? (?:year(?:s)?)? ?(?:of)? ?(?:experience)? ?(?:required)?")
        if minExperienceRegex.search(jobPost.jobDesc.getText().strip()):
            return True            
    return jobPost



#find good keywords as definded in text files, matches them in each job to better highlight required skills
def goodFilters(post):

    softSkillList = {word for word in open("TextFilters/GoodSoftSkillFilter.txt","r", encoding='utf-8').read().split() if word in post.jobDesc.getText().strip().split()}
    techSkillList = {word for word in open("TextFilters/GoodTechnicalFilter.txt","r", encoding='utf-8').read().split() if word in post.jobDesc.getText().strip().split()}

    filteredPosting = namedtuple("Job", "jobTitle companyName jobURL easilyApply jobDesc softSkill techSkill")
    return filteredPosting(post.jobTitle, post.companyName, post.jobURL, post.easilyApply, post.jobDesc, softSkillList, techSkillList)


#Applies Good and Bad filters to each posting, returns list of only valid posts
def filterScore(jobPostings):
    filteredPosts = []
    for post in jobPostings:
        if badFilters(post) != True: 
            filteredPosts.append(goodFilters(post))
    return filteredPosts
    

def displayList(jobPostings):
    for post in jobPostings:
        print(post)
        print("\n--------------------------\n")

def main(maxpages):
    jobPostings = indeed.main(headers, maxpages) #Gets list of namedtuple of all jobs found by indeedscrape
    jobPostings = filterScore(jobPostings) #filter list of posting
    return jobPostings
