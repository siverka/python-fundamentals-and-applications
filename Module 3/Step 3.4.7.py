import requests, re

url = 'http://pastebin.com/Ck7U7J84'
# url = input()
response = requests.get(url)
pattern = r'<a.*href=[\'\"](\w*://)*(\w+\.\w+\.*\w*)'
f = re.findall(pattern, response.text)
print(len(f))

