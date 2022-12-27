import pickle #(객체, 텍스트)직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = 'c:/section4/test.bin'
tfilename = 'c:/section4/test.txt'

data1 = 77
data2 = "Hello, world"
data3 = ["car", "apple", "house"]

# 바이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f) # dumps(문자열 직렬화) # dump = 파일 저장
    pickle.dump(data2, f)
    pickle.dump(data3, f)

# 텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(str(data2))
    f.write('\n')
    f.writelines('\n'.join(data3))

# 바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f) # Loads(문자열 역직렬화) # load = 파일 불러오기
    print(type(b), ' Binary Read1 | ', b)
    b = pickle.load(f) 
    print(type(b), ' Binary Read2 | ', b)
    b = pickle.load(f) 
    print(type(b), ' Binary Read3 | ', b)

# 텍스트 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), 'Text Read' + str(i) + ' | ', line, end='')


#       텍스트 데이터                          |  바이너리 테이터
# 장점 : 텍스트 에디터 편집 가능, 가독성 좋음,  | 크기 작음, 동영상 이미지 등
#        즉시 수정                             |
# 단점 : 크기가 큼                             | 에디터 편집 불가, 데이터 저장 영역 위치 정의
















