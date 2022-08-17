# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:37:30 2022

@author: Skull
"""

import cv2
import os
import numpy as np
import time

now_path = os.getcwd()
"======================================="
camera_number1 = 0
camera_number2 = 1
cut_start = 0
cut_stop = 435
baseline_save_path = "baseline"
"======================================="
baseline_save_path = now_path + "\\" + baseline_save_path

try:
    os.mkdir(baseline_save_path)
    print("成功創建資料夾: " + baseline_save_path)
except:
    print("資料夾已存在: " + baseline_save_path)

checkpoint_x_1_cam1 = 400
checkpoint_y_1_cam1 = 0
checkpoint_x_1_cam2 = 400
checkpoint_y_1_cam2 = cut_stop

cap1 = cv2.VideoCapture(camera_number1)
print("0號相機啟動")
cap2 = cv2.VideoCapture(camera_number2)
print("1號相機啟動")

now = 0
while now < 30:
    ret0, frame1 = cap1.read()
    ret1, frame2 = cap2.read()
    now = now + 1



now = 0
while now < 120:
    ret0, frame1 = cap1.read()
    ret1, frame2 = cap2.read()
    
    frame2 = cv2.flip(frame2, 0)
    frame2 = cv2.flip(frame2, 1)
    
    combine_videos = np.concatenate((frame2[cut_start:cut_stop,:,:], frame1), axis=0)
    cv2.imwrite(baseline_save_path + "\\" + str(now) + ".jpg", combine_videos)
    cv2.imshow('combine', combine_videos)
    now = now + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# 釋放攝影機
cap1.release()
# 釋放攝影機
cap2.release()
# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()







