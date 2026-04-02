def test_example():
    assert 1 + 1 == 2

from selenium import webdriver

def test_google_title():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

import requests

def test_api():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200