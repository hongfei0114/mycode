###第一步：导入库###
from wxpy import *
from threading import Timer

###第二步：生成网页微信登录二维码###
bot = Bot(console_qr=2, cache_path="botoo.pkl") # 这里的二维码是用像素的形式打印出来，如果你在win环境上运行，替换为bot=Bot()，pkl是一种文件格式

###第二步：调用该包中的方法向微信好友发消息###
try:
    my_friend = bot.friends().search(u'（Hazel）')[0]#你朋友的微信昵称，不是你给ta的备注，也不是微信号
    my_friend.send(u"hello，我是微信机器人！")#这里可以随意填写微信内容，可以提升的地方就是你可以从网站上爬取文章或者心灵鸡汤，进行定时发送
    t = Timer(20,send_news)# Timer的第一个参数是表示隔多久发送一次信息，自行设置，这里是20秒
    t.start()
except:
    my_friend = bot.friends().search('鸿飞漫天')[0]# 你的微信昵称，不是微信号
    my_friend.send(u"今天消息发送失败了")

#--------------------- 
#作者：Emily_2018 
#来源：CSDN 
#原文：https://blog.csdn.net/qq_32618817/article/details/80386515 
#版权声明：本文为博主原创文章，转载请附上博文链接！
