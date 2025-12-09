import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TIMEOUT
from page_object.locators.common_locators import CommonLocators


class BasePage:

    def __init__(self, driver):
        self.actions = ActionChains(driver)
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step("Открываем ссылку")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Проверяем ссылку")
    def check_url(self):
        return self.driver.current_url

    @allure.step("Ищем элемент с ожиданием")
    def find_element_with_wait(self, locator, timeout=TIMEOUT):
        self.wait.until(
            expected_conditions.presence_of_element_located(locator)
        )
        self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Нажимаем на элемент")
    def click_element(self, locator, timeout=TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element(CommonLocators.overlay))
        except TimeoutException:
            pass
        except:
            pass

        self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator)).click()

    @allure.step("Вводим текст в поле")
    def add_text(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получаем значение в поле")
    def get_value(self, locator):
        return self.find_element_with_wait(locator).get_attribute("value")

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)
        self.actions.drag_and_drop(source, target).perform()

    @allure.step("Открываем пароль")
    def show_password(self):
        self.find_element_with_wait(CommonLocators.password_hide_btn).click()

    @allure.step("Скрываем пароль")
    def hide_password(self):
        self.find_element_with_wait(CommonLocators.password_hide_btn).click()

    @allure.step("Вводим почту и проверяем содержимое поля")
    def email_input(self, email):
        self.find_element_with_wait(CommonLocators.email_input).send_keys(email)
        value = self.get_value(CommonLocators.email_input)
        assert value == email

    @allure.step("Вводим пароль и проверяем содержимое поля")
    def password_input(self, password):
        self.find_element_with_wait(CommonLocators.password_input).send_keys(password)
        value = self.get_value(CommonLocators.password_input)
        assert value == password

    @allure.step("Получаем состояние поля пароль")
    def password_state_get(self):
        password_input = self.find_element_with_wait(CommonLocators.password_input).get_attribute("type")
        return password_input