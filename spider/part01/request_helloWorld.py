import requests
import os

url = 'http://www.sogou.com/'

response = requests.get(url=url)

# print(response.text)
print(response.encoding, response.status_code, response.headers)

# response.encoding = 'utf-8'

with open('./sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)

