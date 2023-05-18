import requests
from bs4 import BeautifulSoup
import time
import random

while True:  
  time.sleep(15 + random.randint(0, 16))
  request = requests.get(url='http://app2.helwan.edu.eg/HelwanNat/EngHelwan/TermAview.asp?StdCode=441144')
  with open('res.txt', 'w') as f:
      f.write(request.text)
  with open('res.txt', 'r') as f:
      data = f.read()
  soup = BeautifulSoup(data, 'html.parser')
  content = []
  
  for bar in soup.find_all('b'):
      if len(bar.text) > 3:
          continue
      content.append(bar.text)
      
  content = content[1:]
  grades = [[0 for i in range(6)] for _ in range(int(len(content) / 6) + 1)]
  
  for i in range(len(content)):
      j = int(i / 6)
      k = i % 6
      grades[j][k] = content[i]
      
  for grade in grades:
      for i in range(len(grade)):
          if grade[i] == 'á':
              grade[i] = 'D'
          elif grade[i] == 'Ì':
              grade[i] = 'C'
          elif grade[i] == 'ÖÌ':
              grade[i] = 'B'
          elif grade[i] == '':
              grade[i] = '-'
              
      with open('grades.txt', 'a') as f:
        if str(grades) == '[[0, 0, 0, 0, 0, 0]]':
          print('error')
          continue
        f.write(str(grade)+ '\n')
