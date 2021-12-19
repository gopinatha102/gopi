from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/radio.html")

#Number of radio buttons
number=driver.find_elements(By.NAME,"webform")
print(len(number))

#statues of radio buttons
print("----------------radiobutton---------------------")
statues=driver.find_element(By.ID,"vfb-7-1").is_selected()
print(statues)
driver.find_element(By.ID,"vfb-7-1").click()
statues=driver.find_element(By.ID,"vfb-7-1").is_selected()
print(statues)
#statues of cheeck boxs
print("---------------cheeckButton---------------------")
statues=driver.find_element(By.ID,"vfb-6-0").is_selected()
print(statues)
driver.find_element(By.ID,"vfb-6-0").click()
statues=driver.find_element(By.ID,"vfb-6-0").is_selected()
print(statues)