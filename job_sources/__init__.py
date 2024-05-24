# job_sources/__init__.py
from job_sources.remoteok import RemoteOK

def fetch_all_jobs():
    jobs = []
    remoteok = RemoteOK()
    jobs.extend(remoteok.fetch_jobs())
    return jobs
