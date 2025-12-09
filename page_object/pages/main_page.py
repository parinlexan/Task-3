import allure
import pytest
from selenium.webdriver import ActionChains

from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликаем по кнопке 'Личный кабинет'")
    def click_pers_acc_btn(self):
        self.find_element_with_wait(MainPageLocators.personal_account_btn)
        self.click_element(MainPageLocators.personal_account_btn)

    @allure.step("Кликаем по кнопке 'Конструктор'")
    def click_construct_btn(self):
        self.find_element_with_wait(MainPageLocators.constructor_btn)
        self.click_element(MainPageLocators.constructor_btn)

    @allure.step("Кликаем по кнопке 'Лента Заказов'")
    def click_orders_feed_btn(self):
        self.find_element_with_wait(MainPageLocators.orders_feed_btn)
        self.click_element(MainPageLocators.orders_feed_btn)

    @allure.step("Кликаем ингредиенту")
    def click_ingr_btn(self):
        self.find_element_with_wait(MainPageLocators.burger_ing_icon)
        self.click_element(MainPageLocators.burger_ing_icon)

    @allure.step("Проверяем открытие всплывающего окна")
    def shown_popup(self):
        return self.find_element_with_wait(MainPageLocators.popup).is_displayed()

    @allure.step("Закрываем всплывающее окно")
    def close_popup(self):
        self.find_element_with_wait(MainPageLocators.popup_close_btn)
        self.click_element(MainPageLocators.popup_close_btn)
        self.find_element_with_wait(MainPageLocators.order_number)
        number = self.find_element_with_wait(MainPageLocators.order_number).text
        if number == "9999":
            pytest.skip("Номер заказа 9999 - некорректный номер")


    @allure.step("Перетаскиваем ингредиенты в заказ")
    def drag_ingr(self):
        bun_element = self.find_element_with_wait(MainPageLocators.bun)
        basket_element = self.find_element_with_wait(MainPageLocators.ingr_basket)
        if self.driver.name == 'firefox':
            script = """
                    var dragStart = new DragEvent('dragstart', { bubbles: true });
                    var drop = new DragEvent('drop', { bubbles: true });
                    var dragEnd = new DragEvent('dragend', { bubbles: true });
                    arguments[0].dispatchEvent(dragStart);
                    arguments[1].dispatchEvent(drop);
                    arguments[0].dispatchEvent(dragEnd);
                    """
            self.driver.execute_script(script, bun_element, basket_element)
        else:
            self.drag_and_drop_element(MainPageLocators.bun, MainPageLocators.ingr_basket)

    @allure.step("Проверяем счетчик")
    def check_value_counter(self):
        counter = self.find_element_with_wait(MainPageLocators.counter).text
        return counter

    @allure.step("Создаем заказ")
    def submit_order(self):
        self.find_element_with_wait(MainPageLocators.create_order_btn)
        self.click_element(MainPageLocators.create_order_btn)

    @allure.step("Проверяем, что заказ успешно создан")
    def success_check(self):
        self.find_element_with_wait(MainPageLocators.success_message)
        return self.find_element_with_wait(MainPageLocators.success_message).is_displayed()