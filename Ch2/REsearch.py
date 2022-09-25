from urllib.request import urlopen
from bs4 import BeautifulSoup
#정규 표현식
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.findAll('img', {'src' : re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])