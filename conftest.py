import random

import pytest
from selenium.webdriver import Chrome

from constants import Links


@pytest.fixture()
def browser():
    """Фикстура для открытия браузера перед тестом и закрытия после теста"""
    browser = Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def url(request):
    """Фикстура для получения заданного из командной строки окружения. Возвращает URL окружения"""
    env = request.config.getoption("--env")
    url = Links.base_url.get(env)
    if not url:
        raise Exception("Передано неверное окружение")
    return url


def pytest_configure(config):
    """Хук для регистрации кастомных маркеров"""
    config.addinivalue_line(
        "markers", "auth: tests for auth testing"
    )
    config.addinivalue_line(
        "markers", "smoke: tests for smoke testing"
    )


def pytest_addoption(parser):
    """Хук для регистрации кастомных опций для запуска pytest"""
    parser.addoption("--env", default="prod")


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    """Фикстура для генерации более уникальных значений для faker"""
    return random.randint(0, 9999)
