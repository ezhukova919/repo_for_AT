import time
import allure
from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RbPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = Links.RB_PAGE

    YES_RADIO_TO_CLICK = ("xpath", "//label[@for='yesRadio']")
    YES_RADIO_SELECTED = ("xpath", "//input[@id='yesRadio']")
    SELECTION_OPTION = ("xpath", "//span[@class='text-success']")

    @allure.step("Check RB presence")
    def rb_present(self):
        radio_selection = self.wait.until(EC.element_to_be_clickable(self.YES_RADIO_TO_CLICK))
        
        time.sleep(2)

    @allure.step("Check RB selection")
    def rb_is_selected(self):
        radio_selection = self.wait.until(EC.element_to_be_clickable(self.YES_RADIO_TO_CLICK)) 
        radio_selection.click()
        # selection_done = self.wait.until(EC.element_to_be_selected(self.YES_RADIO_SELECTED))
        # assert selection_done.__getattribute__ is True, "Yes is not selected"

    @allure.step("Check value in message")
    def success_msg(self):
        selection_value = self.wait.until(EC.text_to_be_present_in_element(self.SELECTION_OPTION, "Yes"))
        # assert self.SELECTION_OPTION.text == (text, "Yes") , "Incorrect selection"
        # assert full_name_field.get_attribute("value") == "Full test name", "Incorrect Fuul name"
        # assert "Yes" in selection_value.__getattribute__("value"), "Incorrect selection"