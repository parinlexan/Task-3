from selenium.webdriver.common.by import By


class PasswordResetPageLocators:
    reset_btn = By.XPATH, "//*[contains(text(), 'Восстановить')]"
    code_input = By.XPATH, "//*[contains(text(), 'Введите код из письма')]"