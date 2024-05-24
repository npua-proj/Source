# job_sources/job_source.py
from abc import ABC, abstractmethod

class JobSource(ABC):
    @abstractmethod
    def fetch_jobs(self):
        pass
