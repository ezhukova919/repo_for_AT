import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class TextboxPage(BasePage):
    PAGE_URL = Links.TEXTBOX_PAGE

    FULL_NAME_FIELD = ("xpath", "//input[@id='userName']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    @allure.step("Check TBX presence")
    def textbox_present(self):
        self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD))

    @allure.step("Check TBX is clear")
    def textbox_clear(self):
        textbox_field = self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD))
        textbox_field.clear()
        time.sleep(2)

    @allure.step("Check TBX is filled with new value")
    def textbox_input_value(self):
        textbox_field = self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD))
        textbox_field.send_keys("Test_Full_Name")
        assert "Test_Full_Name" in textbox_field.get_attribute(
            "value"
        ), "Incorrect text"

    @allure.step("Click Submit button")
    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        
