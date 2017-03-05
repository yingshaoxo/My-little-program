import sys
import time
import telepot
from __Xiaoya__ import xiaoya

x = xiaoya('xiaoya', 17, 'telegram')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    #print(msg['text'])

    if content_type == 'text':
        text = msg['text']
        if chat_type == 'private':
            bot.sendMessage(chat_id, x.reply(text))
        if text.count('@XiaoyaBot') > 0 and text.count('remove') == 0 and text.count('rm') == 0:
            text = text.replace('@XiaoyaBot', '').strip('  　\n ')
            bot.sendMessage(chat_id, x.reply(text))

TOKEN = '121899714:AAGAp0rdqSbqzP8-j1wqnUfWJ-lx-L9NLrQ'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

#Keep running.
while 1:
	time.sleep(10)
