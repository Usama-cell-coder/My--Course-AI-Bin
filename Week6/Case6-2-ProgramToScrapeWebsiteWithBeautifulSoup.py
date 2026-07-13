#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
print(soup.prettify())
 
table = soup.find('div', attrs = {'class':'a-carousel'}) 
 
for row in table.find_all('div',
                         attrs = {'class':'a-carousel'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" ")[0]
    quote['author'] = row.img['alt'].split(" ")[1]
    quotes.append(quote)
 
filename = 'Week3/inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)