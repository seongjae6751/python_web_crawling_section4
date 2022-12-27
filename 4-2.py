import urllib.request as req
from bs4 import BeautifulSoup
import os.path

# 다운로드 url
url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
savename = 'c:/section4/forecast.xml'

# 초기 xml 파일 저장
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print('다운로드 확인')

# BeautifulSoup 파싱
xml = open(savename, 'r', encoding = 'utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')

# 지역확인
info = {}
for location in soup.find_all("location"):
    loc = location.find('city').string
    # print(loc)
    weather = location.find_all("tmx")
    # print(weather)
    if not (loc in info):
        info[loc] = []
    for tmx in weather:
        info[loc].append(tmx.string)

# print(info)
# print(sorted(info.keys()))
# print(list(info.keys()))
# print(info.values())

# 각 지역별 날씨 텍스트 쓰기
with open('c:/section4/forecast.txt', 'wt') as f:
    for loc in sorted(info.keys()):
        print('+', loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
            print('-',n)
            f.write('\t'+str(n)+'\n')












