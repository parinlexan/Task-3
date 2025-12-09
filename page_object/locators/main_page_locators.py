from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_account_btn = By.XPATH, "//*[contains(text(),'Личный Кабинет')]"
    orders_feed_btn = By.XPATH, "//*[contains(text(), 'Лента Заказов')]"
    constructor_btn = By.XPATH, "//p[text()='Конструктор']"
    log_in_btn = By.XPATH, "//*[contains(text(), 'Войти в аккаунт')]"
    buns_btn = By.XPATH, "//span[contains(text(), 'Булки')]"
    souces_btn = By.XPATH, "//span[contains(text(), 'Соусы')]"
    fillings_btn = By.XPATH, "//span[contains(text(), 'Начинки')]"
    burger_ing_icon = By.XPATH, "//*[contains(@class, '_ingredient_')]"
    popup = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]"
    popup_close_btn = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//*[contains(@class, 'Modal_modal__close')]"
    ingr_order = By.XPATH, "//span[@class = 'constructor-element__row']"
    counter = By.XPATH, "//p[contains(@class, 'counter_counter__num')]"
    ingr_name = By.XPATH, "//*[text() = 'Флюоресцентная булка R2-D3']"
    create_order_btn = By.XPATH, "//button[text() = 'Оформить заказ']"
    success_message = By.XPATH, "//*[text() ='Ваш заказ начали готовить']"
    order_number = By.XPATH, "//*[contains(@class, 'Modal_modal__title')]"