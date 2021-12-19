
"""
from functools import *
a=(1,2,3,4)
b=(1,2,3)
c=(1,2)
ans=reduce(lambda x,y:x*y,(*a,*b,*c))
#l1=list(map(poduct,a))
print(l1)

print(ans)
a=10
a,b=b,a

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\selenium\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//*[@id='u_0_2_HD']/font/font").click()

"""









































