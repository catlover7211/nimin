import cv2
import time


filenamecv2 = time.strftime("C:\\Users\\tcivs\\Documents\\nimin\\screenshot\\%Y-%m-%d %H-%M-%S.png", time.localtime())
filenamecv2out = time.strftime("C:\\Users\\tcivs\\Documents\\nimin\\output\\%Y-%m-%d %H-%M-%S.png", time.localtime())

img = cv2.imread(filenamecv2)  # 讀取圖片


x = 445
y = 113
w = 800
h = 600
crop_img = img[y:y+h, x:x+w]        # 取出陣列的範圍
cv2.imwrite(filenamecv2out, crop_img) # 儲存圖片
cv2.imshow(filenamecv2out, crop_img)
cv2.waitKey(0)                      # 按下任意鍵停止
cv2.destroyAllWindows()