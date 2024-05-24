# job_sources/remoteok.py
import requests
from config import config
from job_sources.job_source import JobSource
import logging

logger = logging.getLogger(__name__)

class RemoteOK(JobSource):
    def fetch_jobs(self):
        try:
            response = requests.get(config.REMOTEOK_API_URL)
            if response.status_code == 200:
                jobs = response.json()
                return [{
                    'title': job.get('position', 'N/A').lower(),
                    'company': job.get('company', 'N/A').lower(),
                    'location': job.get('location', 'N/A').lower(),
                    'url': job.get('url', 'N/A'),
                    'tags': [tag.lower() for tag in job.get('tags', [])]
                } for job in jobs]
            else:
                logger.error(f"Failed to fetch jobs from RemoteOK. Status code: {response.status_code}")
                return []
        except Exception as e:
            logger.exception(f"An error occurred while fetching jobs from RemoteOK: {e}")
            return []
