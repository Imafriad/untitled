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
        self.driver.find_element_by_xpath("xpath=//*[@id='url_iv_head']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='item_home_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='薪酬服务']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='item_home_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='五险一金']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='item_home_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='人事服务']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='item_06']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.LinearLayout' and @width>0 and ./*[@id='item_home_icon'] and ./*[@text='各类活动']]").click()
        self.driver.swipe(477, 415, 477, -740, 932)
        self.driver.swipe(477, 415, 477, -530, 1224)
        self.driver.swipe(477, 415, 480, -1582, 1618)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='url_iv_head']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
