from flask import Flask, render_template, request, redirect, send_file
from scrapper_so import get_jobs
from scrapper_ro import get_RO_jobs
from scrapper_wwr import get_WWR_jobs
from save import save_to_file

app = Flask("FlaskScrapper")
#fake DB
db = {}

@app.route("/") 
def home():
  return render_template("index.html") #해당 html 파일 랜더링

@app.route("/report") 
def report():
  word = request.args.get('word',str)
  if word:
    word = word.lower()
    existingJobs = db.get(word)

    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word) + get_WWR_jobs(word) + get_RO_jobs(word)
      #jobs 변수에 3개 사이트 스크래핑 결과 저장

      db[word] = jobs
      #fake db에 스크래핑 결과 저장
      #print(jobs)

  else:
    return redirect("/")

  return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs) 

#CSV 추출시
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
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")


app.run(host = "0.0.0.0") #repl.it 환경에서 개발 시