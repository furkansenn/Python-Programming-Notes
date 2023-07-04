from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome("C:/Users/Dell User/Desktop/chromedriver.exe")

url="https://sellercentral.amazon.com/hz/fba/profitabilitycalculator/index?lang=en_US"

driver.get(url)
driver.maximize_window()
time.sleep(1)
sign=driver.find_element(By.XPATH, "/html/body/div/div[2]/div/kat-modal/div/kat-button[2]")
sign.click()
time.sleep(1)
sign=driver.find_element(By.XPATH, "/html/body/div/div[2]/div/kat-box/kat-tabs/kat-tab[1]/span")
sign.click()
time.sleep(1)
signsearch=driver.find_element(By.XPATH, "/html/body/div/div[2]/div/kat-box/kat-tabs/kat-tab[1]/div/div[1]/form/kat-input")
signsearch.send_keys("B00004WA8I")
time.sleep(2)
signsearch.send_keys(Keys.ENTER)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ProgramCard"))
    )
    print(element.text)
finally:
    driver.quit()



# try:
#     x=WebDriverWait(driver,1000).until(EC.text_to_be_present_in_element_value((By.XPATH,'/html/body/div/div[2]/div/div[2]/kat-box[1]/div[2]/div[1]')))
#     print(x.text)
# finally:
#     driver.quit()