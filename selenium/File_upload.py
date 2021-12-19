from  selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Download Text File
driver.find_element_by_id("textbox").send_keys("testdata")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("pdf testdata")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

driver.close()