import requests
from bs4 import BeautifulSoup

scource=requests.get('https://www.nytimes.com/').text
soup=BeautifulSoup(scource,'lxml')

titles=soup.find_all('h3',class_="css-xxaj7r" )
cols=[x.text.strip() for x in titles]
print (cols)


