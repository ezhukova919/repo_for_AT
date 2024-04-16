import pytest
from pages.radiobutton_page import RbPage
from pages.textbox_page import TextboxPage


class BaseTest:

    rb_page : RbPage
    text_page : TextboxPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.rb_page = RbPage(driver)
        request.cls.text_page = TextboxPage(driver)
