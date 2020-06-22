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
        self.driver.find_element_by_xpath("xpath=//*[@text='医疗理赔']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='在线理赔']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='确定']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='确 定']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='apply_step_2_bill_pic']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='从相册中选择']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='始终允许']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@text='始终允许']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='图片']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon_thumb' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@text='MagazineUnlock']]]]]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon_thumb' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@text='magazine-unlock-05-2.3.1862-E81564819691D4E65D2C8AEA1AED3154.jpg']]]]]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='apply_step_detailed_list']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='从相册中选择']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='最近']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon_thumb' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@text='Screenshot_20200305-155031.png']]]]]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='请选择日期']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='month_pv']").click()
        self.driver.swipe(544, 1435, 511, 1624, 844)
        self.driver.swipe(835, 1340, 828, 1602, 1035)
        self.driver.find_element_by_xpath("xpath=//*[@text='确认']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='apply_step_2_bill_et']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.view.View' and ./parent::*[./parent::*[@id='inputArea']]]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.view.View' and ./parent::*[./parent::*[@id='inputArea']]]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.view.View' and ./parent::*[./parent::*[@id='inputArea']]]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.view.View' and ./parent::*[./parent::*[@id='inputArea']]]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='提 交']").click()


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
