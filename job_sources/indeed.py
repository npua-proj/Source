# job_sources/indeed.py
import requests
from bs4 import BeautifulSoup

INDEED_URL = 'https://www.indeed.com/jobs?q=remote&l='

def fetch_indeed_jobs():
    jobs = []
    response = requests.get(INDEED_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')

        for job in job_listings:
            title = job.find('a', class_='jobtitle').get_text(strip=True).lower()
            company = job.find('span', class_='company').get_text(strip=True).lower()
            location = job.find('div', class_='recJobLoc')['data-rc-loc'].lower()
            url = f"https://www.indeed.com{job.find('a', class_='jobtitle')['href']}"
            tags = [tag.lower() for tag in title.split() if len(tag) > 1]  # Simple tag extraction from title
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'url': url,
                'tags': tags
            })
    return jobs
