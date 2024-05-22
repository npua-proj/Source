# job_sources/djinni.py
import requests
from config import config
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def fetch_djinni_jobs():
    try:
        response = requests.get(config.DJINNI_API_URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            jobs = []
            job_listings = soup.find_all('div', class_='list-jobs__item')

            for job in job_listings:
                title_element = job.find('div', class_='list-jobs__title')
                company_element = job.find('div', class_='list-jobs__details__info')
                location_element = job.find('span', class_='location-text')

                if not (title_element and company_element and location_element):
                    logger.warning(f"Skipping incomplete job listing: {job}")
                    continue

                title = title_element.get_text(strip=True).lower()
                company = company_element.get_text(strip=True).lower()
                location = location_element.get_text(strip=True).lower()
                url = config.DJINNI_API_URL

                jobs.append({
                    'title': title,
                    'company': company,
                    'location': location,
                    'url': url,
                    'tags': ['djinni', 'remote']
                })

            return jobs
        else:
            logger.error(f"Failed to fetch jobs from Djinni. Status code: {response.status_code}")
            return []
    except Exception as e:
        logger.exception(f"An error occurred while fetching jobs from Djinni: {e}")
        return []
