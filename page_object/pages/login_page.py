import allure

from page_object.locators.log_in_page_locators import LogInPageLocators
from page_object.pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Нажимаем на кнопку 'Восстановить пароль'")
    def click_password_reset_btn(self):
       self.find_element_with_wait(LogInPageLocators.password_reset_btn)
       self.click_element(LogInPageLocators.password_reset_btn)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login_btn(self):
        self.find_element_with_wait(LogInPageLocators.log_in_btn)
        self.click_element(LogInPageLocators.log_in_btn)

    @allure.step("Переходим в Историю заказов")
    def click_history_orders_btn(self):
        self.find_element_with_wait(LogInPageLocators.orders_history_btn)
        self.click_element(LogInPageLocators.orders_history_btn)

    @allure.step("Проверяем id последнего заказа")
    def last_order_check_id(self):
        self.find_element_with_wait(LogInPageLocators.last_order_id)
        id = self.find_element_with_wait(LogInPageLocators.last_order_id).text
        return id

    @allure.step("Выходим из аккаунта")
    def click_logout_btn(self):
        self.find_element_with_wait(LogInPageLocators.logout_btn)
        self.click_element(LogInPageLocators.logout_btn)