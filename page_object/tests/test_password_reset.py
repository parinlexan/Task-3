import allure

import urls
from helpers import *
from page_object.pages.login_page import LoginPage
from page_object.pages.main_page import MainPage
from page_object.pages.password_reset_page import PasswordResetPage


class TestResetPassword:

    @allure.title("Переход на страницу смены пароля по клику на главной странице")
    def test_password_reset_btn(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_pers_acc_btn()
        login_page = LoginPage(driver)
        login_page.click_password_reset_btn()
        driver.refresh()
        current_url = login_page.check_url()
        assert current_url == urls.FORGOT_PASSWORD_URL

    @allure.title("Демонстрация и скрытие пароля")
    def test_password_reset(self, driver):
        email = generate_email()
        reset_page = PasswordResetPage(driver)
        reset_page.go_to_url(urls.FORGOT_PASSWORD_URL)
        reset_page.email_input(email)
        reset_page.reset_password_btn_click()
        reset_page.show_password()
        state1 = reset_page.password_state_get()
        reset_page.hide_password()
        state2 = reset_page.password_state_get()
        assert state2 != state1