from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, '#user-name')
        driver.find_element(By.CSS_SELECTOR, '#password')
        driver.find_element(By.CSS_SELECTOR, '#login-button')
    except NoSuchElementException:
        print('Элементы не найдены')
        assert False
    assert True
    print('Элементы найдены')


