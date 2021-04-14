# import os
# from time import sleep
#
# # 小米手机自带的搜狗输入法
# sougou_xiaomi = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
# # 自己重新下载的搜狗输入法
# sougou = 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'
# # appium默认输入法
# appium = 'adb shell ime set io.appium.settings/.UnicodeIME'
#
# # 通过os包切换系统输入法为自己重新下载的搜狗输入法
# os.system(sougou)
# # 暂停2秒
# sleep(2)
# # appium模拟搜狗输入法的搜索键 66表示是搜索键的物理兼键值
# driver.press_keycode(66)
# # 暂停2秒
# time.sleep(2)
# # 通过os包切换回appium默认输入法
# os.system(appium)


#coding=utf-8
import sys
# sys.setdefaultencoding('utf8')

import os

command0 ='adb shell ime list -s'
command1 ='adb shell settings get secure default_input_method'
command2 ='adb shell ime set com.android.inputmethod.latin/.LatinIME'
command3 ='adb shell ime set io.appium.android.ime/.UnicodeIME'


command4 ='adb shell ime set io.appium.settings/.UnicodeIME'
sougou_xiaomi = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'

#列出系统现在所安装的所有输入法
print(os.system(command0))
#打印系统当前默认的输入法
print(os.system(command1))
#切换latin输入法为当前输入法
#os.system(command2)
#切换appium输入法为当前输入法
#os.system(command3)

class InputMethod:
    # 切换latin输入法为当前输入法
    def enableLatinIME(self):
        os.system(command2)

    # 切换appium输入法为当前输入法
    def enableAppiumUnicodeIME(self):
        os.system(command3)
