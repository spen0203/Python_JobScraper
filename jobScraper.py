#JobScraper.py Launching Class
import exportHtmlResults as exportResults
import scrapeProccessor as scraper


#specific to machine allows connection - google "my user agent" and paste in.
headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def main():
    exportResults.createListingSaveHTML()
    

if __name__ == "__main__":
    main()