
from selenium import webdriver

driver = webdriver.Chrome(executable_path="../ChromePackage/chromedriver.exe")
driver.maximize_window()
driver.get("http://google.com")


