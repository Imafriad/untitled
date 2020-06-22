import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class test_wuxianyijin(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'test_wuxianyijin'
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

    def testtest_wuxianyijin(self):
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='item_home_icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='五险一金']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='社会保险']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("xpath=//*[@id='socialSecurity_rightBtn']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='socialSecurity_leftBtn']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='查看明细']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='变更记录']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_right']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='numberpicker_input' and (./preceding-sibling::* | ./following-sibling::*)[@text='2018']]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='numberpicker_input' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[@text='2018']]] and (./preceding-sibling::* | ./following-sibling::*)[@text='5']]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='numberpicker_input' and (./preceding-sibling::* | ./following-sibling::*)[@text='2018']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='2018']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@text='2019' and (./preceding-sibling::* | ./following-sibling::*)[@text='2017']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='2020' and @class='android.widget.Button']").click()
        self.driver.find_element_by_xpath(
            "xpath=((//*[@class='android.widget.LinearLayout' and ./parent::*[@class='android.widget.LinearLayout' and ./parent::*[@id='content']]]/*[@class='android.widget.LinearLayout'])[2]/*/*/*/*[@text='2021'])[2]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@text='7' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[@text='2022']]]]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='8']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='确认']").click()
        time.sleep(1)
        self.driver.swipe(595, 560, 595, 93, 709)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='公积金']").click()
        time.sleep(1)
        self.driver.swipe(773, 380, 773, 193, 681)
        self.driver.find_element_by_xpath("xpath=//*[@text='变更记录']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='个人账号']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='btn_left']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
