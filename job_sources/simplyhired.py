# job_sources/simplyhired.py
import requests
from bs4 import BeautifulSoup

SIMPLYHIRED_URL = 'https://www.simplyhired.com/search?q=remote&l='

def fetch_simplyhired_jobs():
    jobs = []
    response = requests.get(SIMPLYHIRED_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', class_='SerpJob')

        for job in job_listings:
            title = job.find('a', class_='jobposting-title').get_text(strip=True).lower()
            company = job.find('span', class_='jobposting-company').get_text(strip=True).lower()
            location = job.find('span', class_='jobposting-location').get_text(strip=True).lower()
            url = f"https://www.simplyhired.com{job.find('a', class_='jobposting-title')['href']}"
            tags = [tag.lower() for tag in title.split() if len(tag) > 1]  # Simple tag extraction from title
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'url': url,
                'tags': tags
            })
    return jobs
