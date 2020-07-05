#JobScraper.py Launching Class
import exportHtmlResults as exportResults
import scrapeProccessor as scraper


def sortfunc(e):
    return len(e.techSkill)

#creates html file and adds list from ScrapeProccessor to it
def main():
    count = 0
    maxpages = 10
    exportResults.createListingSaveHTML()
    for post in sorted(scraper.main(maxpages), reverse=True, key=sortfunc):
        #print(post)
        exportResults.saveListofPostings(post.jobTitle, post.companyName, post.jobURL, post.easilyApply, post.jobDesc, post.softSkill, post.techSkill)
        count += 1
    exportResults.endSaveHTML(count)

if __name__ == "__main__":
    main()