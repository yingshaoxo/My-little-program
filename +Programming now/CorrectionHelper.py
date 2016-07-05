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

def SplitSentences(text):
    text = text.replace('.', '.\n')
    text = text.replace('?', '?\n')
    text = text.replace('!', '!\n')
    text = text.replace(';', ';\n')
    sentences_list = text.split('\n')

    return sentences_list


text = input('Enter your article: ')
result = ''
print(SplitSentences(text))
for sentence in SplitSentences(text):
    result += sentence + '\n\n——————————————\n\n'
clipboard_paste(result)
