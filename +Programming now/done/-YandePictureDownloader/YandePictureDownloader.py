import urllib.request
import re
import os
import time

def getImgList(url):
	print ('Loading...Please wait..')
	page = urllib.request.urlopen(url).read()
	page = page.decode('UTF-8')
	img = re.compile ( r'<a class="directlink largeimg" href="(.+?)">')
	imgList = img.findall (page) 
	return imgList

def saveImg (imgUrl,saveDir):
	startTime = time.time()
	fileRe = re.compile(r'/yande.re (.*)')
	fileName = fileRe.findall(urllib.request.unquote(imgUrl))[0]
	outPutRe = re.compile(r'\d+')
	imgNum = outPutRe.findall(fileName)[0]
	print ('Image ID: [' + imgNum + '] Saving Please wait...')
	if not os.path.exists(saveDir + '/' + fileName):
	    urllib.request.urlretrieve(imgUrl,  saveDir + '/' + fileName)
	print ('Image ID: [' + imgNum + '] has been saved,Processed in' , int(time.time() - startTime) , 'seconds.')

MainDirectory = os.path.dirname(os.path.abspath(__file__))

imgList = getImgList('https://yande.re/post')

if not os.path.exists(MainDirectory+'\\pictures'):
    os.makedirs(MainDirectory+'\\pictures')

for i in imgList:
    saveImg (i, MainDirectory+'\\pictures')

print ('###########################Download completed###########################')