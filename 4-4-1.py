import simplejson as json
# import json

# Dict(Json) 
data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'seoul'
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon'
})

# print(data)

# data = {'people': [{'from': 'seoul', 'name': 'Kim', 'website': 'naver.com'}, {'from': 'Busan', 'name': 'Park', 'website': 'google.com'}, {'from': 'Incheon', 'name': 'Lee', 'website': 'daum.net'}]}

# Dict(Json) -> Str
e = json.dumps(data, indent=4)
# print(type(e))
# print(e)

# str -> Dict(Json)
d = json.loads(e)
# print(type(d))
# print(d)

with open('c:/section4/member.json', 'w') as outfile:
    outfile.write(e) # e가 문자열이라서 write를 써줌

with open('c:/section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    print("=====")
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('website: ' + p['website'])
        print('from: ' + p['from'])
    








