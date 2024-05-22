# job_sources/remote_co.py
import requests
from bs4 import BeautifulSoup

REMOTE_CO_URL = 'https://remote.co/remote-jobs/'

def fetch_remote_co_jobs():
    jobs = []
    response = requests.get(REMOTE_CO_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', class_='job_listing')

        for job in job_listings:
            title = job.find('h3', class_='job_listing-title').get_text(strip=True).lower()
            company = job.find('div', class_='job_listing-company').get_text(strip=True).lower()
            location = 'remote'
            url = job.find('a')['href']
            tags = [tag.lower() for tag in title.split() if len(tag) > 1]  # Simple tag extraction from title
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'url': url,
                'tags': tags
            })
    return jobs
