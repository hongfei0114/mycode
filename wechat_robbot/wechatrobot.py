#coding:utf-8

from wxpy import *
import requests
import json

'''
作者：pk哥
公众号：brucepk
日期：2018/07/28
代码解析详见公众号。
如疑问或需转载，请联系微信号：dyw520520，备注来意，谢谢。
'''


#robot = Bot()
robot = Bot(console_qr=2, cache_path="botoo.pkl") # 这里的二维码是用像素的形式打印出来，如果你在win环境上运行，替换为bot=Bot()，pkl是一种

def talk_robot(info='你好啊'):   #定义一个默认参数
    api_url = 'http://www.tuling123.com/openapi/api'  # 图灵接口url
    apikey = 'cd70a13eb57647ceb6251fe36eca2d34'
    data = {'key': apikey, 'info': info}
    r = requests.post(api_url, data=data).text
    response = json.loads(r)['text']
    return response

# 定义一个话痨微信机器人
#@robot.register()
#def reply_my_friend(msg):
#    message = '{}'.format(msg.text)
#    response = talk_robot(info=message)
#    return response
#
# 定义一个当被@才回复的微信机器人
@robot.register()
def print_group_msg(msg):
    if msg.is_at:
        message = '{}'.format(msg.text)
        response = talk_robot(info=message)
        return response

#try:
#    my_friend = robot.friends().search(u'(Hazel)')[0]
#    my_friend.send(u"hello，我是微信机器人！")
#    t = Timer(20,send_news)
#    t.start()
#except:
#    my_friend = robot.friends().search(u'(鸿飞漫天)')[0]
#    my_friend.send(u"今天消息发送失败了")

embed()
