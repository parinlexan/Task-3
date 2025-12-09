import pytest
from selenium import webdriver

from helpers import *


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    browser = None
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920x1080")
        browser = webdriver.Firefox(options=options)
    elif request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920x1080")
        browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(50)
    yield browser
    if browser is not None:
        browser.quit()

@pytest.fixture
def user():
    email = generate_email()
    password = generate_password()
    name = generate_name()
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }
    response_created = create_user(payload)
    access_token = response_created.json().get("accessToken")

    yield password, email, name, access_token

    delete_response = delete_user(access_token)
    assert delete_response.status_code == 202