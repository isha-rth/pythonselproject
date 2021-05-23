#Assignment3(Most Important Assignment for entire training):
#go to triphobo.com website
#Click "Later" in be updated box (this may not appear, then ignore)
#Click on "PLAN YOUR NEXT VACATION" button on the homepage
#Type Where do you want to go? field, Houston in Texas
#Select Start and End date of your journey
#Click on button "Start Planning"
#Click on "Next - About Your Trip"
#Click on "Skip to About You"
#Click on "Trip Overview"
#Click on "Editable View"
#Drag "Children's museum from day 3 to day 4"
#Click on Save plan -> Finish Planning
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class Triphobo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
        self.addCleanup(self.browser.quit)

    def testjourney(self):
        self.browser.get("triphobo.com")
        self.browser.find_element_by_id("plan-my-trip").click()
        wait = WebDriverWait(self.browser, 30)
        place = wait.until(expected_conditions.visibility_of_element_located(By.XPATH("//div/input[@class='wait = WebDriverWait(self.browser, 30)'")))
        place.click()
        place.sendkeys("Houston in Texas")
        city = wait.until(expected_conditions.visibility_of_element_located(By.XPATH("//div/ul[@class='city-list-collection']")))
        self.browser.find_element_by_xpath("//li/span[contains(text(),'Houston, Texas, United States')]").click()
        


