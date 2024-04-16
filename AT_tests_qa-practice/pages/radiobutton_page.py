import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RbPage(BasePage):
    PAGE_URL = Links.RB_PAGE

    YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")
    YES_RADIO_SELECTION = ("xpath", "//input[@id='yesRadio']")
    SELECTION_OPTION = ("xpath", "//span[@class='text-success']")

    @allure.step("Check RB presence")
    def rb_present(self):
        radio_selection = self.wait.until(EC.element_to_be_clickable(self.YES_RADIO_LABEL))
        
        time.sleep(2)

    @allure.step("Check RB selection")
    def rb_is_selected(self):
        radio_selection = self.wait.until(EC.element_to_be_clickable(self.YES_RADIO_LABEL)) 
        radio_selection.click()
        # assert radio_selection.is_selected() is True, "Yes is not selected"

    @allure.step("Check value in message")
    def success_msg(self):
        selection_value = self.wait.until(EC.text_to_be_present_in_element(self.SELECTION_OPTION, "Yes"))
        # assert selection_value.get_attribute("value") == "Yes", "Incorrect selection"
