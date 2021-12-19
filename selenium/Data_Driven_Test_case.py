from selenium import webdriver
import Xlutile

driver=webdriver.Chrome(executable_path=r"C:\Users\DELL\PycharmProjects\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

path=r"D:\selenium class\Login1.xlsx"
rows=Xlutile.getRowcount(path,"Sheet1")
print(rows)

for r in range(3,rows+1):
    UserName=Xlutile.readData(path,"Sheet1",r,1)
    PassWord=Xlutile.readData(path,"Sheet1",r,2)

    driver.find_element_by_name("userName").send_keys(UserName)
    driver.find_element_by_name("password").send_keys(PassWord)
    driver.find_element_by_name("submit").click()

    if driver.title=='Login: Mercury Tours':
        print("Given Test Case is Passed")
        Xlutile.writeData(path,'Sheet1',r,3,"Test passed")
    else:
        print("Given Test case is failed")
        Xlutile.writeData(path,'Sheet1',r,3,"Test failed")

    driver.find_element_by_link_text("Home").click()
