import allure

from page_object.pages.login_page import LoginPage
from page_object.pages.main_page import MainPage
from page_object.pages.orders_feed_page import OrdersFeedPage
import urls


class TestOrdersFeed:

    @allure.title("Открытие всплывающего окна с деталями заказа в ленте заказов")
    def test_info_popup_orders_feed(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.go_to_url(urls.ORDERS_FEED_URL)
        orders_feed_page.order_click()
        assert orders_feed_page.order_popup_check()

    @allure.title("Заказы пользователя из раздела История заказов отображаются на странице Лента заказов")
    def test_client_orders_in_orders_feed(self, driver, user):
        password, email, name, access_token = user
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
        main_page.close_popup()
        main_page.click_pers_acc_btn()
        login_page.click_history_orders_btn()
        id = login_page.last_order_check_id()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.go_to_url(urls.ORDERS_FEED_URL)
        assert orders_feed_page.order_id_check(id)

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_all_time_counter(self, driver, user):
        password, email, name, access_token = user
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_pers_acc_btn()
        login_page = LoginPage(driver)
        login_page.email_input(email)
        login_page.password_input(password)
        login_page.click_login_btn()
        main_page.click_construct_btn()
        main_page.click_orders_feed_btn()
        orders_feed_page = OrdersFeedPage(driver)
        all_time_counter = orders_feed_page.all_orders_counter_check()
        main_page.click_construct_btn()
        main_page.drag_ingr()
        main_page.submit_order()
        main_page.close_popup()
        main_page.click_orders_feed_btn()
        new_all_time_counter = orders_feed_page.all_orders_counter_check()
        assert all_time_counter < new_all_time_counter

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_all_time_counter(self, driver, user):
        password, email, name, access_token = user
        main_page = MainPage(driver)
        main_page.go_to_url(urls.BASE_URL)
        main_page.click_pers_acc_btn()
        login_page = LoginPage(driver)
        login_page.email_input(email)
        login_page.password_input(password)
        login_page.click_login_btn()
        main_page.click_construct_btn()
        main_page.click_orders_feed_btn()
        orders_feed_page = OrdersFeedPage(driver)
        today_counter = orders_feed_page.today_orders_counter_check()
        main_page.click_construct_btn()
        main_page.drag_ingr()
        main_page.submit_order()
        main_page.close_popup()
        main_page.click_orders_feed_btn()
        new_today_counter = orders_feed_page.today_orders_counter_check()
        assert today_counter < new_today_counter

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_all_time_counter(self, driver, user):
        password, email, name, access_token = user
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
        main_page.close_popup()
        main_page.click_pers_acc_btn()
        login_page.click_history_orders_btn()
        id = login_page.last_order_check_id()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.go_to_url(urls.ORDERS_FEED_URL)
        in_process_orders_counter = orders_feed_page.in_process_orders_counter_check()
        assert f'#{in_process_orders_counter}' == id
