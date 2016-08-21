import sys
import time
import telepot
from Xiaoya import xiaoya


x = xiaoya('xiaoya', 17)

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		bot.sendMessage(chat_id, x.reply(msg['text']))

TOKEN = '121899714:AAGAp0rdqSbqzP8-j1wqnUfWJ-lx-L9NLrQ'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

#Keep running.
while 1:
	time.sleep(10)