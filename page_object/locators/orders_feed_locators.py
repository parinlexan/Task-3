from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    order = By.XPATH, "//*[contains(@class, 'OrderHistory_link')][1]"
    order_popup = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]"
    all_orders_count = By.XPATH, "//*[contains(text(), 'Выполнено за все время:')]/following-sibling::p"
    today_orders_count = By.XPATH, "//*[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p"
    in_process_order = By.XPATH, "//*[contains(@class, 'orderListReady_')]/*[contains(@class, 'text text_type_digits-default')]"

    @staticmethod
    def order_id(id: str) -> tuple:
        return By.XPATH, f"//*[text()='{id}']"