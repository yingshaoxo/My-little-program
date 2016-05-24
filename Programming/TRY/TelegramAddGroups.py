#add groups by many keywords.

import ctypes

#Get required functions, strcpy..
strcpy = ctypes.cdll.msvcrt.strcpy
ocb = ctypes.windll.user32.OpenClipboard    #Basic Clipboard functions
ecb = ctypes.windll.user32.EmptyClipboard
gcd = ctypes.windll.user32.GetClipboardData
scd = ctypes.windll.user32.SetClipboardData
ccb = ctypes.windll.user32.CloseClipboard
ga = ctypes.windll.kernel32.GlobalAlloc    # Global Memory allocation
gl = ctypes.windll.kernel32.GlobalLock     # Global Memory Locking
gul = ctypes.windll.kernel32.GlobalUnlock
GMEM_DDESHARE = 0x2000 

def clipboard_get( ):
    ocb(None) # Open Clip, Default task
    pcontents = gcd(1) # 1 means CF_TEXT.. too lazy to get the token thingy ... 
    data = ctypes.c_char_p(pcontents).value
    #gul(pcontents) ?
    ccb()
    return data

def clipboard_paste( data ):
    ocb(None) # Open Clip, Default task
    ecb()
    hCd = ga( GMEM_DDESHARE, len( bytes(data,"ascii") )+1 )
    pchData = gl(hCd)
    strcpy(ctypes.c_char_p(pchData),bytes(data,"ascii"))
    gul(hCd)
    scd(1,hCd)
    ccb()

#Above is about clipboard


key_word = input('Input keywords about some groups you want, (separated by space or Enter directly to default): ')

if (key_word == ''):
    key_word = '.NET Algorithm Android C Chef Clojure Cloud CPP CSharp CSS Data Database Design Elasticsearch Functional Programming Game Git Google Hadoop Hardware iOS Java JavaScript Mac Machine Learning Management Mobile MySQL Network Node Oracle OS PHP Python R Rails RayWenderlich React Robot Ruby Scala Security Software Development Swift Web Development'

word_list = key_word.split(' ')
all_link = ''
for i in word_list:
    link = "https://telegram.me/" + i
    all_link += '\n\n'+link

clipboard_paste(all_link)
print('\nPasted, send to telegram then click them, good luck!')
