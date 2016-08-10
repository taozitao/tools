#codeing=utf-8
# FUNCTION module
#return devices udid[] or False
__author__ = 'wangtao'
import os
import re
def getDevicesId():
    udid = []
    os.system('adb devices > devices.txt')
    fl = open('devices.txt', 'r+') #grant authorization read & write
    text = fl.readlines()
    print 'devices=====' + text
    for i in text[1:-1]:
        devicesList = re.split('\\t',i)
        udid.append(devicesList[0])
        if len(udid) == 0:
            return False
        return udid

