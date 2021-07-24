import requests
from bs4 import BeautifulSoup

def extract_RO_job(tr):
  a = tr.find("a")
  href = "https://remoteok.io/"+a["href"]
  title = tr.find("h2").text
  company = tr.find("h3").text
  return {'title':title, 'company':company, 'link':href}

def extract_RO_jobs(url):
  jobs = []
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  class_ignore = ["closed", "divider", "expand", "sw-insert", "advertise-here", None]

  for tr in soup.find_all('tr', class_=lambda x: x in class_ignore):
      tr.decompose()
  trs = soup.find_all('tr')
  
  for tr in trs:
    job = extract_RO_job(tr)
    jobs.append(job)
  return jobs


def get_RO_jobs(word):
  url =f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = extract_RO_jobs(url)
  return jobs