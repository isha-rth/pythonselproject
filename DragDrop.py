import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test(unittest.TestCase):
    def test_drag_and_drop(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        #driver.implicitly_wait(10)
        self.browser.maximize_window()
        self.browser.get("http://www.cookbook.seleniumacademy.com/DragDropDemo.html")

        # find the element
        draggable = self.browser.find_element_by_id("draggable")
        droppable = self.browser.find_element_by_id("droppable")
        #Create the object for Action Chains
        actions = ActionChains(self.browser)
        actions.drag_and_drop(draggable,droppable)
        # perform the operation on the element
        actions.perform()
        self.assertEquals("Dropped!", droppable.text)
        time.sleep(5)

    def test_double_click(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        #driver.implicitly_wait(10)
        self.browser.maximize_window()
        self.browser.get("http://www.cookbook.seleniumacademy.com/DoubleClickDemo.html")
        message = self.browser.find_element_by_id("message")
        # verify blue color
        self.assertEquals("rgba(0, 0, 255, 1)",message.value_of_css_property("background-color"))
        actions = ActionChains(self.browser)
        actions.double_click(message).perform()
        time.sleep(5)
        self.assertEquals("rgba(255, 255, 0, 1)", message.value_of_css_property("background-color"))


if __name__ == "__main__":
    unittest.main()