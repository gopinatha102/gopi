from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()


admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermang=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermang).move_to_element(user).click().perform()