from pandas import Series, DataFrame

# Series 선언
series1 = Series([92600, 94800, 88800, 75400, 92300])
print(series1)

# 총 개수
print('count', series1.count())
# 요약
print('describe', series1.describe())

# 인덱스 접근
print(series1[2])

# series2 선언
series2 = Series([92600, 94800, 88800, 75400, 92300], index=['2022-08-18','2022-08-19','2022-08-20','2022-08-21','2022-08-22'])
print(series2)

# 인덱스 순회
for date in series1.index:
    print('date', date)

# 값 순회
for price in series2.values:
    print('price', price)

# Series3 선언
series_g1 = Series([10,20,30], index=['n1','n2','n3'])
series_g2 = Series([50,40,25], index=['n3','n2','n1'])

# Series 병합 & 계산
sum = series_g1 + series_g2
mul = series_g1 * series_g2
cul = (series_g1 + series_g2) * (0.5 + 1)

print('sum')
print(sum)
print('mul')
print(mul)
print('cul')
print(cul)









