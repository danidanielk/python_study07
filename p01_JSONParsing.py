#카카오 개발자 사이트  -> 로그인 -> 문서 -> 검색API가이드 의 DAUM검색 아래 개발가이드 -> 오른쪽에 책검색 
from urllib.parse import quote
from http.client import HTTPSConnection
from json import loads

#필요한 데이터 챙겨서 책 검색하면 책 제목,작가 , 할인가 내용 출력 해주세요

q= quote(input("검색 : "))
h= {"Authorization" : "KaKaoAK 0ad31319314db7770c095cf2a6bcbd63"}

hc= HTTPSConnection("dapi.kakao.com")
hc.request("GET", "/v3/search/book?query="+q,  headers=h)
resBody=hc.getresponse().read()

KaKaoBook = loads(resBody) #loads = import 할때 이닛 써있는걸로한다.  이문장은 JS ->python 으로 변환. 

books= KaKaoBook["documents"]

for b in books:
    print(b["title"],"-",b["authors"][0])
    print(b["sale_price"])
    print(b["contents"])
    print("---------")