#!/usr/bin/python3
# -*- codeing : UTF-8 -*-
import telepot  #引入机器人模块；如果没有，请在命令行写入pip install telepot 和pip install telepot
import time  #引入时间模块；如果没有，请在命令行写入pip install time
from ctypes import *#引入dll调用模块
import sys
import os
#如出错，请在python的安装目录下寻找pip.exe，将其拖入cmd窗口，再加上空格+install+空格+模块名

global MainDirectory,dll,token
MainDirectory=os.path.split( os.path.realpath( sys.argv[0] ) )[0]#得到脚本所在目录
dll=windll.LoadLibrary (MainDirectory+"\\AIxiaoya.dll")#注册该dll

token = '121899714:AAGAp0rdqSbqzP8-j1wqnUfWJ-lx-L9NLrQ'  #设置密匙(访问令牌)
bot = telepot.Bot(token)

def handle_message(msg):  #这个函数用来接收新信息
       content_type, chat_type, chat_id = telepot.glance(msg)  #分别得到消息类型、聊天场所、聊天id
       if (content_type=='text'):#如果为 文本信息
           t_id=msg[u'chat'][u'id']#得到聊天id
           t_txt=msg[u'text']#得到对方消息
           number=dll._eventGetMsg(c_char_p(bytes(str(t_id),'utf-8')),c_char_p(bytes(t_txt, 'utf-8')),c_char_p(bytes(token, 'utf-8')))
           if (number>=0):#大于0，表示页数
               PictureDirectory=MainDirectory.replace('\\','\\\\')+'\\book\\'+str(number)+'.png'
               f = open(PictureDirectory, 'rb')
               bot.sendPhoto(msg[u'chat'][u'id'], f)
       else:
           print ('Not text')

bot.notifyOnMessage(handle_message)  #关联上面那个def函数用到的代码


while 1:  #为了保持程序运转，十秒一次
    time.sleep(10)