import json
file_path='d:\\Python34\\workspace\\bookmarks-2019-12-18.json'
with open(file_path,encoding='utf-8') as f:
    js=json.load(f)
print(js)