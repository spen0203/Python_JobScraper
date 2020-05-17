# Python_JobScraper
Job indexing websites have made it easy to find job postings relevant to my field of study. One downside I often find though is the postings skills and requirements often don't match my experiences, this creates lost time that could be better used modifying my resume for applications. Because of this I have decided to create a python scraper that will take my daily job postings and forward the most relevant to me.

v1.
Uses Python and beautiful soup to parse job postings, currently it scrapes 10 pages worth of results returning the company name, position title and description. I hope to add further filtering to the list that will allow me to save specific jobs to a file. Currently This still saves time by allowing the user to read aproximately 150 positions in one place without the need to reload an webpages.

v2. Now filters out job postings based on a minimum year experience, and saves all jobs in the criteria to an html file for easy formated reading. Using basic html speed isn't an issue. to change the minimum experience cut off modify the value on BadFilter.txt (this currently only supports single digits 1-9 but cuts everything greater out)

<hr>
<h1>jobTitle</h1>
<h2>companyName</h2>
<a href="jobURL"> URL LINK </a><br>
jobDesc
<hr>

Next steps will be working on filters and flags, If a certain skill or langauge is required I will set a corresponding flag. Using theese flags I hope to build a modular resume that python can adapt to each posting to get the best results.


I have started creating a spread sheet that contains 3 pages: Skill, Related Work, Unrelated work.
Im going to start with filling Unrelated work with softskills used on that job to best match postings, I decided to start here as it will require the least logic. Skills and Related work will have to create a balance of skills matched to their importance. (Most Techpostings have few soft skills listed compared to technical makes sense)


Going to make a basic word frequency analysis function to make finding keywords easier, similiar words could then be grouped and during the search for word x replace the x in the string with word. This could allow words like 




<h1> Suggested Use </h1>
Adjust the programs vars:

urlCount = 0 # Start count at 0 first results page
urlCountMax = 10 #works in increments of 10 (every 10 is 1 page)
URL = your search on indeed(more filters in search the better)

Run jobScraper.py

After first run completes check 
Keywords_Count.txt - This displays how frequently a word is displayed between all postings.
Keywords_List.txt - Displays only the words without a count.

Using Keywords_Count and Keywords_List determine useful keywords and optionally add more to 
keywordFilters.txt - Stops the machine from counting that word.

*GoodFilter.txt - Keywords here are specific words to watch for. ( Later Update will highlight words when present in posting, return phrases related or directly modify a resume)
*Creation in progress, preffered method if skills are known.
