#Assignment1 (doubleClick)
#Go to - https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick
#double click on "Double-click this paragraph to trigger a function."
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class Doubleclick(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        self.addCleanup(self.browser.quit)

    def testdoubleclick(self):
        self.browser.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")
        self.browser.maximize_window()
        time.sleep(5)
        self.browser.switch_to.frame(self.browser.find_element_by_xpath("//iframe[@id='iframeResult']"))
        #self.browser.find_element_by_xpath("//body[@contenteditable='false']").click()
        message = self.browser.find_element_by_xpath("//body/p[@ondblclick='myFunction()']")
        actions = ActionChains(self.browser)
        actions.double_click(message).perform()
        time.sleep(5)

        #msg = self.assert_(self.browser.find_element_by_id("demo").is_displayed())
        #print(msg)



