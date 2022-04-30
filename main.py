#Import Nessecary Libraries
#PD for data-table scraping
import pandas as pd
import requests
from bs4 import BeautifulSoup

def find_speaks(x, speak):
  
  nums = []
  
  for i in range(len(x)):
    if(x[i].isdigit()):
      nums.append(int(x[i]))

  if (speak):
    first_speak = float(nums[0] * 10) + float(nums[1]) + float(nums[2]*0.1)
    second_speak = float(nums[4] * 10) + float(nums[5]) + float(nums[6]*0.1)
    
  else:
    first_speak = float(nums[0] * 10) + float(nums[1]) + float(nums[2]*0.1)
    second_speak = float(nums[3] * 10) + float(nums[4]) + float(nums[5]*0.1)

  return (first_speak + second_speak) / 2
    

#Take URL and Round Input
url = str(input("Enter Round 1 Tabroom URL: "))
rounds = int(input("Enter # of Prelims: "))
ask_speak = str(input("Does the tournament list speaker positions y/n: "))

speak_pos = False

if(ask_speak == 'y'):
  speak_pos = True

#Generate all round links
last_part_id = int(url[-2:])
round_links = []

temp_rounds = 0
for i in range(rounds):
  round_links.append(url[0:-2]+str(last_part_id+temp_rounds))
  temp_rounds += 1

#Open Links

try:
  
  for i in range(len(round_links)):
  
    round_html = requests.get(round_links[i])
    round_soup = BeautifulSoup(round_html.text, 'html.parser')
    
    dfs = pd.read_html(round_html.text)
    table = dfs[0]
  
    #Iterate through rows
    for j in range(len(table)):
  
      try:
        t1 = find_speaks(str(table.iloc[j,4]), speak_pos)
        t2 = find_speaks(str(table.iloc[j,5]), speak_pos)
    
        average = float(t1+t2)/2
    
        print(str(table.iloc[j,2]) + " : " + str(average))
  
      except:
        print("BYE ROUND - NO SPEAKS TABULATED")

except:
  
  pass


  

  
