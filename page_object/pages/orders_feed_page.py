import allure

from page_object.locators.orders_feed_locators import OrdersFeedLocators
from page_object.pages.base_page import BasePage


class OrdersFeedPage(BasePage):

    @allure.step("Нажимаем на заказ")
    def order_click(self):
        self.find_element_with_wait(OrdersFeedLocators.order)
        self.click_element(OrdersFeedLocators.order)

    @allure.step("Проверяем открыие всплывающего окна")
    def order_popup_check(self):
        self.find_element_with_wait(OrdersFeedLocators.order_popup)
        return self.find_element_with_wait(OrdersFeedLocators.order_popup).is_displayed()

    @allure.step("Проверяем наличие заказа с определенным id в ленте заказов")
    def order_id_check(self, id):
        self.find_element_with_wait(OrdersFeedLocators.order_id(id))
        return self.find_element_with_wait(OrdersFeedLocators.order_id(id)).is_displayed()

    @allure.step("Проверяем значение счетчика заказов за все время")
    def all_orders_counter_check(self):
        self.find_element_with_wait(OrdersFeedLocators.all_orders_count)
        all_orders_count = self.find_element_with_wait(OrdersFeedLocators.all_orders_count).text
        return all_orders_count

    @allure.step("Проверяем значение счетчика заказов за сегодня")
    def today_orders_counter_check(self):
        self.find_element_with_wait(OrdersFeedLocators.today_orders_count)
        today_orders_count = self.find_element_with_wait(OrdersFeedLocators.today_orders_count).text
        return today_orders_count

    @allure.step("Проверяем значение списка заказов в работе")
    def in_process_orders_counter_check(self):
        self.find_element_with_wait(OrdersFeedLocators.in_process_order)
        in_process_orders_count = self.find_element_with_wait(OrdersFeedLocators.in_process_order).text
        return in_process_orders_count