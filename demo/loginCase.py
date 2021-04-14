from time import sleep
from appium import webdriver
from androguard.core.bytecodes.apk import APK
from appium.webdriver import Remote
import os
apk_path = "TNAOT_Android_v5.2.0_gtest_20210323_new.apk"

command3 ='adb shell ime set io.appium.settings/.UnicodeIME'
sougou_xiaomi = 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'

def get_devices() -> list:
    all_devices = []
    cmd = "adb devices"
    reslut = os.popen(cmd).readlines()[2:]
    for item in reslut:
        if item != "\n":
            all_devices.append(str(item).split("\t")[0])
    return all_devices


def getPlatForm(dev: str) -> str:
    cmd = 'adb -s {} shell getprop ro.build.version.release'.format(dev)
    reslut = os.popen(cmd).readlines()[0]
    return str(reslut).split("\n")[0]


def get_apkname(apk):
    a = APK(apk, False, "r")
    return a.get_package()


def get_apk_lautc(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()


def isinstallapk(packname: str, devname: str) -> bool:
    cmd = "adb -s {} shell pm list packages -3".format(devname)
    reslut = os.popen(cmd).readlines()
    all_apkname = []
    for i in reslut:
        apkname = str(i).split('\n')[0].split(":")[1]
        all_apkname.append(apkname)
    if packname in all_apkname:
        return True
    return False


def uninstallapk(packname: str, devname: str) -> bool:
    cmd = "adb -s {} shell pm list packages -3".format(devname)
    reslut = os.popen(cmd).readlines()
    all_apkname = []
    for i in reslut:
        apkname = str(i).split('\n')[0].split(":")[1]
        all_apkname.append(apkname)
    if packname in all_apkname:
        cmd = 'adb -s %s uninstall %s ' % (devname, packname)
        os.system(cmd)
        return True
    return False


def installapk(paknamepath: str, devname: str) -> bool:
    cmd = 'adb -s %s install %s' % (devname, paknamepath)
    os.system(cmd)
    return True


def testqqlogin():
    # packname = get_apkname(apk_path)
    # dev = get_devices()[0]
    # is_first_install=False
    # # 1.判断是否安装app
    # is_install = isinstallapk(packname, dev)
    # if is_install is False:
    #     # 2.如果没有安装，则安装
    #     installapk(apk_path, dev)
    #     is_first_install = True
    #
    # # 3.启动apk测试
    # apkname = get_apkname(apk_path)
    # launcheractivity = get_apk_lautc(apk_path)


    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Samsung Galaxy S7_1',#adb  deivces
        'platformVersion': '8.0', #从设置中可以获取
        'appPackage': 'com.tnaot.newspro',#包名
        'appActivity': 'com.tnaot.news.mctnews.detail.activity.MainActivity', # apk的launcherActivity
        # 'skipServerInstallation': True
        # 'browserName': 'chrome',
        'chromedriverExecutable': r"C:\\Users\\23633\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\win\\chromedriver.exe"
        # 'chromeOptions': {'androidProcess', 'WEBVIEW_com.tanot.newspro'}
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(5)
    # # 点击“我的”
    # driver.find_element_by_id("com.tnaot.newspro:id/iv_mine").click()
    # sleep(3)
    # driver.find_element_by_id("com.tnaot.newspro:id/tv_login_btn").click()
    # sleep(3)
    # driver.find_element_by_id("com.tnaot.newspro:id/tv_main_password_login").click()
    # sleep(3)
    # driver.find_element_by_id("com.tnaot.newspro:id/iv_password_arrow_area_code").click()
    # sleep(3)
    # driver.find_element_by_xpath("//*[@text='中国']").click()
    #
    # # 输入用户名
    # driver.find_element_by_id("com.tnaot.newspro:id/et_password_phone_num").send_keys("18054290008")
    # # 输入密码
    # driver.find_element_by_id("com.tnaot.newspro:id/et_phone_password").send_keys("12121212")
    # # 点击登录
    # driver.find_element_by_id("com.tnaot.newspro:id/ibtn_password_login").click()
    print("--------------------")
    list = driver.contexts
    print(list)
    sleep(10)
    print(driver.find_element_by_id("com.tnaot.newspro:id/iv_life").is_displayed())
    sleep(15)
    # driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.ImageView").click()

    # webview = driver.contexts[-1]
    # driver.switch_to.context(webview)

    # ChromeOptions options = new ChromeOptions();
    # options.setExperimentalOption("androidProcess", "WEBVIEW_com.xxx.zhidao");
    # capabilities.setCapability(ChromeOptions.CAPABILITY, options);

    for con in list:
        if con.lower().startswith('webview'):  # if判断若是以webview开头就切换
            sleep(2)
            print("switch context")
            print(con)
            driver.switch_to.context('WEBVIEW_com.tnaot.newspro')
            print("switch success")

    # driver.switch_to.context(driver.contexts[-1])
    print(driver.context)  # 打印出切换到的界面
    print("+++++++++++++++++++++++")
    print(driver.contexts)
    driver.find_element_by_xpath("//*[@class='fish_play_button']")
    driver.find_element_by_xpath("//*[@class='fish_play_button']").click()


    # if is_first_install :
    #     # 首次安装需要加载文件
    #     sleep(50)
    sleep(10)
    # driver.find_element_by_xpath("//*[@text='登录']").click()
    # driver.find_element_by_id('tv.danmaku.bili:id/btn_change_account').click()
    #
    # username=driver.find_element_by_id('tv.danmaku.bili:id/username')
    # username.clear()
    # username.send_keys("name")
    # password=driver.find_element_by_id('tv.danmaku.bili:id/passport_tag')
    # password.clear()
    # password.send_keys("123456")
    # login=driver.find_element_by_id('tv.danmaku.bili:id/btn_login')
    # login.click()
    driver.close()


class demo:
    def __init__(self,driver):
        self.driver = driver
        print("开始测试")
    def ChangeWebview(self):
        '''切换到webview'''
        sleep(5)  # 此处加上睡眠等待，此时向服务器请求数据，一般数据量多时，会获取不到webview和native的界面元素
        d = self.driver  # 调用appium中的driver，tool是用来引用driver
        list = d.contexts  # 将获取到的添加到集合list
        sleep(10)
        print(list)  # 打印查看
        for con in list:
            if con.lower().startswith('webview'):  # if判断若是以webview开头就切换
                sleep(2)
                d.switch_to.context(con)
                print("已经去切换到内嵌网页")
            # else:
            #     continue
        driver.find_element_by_class_name('fish_play_button').click()
        sleep(3)
        d.switch_to.context('NATIVE_APP')
        print('跳出h5，返回app，完成 9')

        print("当前所在的上下文：", d.current_context)  # 打印出切换到的界面
        sleep(10)

    def search(self):
        self.driver.find_element_by_id("com.tnaot.newspro:id/iv_top_search").click()

        self.driver.find_element_by_id("com.tnaot.newspro:id/et_search_keywords").send_keys("多幸运")
        sleep(5)
        # self.driver.press_keycode(66)
        os.system(sougou_xiaomi)
        sleep(5)
        # self.driver.keyevent(84)  无任何作用
        self.driver.press_keycode(66)
        sleep(10)
        os.system(command3)

        self.driver.find_element_by_id("com.tnaot.newspro:id/tv_to_claim").click()
        

    def __del__(self):
        self.driver.quit()

if __name__ == "__main__":
    # testqqlogin()
    desired_caps = {
        'platformName': 'Android',
        # 'deviceName': 'Samsung Galaxy S7_1',  # adb  deivces
        # 'platformVersion': '8.0',  # 从设置中可以获取
        'deviceName': '127.0.0.1:62001',  # adb  deivces
        'platformVersion': '7.1.2',  # 从设置中可以获取

        'appPackage': 'com.tnaot.newspro',  # 包名
        'appActivity': 'com.tnaot.news.mctnews.detail.activity.MainActivity',  # apk的launcherActivity
        # 'skipServerInstallation': True
        # 'browserName': 'chrome',
        # 'chromedriverExecutable': r"C:\\Users\\23633\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\win\\chromedriver.exe"
        # 'chromeOptions':{
        # 'androidProcess', 'WEBVIEW_com.tanot.newspro'}
        "unicodeKeyboard": True,#（用unicode编码方式发送字符串）
        "resetKeyboard": True #（键盘隐藏）
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(5)
    cw = demo(driver)
    cw.ChangeWebview()
    cw.search()

