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

Next steps will be working on filters and flags, If a certain skill or langauge is required I will set a corresponding flag. Using theese flags I hope to build a modular resume that python can adapt to each posting to get the best results.
