from selenium import webdriver
from selenium.webdriver.common.by import By   # тип локатора
from selenium.common.exceptions import NoSuchElementException  #блок ошибок

def test_site_visit(): # есть ли элемент?
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    try:
        driver.find_element(By.CSS_SELECTOR, 'header > a > img')
    except NoSuchElementException:
        assert False
    assert True

