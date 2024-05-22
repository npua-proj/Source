# job_sources/upwork.py
import requests
from bs4 import BeautifulSoup

UPWORK_URL = 'https://www.upwork.com/ab/jobs/search/?q=remote'

def fetch_upwork_jobs():
    jobs = []
    response = requests.get(UPWORK_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('section', class_='air-card')

        for job in job_listings:
            title = job.find('h4', class_='job-title').get_text(strip=True).lower()
            company = 'N/A'  # Upwork listings usually do not have company names in the same way
            location = 'remote'
            url = f"https://www.upwork.com{job.find('a')['href']}"
            tags = [tag.lower() for tag in title.split() if len(tag) > 1]  # Simple tag extraction from title
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'url': url,
                'tags': tags
            })
    return jobs
