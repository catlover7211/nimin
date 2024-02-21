import pyautogui
import webbrowser
import time



def copy():

    k=int(input("How many? : "))

    #open tellonym
    urL='https://tellonym.me/tells'
    webbrowser.get('windows-default').open_new(urL)
    time.sleep(2)

    ffilename = time.strftime("C:/Users/tcivs/Documents/nimin/txt/%Y-%m-%d %H-%M-%S.txt", time.localtime())
    ffilenameee = time.strftime("%Y-%m-%d %H-%M-%S.txt", time.localtime())

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
