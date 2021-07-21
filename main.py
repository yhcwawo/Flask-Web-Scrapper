# Flask는 파이썬으로 웹사이트 만들게 도와주는 micro(설정 일일이 해주지 않아도 됨)-framework
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
#from save import save_to_file

app = Flask("FlaskScrapper")

db = {}

# @는 바로 아래에 있는 함수를 찾음
@app.route("/") #누군가 /로 접속시도시 파이썬 함수 실행 
def home():
  return render_template("index.html") #html 파일을 메인(유저)에게 보내주기

@app.route("/report") 
def report():
  word = request.args.get('word',str)
  if word:
    word = word.lower()
    existingJobs = db.get(word)

    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
      print(jobs)

  else:
    return redirect("/")

  return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs) 

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
        raise Exception()

    word = word.lower()
    jobs = db.get(word)

    if not jobs:
      raise Exception()
    return f"Genrate CSV for {word}"

    

  except:
    return redirect("/") 
  



"""
@app.route("/<username>") #각기 다른 url 찾을 수 있음
def potato(username):
  return f"Hello your name is {username}"
#html 템플릿 만들기
"""
 
app.run(host = "0.0.0.0") #repl.it에서 작업하느라 host를 저렇게 설정