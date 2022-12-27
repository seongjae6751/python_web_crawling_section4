import pandas as pd

# 기본 읽기
# df = pd.read_csv('c:/section4/csv_s1.csv')
# print(df)

# 행 스킵, 헤더 성격
# df = pd.read_csv('c:/section4/csv_s1.csv', skiprows = [0,1]) # skiprows -> 행 스킵
# print(df)

# 행 스킵, 헤더 성격
# df = pd.read_csv('c:/section4/csv_s1.csv', skiprows = [0,1], header=2) # header(맨위에) -> 뭐 올지 설정
# print(df)

# 헤더 정의
# df = pd.read_csv('c:/section4/csv_s1.csv', skiprows = [0,1], header=None, names=["month",2013,2014,2015]) # names -> 맨 위에
# print(df)

# 인덱스 컬럼 정의
# df = pd.read_csv('c:/section4/csv_s1.csv', skiprows = [0,1], header=None, names=["month",2013,2014,2015], index_col=[0]) # index_col -> 맨 왼쪽
# print(df)

# df = pd.read_csv('c:/section4/csv_s1.csv', skiprows = [0,1], header=None, names=["month",2013,2014,2015], index_col=[0], na_values=['Jan'])
# print(pd.isnull(df)) # isnull은 df넣어서 true or false 를 받음
# print(df)

# 실습 정리 및 인덱스 재정의
# df = pd.read_csv('c:/section4/csv_s1.csv', skiprows = [0,1], header=None, names=["month",2013,2014,2015])
# print(df)
# print(df.index)
# print(list(df.index))
# print(df.index.values)
# print(df.rename(index={0:'aa',1:'bb',2:'cc'}))
# print(df.rename(index=lambda x:x+1))

# 읽기
df2 = pd.read_csv('c:/section4/csv_s2.csv',sep=';', skiprows=[0], header = None, names=['Name','Test1','Test2','Test3','Final','Grade'])
# print(df)

# 칼럼 내용 변경
# df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
# print(df2)

# 평균 칼럼 추가
# df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1) # mean은 평균 내주는 함수 axis=1 은 가로방향 axis=0은 세로방향 평균
# print(df2)

# 합계 칼럼 추가
df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
print(df2)










