#!/usr/bin/python3
# -*- codeing : UTF-8 -*-
import telepot  #引入机器人模块；如果没有，请在命令行写入pip install telepot
import time  #引入时间模块；如果没有，请在命令行写入pip install time

#如出错，请在python的安装目录下寻找pip.exe，将其拖入cmd窗口，再加上空格+install+空格+模块名


bot = telepot.Bot('121899714:AAFyTKIRyn3u3MCi_7DUBIDHFoABcahPM-Y')  #设置密匙(访问令牌)，没有请@BotFather
#print (bot.getMe())  #得到这个机器人的信息

def handle_message(msg):  #这个函数用来接收新信息
       content_type, chat_type, chat_id = telepot.glance(msg)  #分别得到消息类型、聊天场所、聊天id
       print(content_type, chat_type, chat_id)
       print(msg[u'chat'][u'id'])  #输出聊天id
       print(msg[u'text'])  #输出消息内容
       bot.sendMessage(msg[u'chat'][u'id'], msg[u'text'])  #回复发送同样的内容
       
       #f = open('C:\\YS.png', 'rb')  #打开某个本地文件，并取得字节集
       #bot.sendPhoto(msg[u'chat'][u'id'], f)  #然后发给别人，同理还有sendAudio(), sendDocument(), sendSticker(), sendVideo(), and sendVoice()


bot.notifyOnMessage(handle_message)  #关联上面那个def函数用到的代码



while 1:  #为了保持程序运转，十秒一次
    time.sleep(10)