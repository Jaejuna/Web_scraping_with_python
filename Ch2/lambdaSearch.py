from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#태그들 중 속성이 정확히 2개 있는 
print(bs.findALL(lambda tag: len(tag.attrs) == 2))

#결과는 같으나 bs 기본 함수로도 같은 결과를 낼 수 있다는 것을 보여줌
print(bs.findALL(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?'))
print(bs.findALL('', text= 'Or maybe he\'s only resting?'))