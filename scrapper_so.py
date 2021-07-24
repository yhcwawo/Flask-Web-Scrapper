import requests
from bs4 import BeautifulSoup

def get_last_page(url):
  result = requests.get(url) 
  soup = BeautifulSoup(result.text, "html.parser") # 모든 html 소스코드 가져오기
  pagination = soup.find("div", {"class" : "s-pagination"})
  pages = pagination.find_all("a") #(find()는 한 개만)
  last_page = pages[-2].get_text(strip = True)# 가장 큰 숫자를 가져올 때, <next> 버튼 내용을 없애준 상태여야 마지막의 페이지 숫자를 손쉽게 가져올 수 있다 # [-1]이 마지막 내용인 next이니 그 전 숫자인 86을 가져오려면 [-2]
  #integer 형변환
  return int(last_page) 

def extract_job(html):
  title = html.find("h2", {"class" : "mb4"}).find("a")["title"] # 직무명
  company, location = html.find("h3", {"class":"fc-black-700"}).find_all("span",recursive = False) #recursive = False #recursive로 리스트 언팩킹
  company = company.get_text(strip = True) #공백 삭제
  location = location.get_text(strip = True)
  job_id = html['data-jobid']
  return {
    'title' : title,
    'company': company,
    'location': location,
    'link' : f"https://stackoverflow.com/jobs/{job_id}"
    }

def extract_jobs(last_page, url):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping StackOverflow Page: {page}") # scrapping test
    result = requests.get(f"{url}&pg={page+1}") #index는 0부터 시작하기에 +1을 해줌
    soup = BeautifulSoup(result.text, "html.parser") #Nested Form
    results = soup.find_all("div", {"class" : "-job"})

    for result in results:
     job = extract_job(result)
     jobs.append(job)
  return jobs

def get_jobs(word):
 url = f"https://stackoverflow.com/jobs?q={word}&sort=i"
 last_page = get_last_page(url)
 jobs = extract_jobs(last_page, url)
 return jobs