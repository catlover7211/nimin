import time
import pyautogui


filename = time.strftime("./screenshot/%Y-%m-%d %H-%M-%S.png", time.localtime())
filenameeee = time.strftime("%Y-%m-%d %H-%M-%S.png", time.localtime())

def post():
    #open ig
    import webbrowser    
    urL='https://www.instagram.com/'
    webbrowser.get('windows-default').open_new(urL)
    time.sleep(7)

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
    text = 'nimin\n'
    secs_between_keys = 0.1
    pyautogui.typewrite(message=text, interval=secs_between_keys)  

    text = 'screenshot\n'
    secs_between_keys = 0.1
    pyautogui.typewrite(message=text, interval=secs_between_keys)  

    text = "2024-02-20 14-47-26.png\n"
    secs_between_keys = 0.1
    pyautogui.typewrite(message=text, interval=secs_between_keys)  

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

    moveToX = 1425
    moveToY = 287
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
