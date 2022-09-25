from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

#bs.findAll(tagName, tagAttributes)
# CSS 입력 or 복수의 입력 사용시 대괄호 안에 넣기 '{}' 
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())