import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def setup():
    service_obj = Service(".\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    return driver

