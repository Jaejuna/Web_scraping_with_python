from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#div안에 있는 img 태그들을 전부 검색
img = bs.div.findAll("img")

#giftList 데이블에 들어 있는 제품 행 목록 출력
for child in bs.find('table',{'id' : 'giftList'}).children:
    print(child, img)

#형제 다루기
for siblings in bs.find('table',{'id' : 'giftList'}).tr.next_siblings:
    print(siblings)

#부모 다루기(말이 좀 이상한데...)
#본인 태그의 부모 태그들중 바로 전 태그만 출력
print(bs.find('img',{'src' : '../img/gifts/img1/jpg'}).parent.previous_sibling.get_text())