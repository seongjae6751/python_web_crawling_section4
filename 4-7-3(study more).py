import datetime
import FinanceDataReader as fdr

# 조회 시작 & 마감 날짜
start = datetime.datetime(2022,8,1)
end = datetime.datetime(2022,8,19)

# 한국거래소 상장종목 전체
df_krx = fdr.StockListing('KRX')

# 리스트 10개 출력
print(df_krx.head(10))

#출력
print(df_krx.index)
print(df_krx['Symbol'])
print(df_krx.iloc[0])
print(df_krx.describe(include='all', datetime_is_numeric=True))

# finance 사용법/Git
# -> 참고 https://github.com/financedata-org/FinanceDataReader




