from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:/Users/Dell User/Desktop/chromedriver.exe")

url="https://sellercentral.amazon.com/hz/fba/profitabilitycalculator/index?lang=en_US"

driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
sign=driver.find_element(By.XPATH, "/html/body/div/div[2]/div/kat-modal/div/kat-button[2]")
sign.click()
sign=driver.find_element(By.XPATH, "/html/body/div/div[2]/div/kat-box/kat-tabs/kat-tab[1]/span")
sign.click()
signsearch=driver.find_element(By.XPATH, "/html/body/div/div[2]/div/kat-box/kat-tabs/kat-tab[1]/div/div[1]/form/kat-input")
signsearch.send_keys("B00004WA8I")
signsearch.send_keys(Keys.ENTER)

