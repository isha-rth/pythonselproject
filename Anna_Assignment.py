# 1. goto http://annauniv.edu/
# 2. click on "Departments" link
# 3. Goto "Faculty Of Civil Engineering" and click on "Institute for Ocean Management"
# 4. Verify the page title.
# 5. Goto "Research Themes" options and Click "Coastal Pollution Monitoring and Hazards"
# 6. Verify the page title.


import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class AnnaUniversity(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        self.addCleanup(self.browser.quit)

    def testpagetitle(self):
        self.browser.get("http://annauniv.edu/")
        self.browser.maximize_window()
        print(self.browser.current_url)
        dept = self.browser.get("https://www.annauniv.edu/department/index.php")
        wait = WebDriverWait(self.browser, 30)
        menu = self.browser.find_element_by_name("link13")
        time.sleep(3)
        actions = ActionChains(self.browser)
        actions.move_to_element(menu)
        time.sleep(3)
        Element = self.browser.find_elements_by_xpath("//div/a[contains(text(),'Ocean')]")
        actions.click(Element)
        actions.perform()
        Title = self.browser.find_elements_by_xpath("//div/img[@src='images/iomtxt.jpg']")
        if Title == True:
            print("Page is verified")
        else:
            print("Page is not loaded")







                #iom = self.browser.find_element_by_link_text("https://www.annauniv.edu/iom/index.php")
        #wait.until(expected_conditions.element_to_be_clickable())
        #table_link = wait.until(expected_conditions._element_if_visible("https://www.annauniv.edu/iom/index.php"))
        #table_link.click()


