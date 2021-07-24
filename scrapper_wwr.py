import requests
from bs4 import BeautifulSoup

def extract_WWR_job(li):
  a = li.find("a", recursive=False)
  href = "https://weworkremotely.com/"+a["href"]
  company = a.find("span", {"class":"company"}).text
  title = a.find("span", {"class":"title"}).text
  return {'title':title, 'company':company, 'link':href}

def extract_WWR_jobs(url):
  jobs = []
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  articles = soup.find_all("article")
  article1 = articles[0].find_all("li")
  article1 = article1[:-1]
  article2 = articles[1].find_all("li")
  article2 = article2[:-1]

  lis = article1 + article2

  for li in lis:
    # print(result["data-jobid"])
    job = extract_WWR_job(li)
    jobs.append(job)
  return jobs

def get_WWR_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_WWR_jobs(url)
  return jobs