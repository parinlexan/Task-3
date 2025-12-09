from selenium.webdriver.common.by import By


class CommonLocators:
    email_input = By.XPATH, "//*[contains(text(), 'Email')]/following-sibling::input"
    password_input = By.XPATH, "//*[contains(text(), 'Пароль')]/following-sibling::input"
    password_hide_btn = By.XPATH, "//*[contains(@class, '_icon-action')]//*"
    overlay = By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"