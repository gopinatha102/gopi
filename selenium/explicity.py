from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.expedia.com/")
driver.implicitly_wait(5)
driver.maximize_window()
#by using element
driver.find_element(By.LINK_TEXT,"Flights").click()
driver.find_element(By.LINK_TEXT,"One-way").click()
#source  button finder
driver.find_element(By.XPATH,"//*[@id='location-field-leg1-origin-menu']/div[1]/button").click()
driver.find_element(By.ID,"location-field-leg1-origin").send_keys("SFO")
driver.find_element(By.XPATH,'//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]/button/div/div[1]/span/strong').click()

#destination button finder
driver.find_element(By.XPATH,'//*[@id="location-field-leg1-destination-menu"]/div[1]/button').click()
driver.find_element(By.ID,"location-field-leg1-destination").send_keys("NYC")
driver.find_element(By.XPATH,'//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]/button/div/div[1]/span/strong').click()

#data  enter button
driver.find_element(By.XPATH,'//*[@id="d1-btn"]').click()
driver.find_element(By.XPATH,'//*[@id="wizard-flight-tab-oneway"]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/section/section/button[1]/span').click()
driver.find_element(By.XPATH,'//*[@id="wizard-flight-tab-oneway"]/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[7]/button').click()
driver.find_element(By.XPATH,'//*[@id="wizard-flight-tab-oneway"]/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/button/span').click()
driver.find_element(By.XPATH,'//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()

#Explicity
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stopFilter_stops-0"]')))
element.click()

time.sleep(6)
driver.quit()

