import pandas as pd

# 읽기
df2 = pd.read_csv('c:/section4/csv_s2.csv',sep=';', skiprows=[0], header = None, names=['Name','Test1','Test2','Test3','Final','Grade'])
# print(df)

# 칼럼 내용 변경
# df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
# print(df2)

# 평균 칼럼 추가
df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1) # mean은 평균 내주는 함수 axis=1 은 가로방향 axis=0은 세로방향 평균
# print(df2)

# 합계 칼럼 추가
df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
print(df2)

# df2.to_csv('c:/section4/result_s1.csv')
df2.to_csv('c:/section4/result_s1.csv', index = False)









