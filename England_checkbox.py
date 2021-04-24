import unittest
import time
from selenium import webdriver

class England(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        self.addCleanup(self.browser.quit)

    def testnichethyselfurl(self):
        self.browser.get("http://selenium-examples.nichethyself.com")
        self.browser.maximize_window()

    def testenglandboxpage(self):
        self.browser.get("http://selenium-examples.nichethyself.com")
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//div/a[contains(text(),'Customized tours')]").click()
        self.browser.refresh()
        print(self.browser.current_url)
        self.browser.implicitly_wait(4)
        england = self.browser.find_element_by_xpath("//div[2][@class='checkbox-inline']/label/input[@type='checkbox']")
        england.click()
        time.sleep(10)
        submit = self.browser.find_element_by_xpath("//*[@id='international']/form/button[@type='submit'][contains(text(),'Submit')]")
        #if submit.is_enabled()==1:
        #    print("England is Checked")
        #else:
        #    print("England is not Checked")

        self.assert_(submit.is_enabled(),)
