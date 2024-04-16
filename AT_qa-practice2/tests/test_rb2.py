# from base.base_test import BaseTest
import allure
import pytest
from pages.radiobutton_page import RbPage

# @allure.testcase("RB functionality")
# class TestRB(driver):

#     @allure.title("RB testcase title")
#     @allure.severity("High")
    # @pytest.mark.smoke
def test_rb(driver):
        test_page = RbPage(driver)  # в этой строке указываем для test_page куда ей обращаться 
        test_page.open()            # -> class (RbPage) в соответсвующем _page.py файле
        test_page.is_opened()
        test_page.rb_present()
        test_page.rb_is_selected()
        test_page.success_msg()



