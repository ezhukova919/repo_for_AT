from base.base_test import BaseTest
import allure
import pytest


@allure.testcase("TBX functionality")
class TestTextBox(BaseTest):
    
    @allure.title("TBX testcase title") #comments in GitHub
    @allure.severity("High")
    # @pytest.mark.smoke
    def test_textbox(self):
        self.text_page.open()
        self.text_page.is_opened()
        self.text_page.textbox_present()
        self.text_page.textbox_clear()
        self.text_page.textbox_input_value()
        self.text_page.submit()


