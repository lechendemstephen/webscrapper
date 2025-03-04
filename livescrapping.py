import time

import requests

from bs4 import BeautifulSoup

print('Put some skills you are not fimiliar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


# getting the url of the website to scrap

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=USA&txtKeywords=Python&txtLocation=USA').text

    soup = BeautifulSoup(html_text, 'html.parser')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text

        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'Job Link: {more_info}')
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'{time_wait} minutes...')
        time.sleep(time_wait * 60)
