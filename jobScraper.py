#JobScraper.py Launching Class
import exportHtmlResults as exportResults
import scrapeProccessor as scraper


#specific to machine allows connection - google "my user agent" and paste in.


def main():
    exportResults.createListingSaveHTML()
    scraper.main()
    

if __name__ == "__main__":
    main()