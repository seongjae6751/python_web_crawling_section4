import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import datetime

# 조회 시작 날짜
start = datetime.datetime(2018,2,1)
end = datetime.datetime(2018,2,17)

# 네이버 주식 정보 조회
df_naver = fdr.StockListing('KRX: 035420')

# 카카오 주식 정보 조회
df_kakao = fdr.StockListing('KRX: 035720')

# 출력
print(df_naver)
print(df_kakao)

fig = plt.fiure