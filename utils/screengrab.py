#coding:utf-8



import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api


bbox = {'left':0, 'top':30, 'right':800, 'botton':600}

def grab_screen(bbox, region=None):
    hwin = win32gui.GetDesktopWindow()

    # if region:
    #     left, top, x2, y2 = region
    #     width = x2 - left + 1
    #     height = y2 - top + 1
    # else:
    #     width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    #     height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    #     left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    #     top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    width = bbox['right']
    height = bbox['botton']
    left = bbox['left']
    top = bbox['top']

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype=np.uint8)
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def imshow(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('1', img)
    cv2.waitKey(1)


if __name__ == '__main__':
    while True:
        img = grab_screen(bbox)
        imshow(img)





