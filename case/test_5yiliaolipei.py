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
            "xpath=//*[@class='android.widget.LinearLayout' and ./*[@id='item_home_icon'] and ./*[@text='医疗理赔']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='claims3']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='确定']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='tv_claim_name']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='本人']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='医药费理赔']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='确 定']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='apply_step_2_bill_pic']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='从相册中选择']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='图片']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon_thumb' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@text='clip']]]]]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon_thumb' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@text='20160623153548421.jpg']]]]]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='请选择日期']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='month_pv']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='month_pv']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='month_pv']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='month_pv']").click()
        self.driver.swipe(540, 1413, 562, 1584, 640)
        self.driver.swipe(784, 1395, 835, 1586, 465)
        self.driver.find_element_by_xpath("xpath=//*[@text='确认']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='apply_step_2_bill_et']").send_keys('10000')
        ##self.driver.find_element_by_xpath(
        ##  "xpath=//*[@class='android.view.View' and ./parent::*[./parent::*[./parent::*[@id='candidatesArea']]]]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.ImageView' and ./parent::*[@id='apply_step_detailed_list']]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@text='从相册中选择']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='图片']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon_thumb' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@text='MagazineUnlock']]]]]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon_thumb' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[./*[./*[@text='magazine-unlock-05-2.3.1862-E81564819691D4E65D2C8AEA1AED3154.jpg']]]]]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@text='提 交']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("xpath=//*[@text='确定']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='claims1']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_right']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@text='确定']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@text='取 消']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.RelativeLayout' and ./*[@id='item_cliaims_top' and ./*[@text='3.00']]]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='claims2']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='claims4']").click()
        time.sleep(1)
        self.driver.swipe(953, 868, 953, 495, 800)
        time.sleep(1)
        self.driver.swipe(953, 868, 953, -11357, 9471)
        time.sleep(1)
        self.driver.swipe(953, 868, 953, 402, 837)
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='icon_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='claims5']").click()
        time.sleep(1)
        self.driver.swipe(924, 866, 924, 400, 704)
        time.sleep(1)
        self.driver.swipe(924, 866, 924, -66, 1342)
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='btn_left']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("xpath=//*[@id='btn_left']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
