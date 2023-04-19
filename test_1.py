from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# def test_open():
#     browser.get("https://suninjuly.github.io/xpath_examples")
#     time.sleep(5)

def open_page():
    browser.get("https://suninjuly.github.io/cats.html")
    bullet_cat = browser.find_element(By.XPATH, "//*[text()='Bullet cat']")
    # time.sleep(5)
    print(bullet_cat.text)

    view_buttons = browser.find_elements(By.XPATH, "//*[text()='View']")
    print(view_buttons)
    assert len(view_buttons) == 6, 'wrong length'


def test_open_page():
    open_page()