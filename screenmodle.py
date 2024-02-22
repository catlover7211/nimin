import mss
import mss.tools
import time
import smtplib
import webbrowser
import pyautogui
from copyy import *
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = time.strftime("C:/Users/tcivs/Documents/nimin/screenshot/%Y-%m-%d %H-%M-%S.png", time.localtime())
ffilename = time.strftime("C:/Users/tcivs/Documents/nimin/txt/%Y-%m-%d %H-%M-%S.txt", time.localtime())

ffilenameee = time.strftime("%Y-%m-%d %H-%M-%S.txt", time.localtime())


def screen_shot():
    global filename
    global ffilename
    global ffilenameee

    # 872 17
    moveToX = 872
    moveToY = 17
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    global ffilenameee
    text = ffilenameee
    secs_between_keys = 0.1
    pyautogui.typewrite(message=text, interval=secs_between_keys)
    # enter
    text = '\n'
    secs_between_keys = 0.1
    pyautogui.typewrite(message=text, interval=secs_between_keys)
    time.sleep(0.3)

    # move # 1699 761
    x = 1699
    y = 761
    num_seconds = 1
    pyautogui.moveTo(x, y, duration=num_seconds) 


    # 截圖
    with mss.mss() as sct:
        mon_num = 1
        mon = sct.monitors[mon_num]

        monitor = {
            "top":mon['top'],
            "left":mon['left'],
            "width":mon['width'],
            "height":mon['height'],
            "mon":mon_num
        }
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb,sct_img.size,output=filename)


def sendmail():
    html = '''
    <h1>已截圖</h1>
    '''
    # C:\Users\tcivs\Documents\nimin
    global filename

    msg = MIMEMultipart()                         # 使用多種格式所組成的內容
    msg.attach(MIMEText(html, 'html', 'utf-8'))   # 加入 HTML 內容
    # 使用 python 內建的 open 方法開啟指定目錄下的檔案
    with open(filename, 'rb') as file:
        img = file.read()
    attach_file = MIMEApplication(img, Name=filename)    # 設定附加檔案圖片
    msg.attach(attach_file)                       # 加入附加檔案圖片
    
    msg['Subject']='自動匿名貼文'
    msg['From']='Auto nimin'
    msg['To']='bm963852@gmail.com'
    
    
    
    
    smtp=smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('bm963852@gmail.com','lfcn kwen qohh ryhp')
    status=smtp.send_message(msg)#加密文件，避免私密信息被截取
    if status=={}:
        print("郵件傳送成功!")
    else:
        print("郵件傳送失敗!")
    smtp.quit()

def copy():
        
    global filename
    global ffilename
    global ffilenameee

    k=int(input("How many? : "))

    #open tellonym
    urL='https://tellonym.me/tells'
    webbrowser.get('windows-default').open_new(urL)
    time.sleep(2)



    for i in range(k):
        

        # 610 516
        moveToX = 610
        moveToY = 516
        num_of_clicks = 1
        secs_between_clicks = 1
        pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

        time.sleep(0.3)

        # 610 257
        moveToX = 610
        moveToY = 257
        num_of_clicks = 3
        secs_between_clicks = 0.2
        pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

        time.sleep(0.3)


        # control c
        pyautogui.hotkey('ctrl', 'c')  

        time.sleep(1)

        # ctrl tab
        # 按下ctrl键
        pyautogui.keyDown('alt')
        # 按下tab键
        pyautogui.keyDown('tab')
        # 松开ctrl键盘
        pyautogui.keyUp('alt')

        file=open(ffilename,"a")

        time.sleep(0.3)

        # 872 17
        moveToX = 872
        moveToY = 17
        num_of_clicks = 1
        secs_between_clicks = 1
        pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

        text = ffilenameee
        secs_between_keys = 0.1
        pyautogui.typewrite(message=text, interval=secs_between_keys)

        # enter
        text = '\n'
        secs_between_keys = 0.1
        pyautogui.typewrite(message=text, interval=secs_between_keys)

        time.sleep(0.3)


        # 1699 761
        moveToX = 1699
        moveToY = 761
        num_of_clicks = 1
        secs_between_clicks = 1
        pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

        # ctrl v
        pyautogui.hotkey('ctrl', 'v') 

        # enter
        text = '\n'
        secs_between_keys = 0.1
        pyautogui.typewrite(message=text, interval=secs_between_keys)

        # ctrl s
        pyautogui.hotkey('ctrl', 's') 

        time.sleep(0.3)

        # ctrl tab
        # 按下ctrl键
        pyautogui.keyDown('alt')
        # 按下tab键
        pyautogui.keyDown('tab')
        # 松开ctrl键盘
        pyautogui.keyUp('alt')

        # 557 184
        moveToX = 557
        moveToY = 184
        num_of_clicks = 1
        secs_between_clicks = 1
        pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

        time.sleep(0.3)

        # 往下滑
        pull=-130*(i+1)
        x = 610
        y = 516
        num_seconds = 1
        pyautogui.moveTo(x, y, duration=num_seconds)  
        pyautogui.scroll(clicks=pull)

        time.sleep(0.3)


    # ctrl tab
    # 按下ctrl键
    pyautogui.keyDown('alt')
    # 按下tab键
    pyautogui.keyDown('tab')
    # 松开ctrl键盘
    pyautogui.keyUp('alt')
