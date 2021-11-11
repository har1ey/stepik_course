from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
selector = "#add_to_basket_form > button"


def test_check_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    elm = browser.find_elements(By.CSS_SELECTOR, f'{selector}')
    assert len(elm) == 1, f"Element with '{selector}' selector - not found or found more 1"
