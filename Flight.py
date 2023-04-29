from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.irctc.co.in/")

driver.find_element(By.XPATH,"//a[@aria-label='Menu Flight. Website will be opened in new tab']").click()

First_Win = driver.window_handles[1]
driver.switch_to.window(First_Win)

driver.find_element(By.XPATH,"//*[@id='carouselExampleInterval']/div[1]/div/div/div[1]/div[1]/div[2]/label").click()
driver.find_element(By.XPATH,"//input[@id='stationFrom']").send_keys("del")

from_origine= driver.find_element(By.XPATH,"//ul[@id='ui-id-1']/li/div").click()

driver.find_element(By.XPATH,'//input[@id="stationTo"]').click()
driver.find_element(By.NAME,"To").send_keys("bom")

From_origine= driver.find_element(By.XPATH,"//ul[@id='ui-id-2']").click()

OrigineDate= driver.find_element(By.ID,"originDate").click()

OrigineDate= driver.find_element(By.XPATH,"//*[@id='carouselExampleInterval']/div[1]/div/div/div[2]/form/div[3]/datepickermodifi/div/div[2]/div[1]/table/tr[5]/td/span[1]").click()

OrigineDate = driver.find_element(By.XPATH,"//*[@id='carouselExampleInterval']/div[1]/div/div/div[2]/form/div[3]/datepickermodifi/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/span").click()


Return= driver.find_element(By.XPATH,"//*[@id='returnDate']").click()
Return= driver.find_element(By.XPATH,"//*[@id='carouselExampleInterval']/div[1]/div/div/div[2]/form/div[4]/datepickermodifi/div/div[2]/div[1]/table/tr[6]/td/span[1]").click()

Return= driver.find_element(By.XPATH,"//*[@id='carouselExampleInterval']/div[1]/div/div/div[2]/form/div[4]/datepickermodifi/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/span").click()
driver.find_element(By.ID,"noOfpaxEtc").click()
driver.find_element(By.XPATH,"//*[@id='TravellerEconomydropdown']/div[1]/div[1]/div/a[2]/i").click()
driver.find_element(By.XPATH,"//*[@id='noOfpaxEtc']").click()
driver.find_element(By.XPATH,"//*[@id='carouselExampleInterval']/div[1]/div/div/div[2]/form/div[6]/button").click()
time.sleep(15)
driver.close()
