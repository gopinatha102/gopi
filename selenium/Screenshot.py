from selenium import webdriver

driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
path=r"D:\selenium class\Homepage1.png"
path1=r"D:\selenium class\Homepage1.jpg"
driver.save_screenshot(path)
driver.get_screenshot_as_file(path1)