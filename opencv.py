import cv2                   # 匯入 OpenCV 函式庫
img = cv2.imread('2024-02-21 20-36-39.png')  # 讀取圖片


x = 445
y = 113
w = 800
h = 600
crop_img = img[y:y+h, x:x+w]        # 取出陣列的範圍
cv2.imwrite('output.jpg', crop_img) # 儲存圖片
cv2.imshow('oxxostudio', crop_img)
cv2.waitKey(0)                      # 按下任意鍵停止
cv2.destroyAllWindows()

# 335 123
# 979 123
#     566