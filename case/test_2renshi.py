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
            "xpath=//*[@class='android.widget.LinearLayout' and ./*[@text='人事服务'] and ./*[@id='item_home_icon']]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@text='申请记录']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@text='服务已提交']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='item_06']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='item_07']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='btn_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='item_08']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='item_09']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='service_h1']").click()
        self.driver.swipe(317, 432, 317, -197, 851)
        self.driver.swipe(317, 432, 317, -197, 791)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='service_h2']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
