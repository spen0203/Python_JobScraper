# Python_JobScraper 
Job indexing websites have made it easy to find job postings relevant to my field of study. One downside I often find though is the postings skills and requirements often don't match my experiences, this creates lost time that could be better used modifying my resume for applications. Because of this I have decided to create a python scraper that will take my daily job postings and forward the most relevant to me.

v1.
Uses Python and beautiful soup to parse job postings, currently it scrapes 10 pages worth of results returning the company name, position title and description. I hope to add further filtering to the list that will allow me to save specific jobs to a file. Currently This still saves time by allowing the user to read aproximately 150 positions in one place without the need to reload an webpages.

v2. Now filters out job postings based on a minimum year experience, and saves all jobs in the criteria to an html file for easy formated reading. Using basic html speed isn't an issue. to change the minimum experience cut off modify the value on BadFilter.txt (this currently only supports single digits 1-9 but cuts everything greater out)

v3. Completly Refactored and made more Pythonic, Made the Code much more Readible and adaptible with several helper functions spread across 4 python files and 4 text files. The Program now Uses a Standardized NamedTuple so more job posting websites can be appended in the future. 

Functionality I added more effecient Filtering of bad posts and implemented a sort based off number of matching Technical Skills. Also corrected the minimum experience cutoff error of v2.



<h1>Example HTML Layout: </h1>
<hr>
<h1>jobTitle</h1>
<h2>companyName</h2>
<a href="jobURL"> URL LINK </a><br>
<p> jobDesc .... "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

<h3>TechSkills: </h3>
{'agile', 'Marketing', 'development', 'framework', 'process', 'Java', 'c++', 'OOP'} 

<h3>SoftSkills: </h3>
{'driven', 'perform', 'participate', 'help',  'problem-solving', 'communication', 'successful', 'analytical', } 
<hr>


<h1> Suggested Use </h1>
<h3>Adjust the programs vars:</h3>
<h4>jobScraper.py :</h4>
</t>maxpage = ___ # Number of pages to scrape 

<h4>scrapeProccessor.py :</h4>
</t>headers = { "User-Agent": '________'}  #Google "my user agent" paste result

<h4>indeedScrape.py :</h4>
</t>URL = your search on indeed(more filters in search the better)
</t>IE:<u>https://ca.indeed.com/jobs?q=Software+%2450%2C000&l=Ottawa%2C+ON&radius=5&jt=fulltime&start= </u>


</br> Run jobScraper.py

<p>Once it completes running open jobListings.html to see all the job postings relevant to you, in a single scrollable page sorted by technical matching rank.</p>


<h1>Future Goals</h1>
<li>Add scrapeLinkedin.py to find jobs from linkedin </li>

<li>Implement an automatic resume adoption system </li>
<p>This would match the required  Technical and Soft Skill Matches and return a sentence that is relevant to my previous work and the new position. This would result in a completly unique resume for each job and almost completly automate my job application proccess</p>

<li>Implement Natural Languge Proccessing</li>
<p> Currently my system is working off predetermined keyword lists to try and match the best positions. Originaly I was going to set flags and use a word bank to pick sentences that "most" match a job, If I learn Natural Language Proccessing I could automate this and allow the machine to filter, comprehend and respond to each task.
<br/>
This is the much harder method but will allow me to experience the most and learn Machine Learning. It will be a riskier but more rewarding task that could advance my project and skills much more.
</p>
