from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver= webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe", chrome_options=chrome_options)

driver.maximize_window()
driver.get("https://www.1mg.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='srchBarShwInfo']").send_keys("whey")
time.sleep(180)