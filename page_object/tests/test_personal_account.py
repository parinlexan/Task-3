import allure

import urls
from page_object.pages.login_page import LoginPage
from page_object.pages.main_page import MainPage


class TestPersonalAccount:

    @allure.title("Переход с главной страницы в раздел авторизации")
    def test_personal_account_main_page_btn(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_pers_acc_btn()
        current_url = main_page.check_url()
        assert current_url == urls.LOGIN_URL

    @allure.title("Авторизация и переход в Историю заказов")
    def test_personal_account_order_history_btn(self, driver, user):
        password, email, name, access_token = user
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_pers_acc_btn()
        login_page = LoginPage(driver)
        login_page.email_input(email)
        login_page.password_input(password)
        login_page.click_login_btn()
        main_page.click_pers_acc_btn()
        login_page.click_history_orders_btn()
        driver.refresh()
        current_url = login_page.check_url()
        assert current_url == urls.ORDERS_HISTORY_URL

    @allure.title("Выход из аккаунта и открытие формы авторизации")
    def test_personal_account_logout_btn(self, driver, user):
        password, email, name, access_token = user
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_pers_acc_btn()
        login_page = LoginPage(driver)
        login_page.email_input(email)
        login_page.password_input(password)
        login_page.click_login_btn()
        main_page.click_pers_acc_btn()
        login_page.click_logout_btn()
        login_page.link_change(driver, urls.LOGIN_URL)
        current_url = login_page.check_url()
        assert current_url == urls.LOGIN_URL