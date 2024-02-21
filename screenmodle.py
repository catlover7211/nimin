import mss
import mss.tools
import time
import smtplib
import webbrowser    
import pyautogui
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = None
filenameeee = None

def screen_shot():
    pull=int(input("page choose 1 2 3 : "))
    if pull==1:
        pull=-200
    elif pull==2:
        pull=-900
    elif pull==3:
        pull=-1500
    
    #open tellonym
    urL='https://tellonym.me/tells'
    webbrowser.get('windows-default').open_new(urL)
    time.sleep(2)

    # 往下滑
    x = 0
    y = 540
    num_seconds = 1
    pyautogui.moveTo(x, y, duration=num_seconds)  

    pyautogui.scroll(clicks=pull)

    moveToX = 0
    moveToY = 540
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

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
        global filename
        global filenameeee
        filename = time.strftime("C:/Users/tcivs/Documents/nimin/screenshot/%Y-%m-%d %H-%M-%S.png", time.localtime())
        filenameeee = time.strftime("%Y-%m-%d %H-%M-%S.png", time.localtime())
        mss.tools.to_png(sct_img.rgb,sct_img.size,output=filename)


def sendmail():
    html = '''
    <h1>已截圖</h1>
    '''
    # C:\Users\tcivs\Documents\nimin


    msg = MIMEMultipart()                         # 使用多種格式所組成的內容
    msg.attach(MIMEText(html, 'html', 'utf-8'))   # 加入 HTML 內容
    # 使用 python 內建的 open 方法開啟指定目錄下的檔案
    with open(filename, 'rb') as file:
        img = file.read()
    attach_file = MIMEApplication(img, Name=filenameeee)    # 設定附加檔案圖片
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





    #open ig
    import webbrowser    
    urL='https://www.instagram.com/'
    webbrowser.get('windows-default').open_new(urL)
    time.sleep(3)



    # 将鼠标移动到(moveToX,moveToY)位置，点击鼠标num_of_clicks次，每次点击间隔secs_between_clicks秒
    # button表示单击方式，'left'左键单击，'middle'中键单击，'right'右键单击
    moveToX = 73
    moveToY = 736
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


    moveToX = 73
    moveToY = 794
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


    moveToX = 958
    moveToY = 693
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


    moveToX = 75
    moveToY = 406
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

    moveToX = 290
    moveToY = 802
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


    # 在当前位置输入文字text，每个字符输入间隔secs_between_keys秒
    # \n表示换行
    text = f'nimin\screenshot\{filenameeee}\n'
    secs_between_keys = 0.1
    pyautogui.typewrite(message=text, interval=secs_between_keys)  

    # text = 'screenshot\n'
    # secs_between_keys = 0.1
    # pyautogui.typewrite(message=text, interval=secs_between_keys)  

    # text = filenameeee
    # secs_between_keys = 0.1
    # pyautogui.typewrite(message=text, interval=secs_between_keys)  

    # 比例
    moveToX = 701
    moveToY = 868
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

    moveToX = 701
    moveToY = 799
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

    # 放大
    moveToX = 751
    moveToY = 862
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

    x = 753
    y = 803
    num_seconds = 1
    pyautogui.moveTo(x, y, duration=num_seconds) 

    x = 870
    y = 803
    num_seconds= 1
    pyautogui.dragTo(x, y, duration=num_seconds)  

    moveToX = 1206
    moveToY = 278
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    # 1425 267

    moveToX = 1425
    moveToY = 287
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

    pyautogui.confirm('發送匿名?')

    # moveToX = 1425
    # moveToY = 287
    # num_of_clicks = 1
    # secs_between_clicks = 1
    # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
