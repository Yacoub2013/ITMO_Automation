from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
suarech_username = driver.find_element(By.CSS_SELECTOR, '#user-name').accessible_name
suarech_username_1="Username"


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
suarech_password = driver.find_element(By.CSS_SELECTOR, '#password').accessible_name
suarech_password_1="Password"


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
suarech_submit = driver.find_element(By.CSS_SELECTOR, '#login-button').accessible_name
suarech_supmit_1="Login"


if suarech_username ==  suarech_username_1 and  suarech_password ==  suarech_password_1 and  suarech_submit ==  suarech_supmit_1:
    print("Элементы найдены")