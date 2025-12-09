import allure

from page_object.locators.password_reset_locators import PasswordResetPageLocators
from page_object.pages.base_page import BasePage


class PasswordResetPage(BasePage):

    @allure.step("Нажимаем 'Восстановить'")
    def reset_password_btn_click(self):
        self.find_element_with_wait(PasswordResetPageLocators.reset_btn)
        self.click_element(PasswordResetPageLocators.reset_btn)