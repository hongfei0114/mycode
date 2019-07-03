# cd70a13eb57647ceb6251fe36eca2d34

from wxpy import *
import requests
import json
# 初始化机器人，扫码登陆


bot = Bot(console_qr=2, cache_path="botoo.pkl") # 这里的二维码是用像素的形式打印出来，如果你在win环境上运行，替换为bot=Bot()，pkl是一种

def talk_robot(info='你好啊'):   #定义一个默认参数
    api_url = 'http://www.tuling123.com/openapi/api'  # 图灵接口url
    apikey = 'cd70a13eb57647ceb6251fe36eca2d34'       # 注册图灵生成key 
    data = {'key': apikey, 'info': info}                                   
    r = requests.post(api_url, data=data).text

@robot.register()
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    response = talk_robot(info=message)
    return response
embed()

