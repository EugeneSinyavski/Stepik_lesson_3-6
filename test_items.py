from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_see_button_add_to_basket(browser):
    try:
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    except NoSuchElementException:
        assert False, "Button is not presented"
