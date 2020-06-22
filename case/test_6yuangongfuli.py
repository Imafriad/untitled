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
        self.dc['appPackage'] = 'com.Wf'
        self.dc['appActivity'] = '.controller.MainActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='item_home_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='员工福利']]").click()
        self.driver.press_keycode(4)
        #系统返回按钮
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.LinearLayout' and ./*[@id='item_home_icon'] and ./*[@text='员工福利']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='benefit_ib_scan']").click()
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
