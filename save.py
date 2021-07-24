import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w", encoding='utf-8')
  writer = csv.writer(file)
  writer.writerow(["Title", "Company","Location", "Link"])
  for job in jobs:
    writer.writerow(list(job.values()))
     # jobs에 저장된 {} 형태는 dictionary 라서 값(values)만 불러올 수 있는 dictionary 기능 제공함 #list()로 감싸서 dict_values로 묶인 상태를 없앰
  return