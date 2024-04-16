from base.base_test import BaseTest
import allure
import pytest

@allure.testcase("RB functionality")
class TestRB(BaseTest):


    @allure.title("RB testcase title") #comments
    @allure.severity("High")
    # @pytest.mark.smoke
    def test_rb(self):
        self.rb_page.open()
        self.rb_page.is_opened()
        self.rb_page.rb_present()
        self.rb_page.rb_is_selected()
        self.rb_page.success_msg()



