import requests
from bs4 import BeautifulSoup

# getting the url using the requests library
html_text = requests.get('https://www.indeed.com/jobs?q=python+developer&l=United+States&from=searchOnDesktopSerp').text

# preparing soup for the requests and creating an instance for the BeautifulSoup Library
soup = BeautifulSoup(html_text, 'html.parser')

job = soup.find('li', class_='css-5lfssm eu4oa1w0')

job_title = job.find('h2', class_='jobTitle css-198pbd eu4oa1w0').text

print(job_title)




