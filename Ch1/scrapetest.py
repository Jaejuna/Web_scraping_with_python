from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#
def getTitle(url):
    try:
        # url 함수 임포트 -> html 변수에 넣기
        html = urlopen(url)
        #웹 예외 처리
    except HTTPError as e:
        return None
    try:
        #read() 함수 호출하지 않고 urlopen이 반환하는 파일 객체를 바로 사용
        #첫 번째 매개변수는 HTML 텍스트
        #두 번째 매개변수는 구문 분석기이다.
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 타이틀인 body태그 안에 h1 태크 속성 변수에 넣기
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title == None:
    print('Title could not be found')
else:
    print(title)