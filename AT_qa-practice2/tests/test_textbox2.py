import allure
import pytest
from pages.textbox_page import TextboxPage


def test_textbox(driver):
    test_page = TextboxPage(
        driver
    )  # в этой строке указываем для test_page куда ей обращаться
    test_page.open()  # -> class (TextboxPage) в соответсвующем _page.py файле
    test_page.is_opened()
    test_page.textbox_present()
    test_page.textbox_clear()
    test_page.textbox_input_value()
    test_page.submit()
