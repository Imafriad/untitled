import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'EJLDU16902016267'
        #self.dc['app'] = 'C:\\Users\\Administrator\\AppData\\Roaming\\appiumstudio\\apk\\com.Wf.controller.MainActivity.2.apk'
        self.dc['appPackage'] = 'com.Wf'
        self.dc['appActivity'] = '.controller.MainActivity'
        self.dc['instrumentApp'] = 'true'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

        # 获取屏幕的size
        size = self.driver.get_window_size()
        print(size)
        # 屏幕宽度width
        print(size['width'])
        # 屏幕高度width
        print(size['height'])

    def testUntitled(self):

        #self.driver.swipe(1012, 1210, -20, 1177, 1475)
        #self.driver.swipe(1050, 1247, -20, 1247, 1641)
        #self.driver.swipe(1042, 1280, -20, 1280, 1815)
        #self.driver.swipe(1079, 1342, 1, 1335, 5)
        self.driver.find_element_by_xpath("xpath=//*[@id='url_iv_head']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='立即登录']").click()
        self.driver.swipe(537, 1232, 537, 1337, 615)
        self.driver.find_element_by_xpath("xpath=//*[@hint='邮箱/手机/账号']").send_keys('vivienchen')
        self.driver.execute_script("seetest:client.deviceAction(\"Enter\")")
        self.driver.execute_script("seetest:client.sendText(\"a1234567\")")
        self.driver.execute_script("seetest:client.deviceAction(\"Enter\")")
        self.driver.execute_script("seetest:client.sendText(\"1111\")")
        self.driver.find_element_by_xpath("xpath=//*[@text='登 录']").click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
