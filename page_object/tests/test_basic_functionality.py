import allure

import urls
from page_object.pages.login_page import LoginPage
from page_object.pages.main_page import MainPage


class TestBasicFunctionality:

    @allure.title("Клик по конструктору переводит на главную страницу")
    def test_constructor_btn(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_url(urls.LOGIN_URL)
        main_page = MainPage(driver)
        main_page.click_construct_btn()
        driver.refresh()
        current_url = main_page.check_url()
        assert current_url == urls.BASE_URL

    @allure.title("Клик по ленте заказов переводит на ленту заказов страницу")
    def test_orders_feed_btn(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_orders_feed_btn()
        driver.refresh()
        current_url = main_page.check_url()
        assert current_url == urls.ORDERS_FEED_URL

    @allure.title("Открытие всплывающего окна кликом по ингридиенту и закрытие кликом по крестику")
    def test_popup_btn(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_ingr_btn()
        assert main_page.shown_popup()
        main_page.close_popup()

    @allure.title("Изменение счетчика ингредиентов при добавлении ингредиента")
    def test_counter(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        value1 = main_page.check_value_counter()
        main_page.click_construct_btn()
        main_page.drag_ingr()
        main_page.drag_ingr()
        value2 = main_page.check_value_counter()
        assert value1 != value2

    @allure.title("Оформление заказа после авторизации")
    def test_login_create_order(self, driver, user):
        password, email, access_token = user
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_pers_acc_btn()
        login_page = LoginPage(driver)
        login_page.email_input(email)
        login_page.password_input(password)
        login_page.click_login_btn()
        main_page.click_construct_btn()
        main_page.drag_ingr()
        main_page.submit_order()
        assert main_page.success_check()