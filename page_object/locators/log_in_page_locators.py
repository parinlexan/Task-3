from selenium.webdriver.common.by import By


class LogInPageLocators:
    log_in_btn = By.XPATH, "//*[contains(text(), 'Войти')]"
    password_reset_btn = By.XPATH, "//*[contains(text(), 'Восстановить пароль')]"
    orders_history_btn = By.XPATH, "//*[contains(text(), 'История заказов')]"
    logout_btn = By.XPATH, "//*[contains(text(), 'Выход')]"
    account_btn = By.XPATH, "//*[contains(text(), 'Профиль')]"
    last_order_id = By.XPATH, "//*[contains(@class, 'OrderHistory_profileList')]//*[contains(@class, 'OrderHistory_textBox')]/p[1]"