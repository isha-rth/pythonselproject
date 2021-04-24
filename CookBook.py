import unittest
from selenium import webdriver

class CookBook(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        self.addCleanup(self.browser.quit)

    def testcookbookurl(self):
        self.browser.get("http://cookbook.seleniumacademy.com/Config.html")
        self.browser.maximize_window()
        print(self.browser.current_url)

    def testparkingcheckbox(self):
        self.browser.get("http://cookbook.seleniumacademy.com/Config.html")
        self.browser.maximize_window()
        parkbox = self.browser.find_element_by_name('parksensor')
        parkbox.is_selected()
        if parkbox.is_enabled() == 1:
            print('Parking Checkbox is enabled')
        else:
            print('Parking checkbox is not enabled')

    def testLEDcheckbox(self):
        self.browser.get("http://cookbook.seleniumacademy.com/Config.html")
        self.browser.maximize_window()
        Ledbox = self.browser.find_element_by_name("ledheadlamp")
        Ledbox.is_selected()
        if Ledbox.is_enabled() == 1:
            print("LedBox is enabled")
        else:
            print("LedBox is not enabled")