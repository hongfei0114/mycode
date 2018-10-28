import requests

# url = 'https://www.sogou.com/web?query=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=4955&sst0=1540693439703&lkt=3%2C1540693434748%2C1540693435012&sugsuv=00C8177FD20CE6EA593967D49F1E7719&sugtime=1540693439703'
url = 'https://www.sogou.com/'

param = {
    'puery': '美女图片'
}

response = requests = requests.get(url=url, params=param)

page_text = response.text

print(page_text)