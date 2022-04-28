#Import Nessecary Libraries

#PD for data-table scraping
import requests
from bs4 import BeautifulSoup

#Take URL and Round Input
url = str(input("Enter Round 1 Tabroom URL: "))
rounds = int(input("Enter # of Prelims: "))

#Generate all round links
last_part_id = int(url[-2:])
round_links = []
temp_rounds = 0

for i in range(rounds):
  round_links.append(url[0:-2]+str(last_part_id+temp_rounds))
  temp_rounds+=1

print(round_links)

