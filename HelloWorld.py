import unittest
import time
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        self.addCleanup(self.browser.quit)

    def testelementpresent(self):
        self.browser.get("http://the-internet.herokuapp.com/dynamic_loading/1")
        self.browser.maximize_window()
        print(self.browser.current_url)
        start = self.browser.find_element_by_id('start')
        start.is_displayed()
        if start.is_displayed()==1 :
            print('Start is Present')
        else :
            print('Start is not available')
        finish = self.browser.find_element_by_id('finish')
        finish.is_displayed()
        if finish.is_displayed() ==1:
            print('Finish is present')
        else :
            print('Finsih is not available')

    def testHelloMessage(self):
        self.browser.get("http://the-internet.herokuapp.com/dynamic_loading/1")
        self.browser.find_element_by_xpath("//div[@id='start']/button").click()
        time.sleep(6)
        Message = self.browser.find_element_by_xpath("//div[@id='finish']/h4[contains(text(),'Hello World!')]")
        #Message.is_displayed()
        #if Message.is_displayed()== 1:
        #    print('Hello World')

        self.assert_(Message.is_displayed())

        # test








