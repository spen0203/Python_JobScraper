#scrapeProccessor.py Used to procces information returned from the webscrapers
#Will call indeedScraper, LinkedinScraper etc and be returned an object or standerdized item.
#Then I will use the items inside filterScore to determine the best match and sort method before
#returning or saving the complete list


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

#Remove any none relevant chars and standerdize the text to lowerCase
def stripJobDescription(jobDesc):
    regexTextStrip = re.compile('([^a-zA-Z\+#-])') 
    return regexTextStrip.sub(' ', jobDesc).lower()

# Filters out jobs not fit to display.
#ie: 10 years experience, None Tech jobs etc
def badFilters():
    pass

def filterScore():
    pass

#will control what filters to apply to postings
def filterController():
    pass

def main():
    

if __name__ == "__main__":
    main()