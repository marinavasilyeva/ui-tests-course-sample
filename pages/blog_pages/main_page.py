from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы с главной страницей блога (/blog)
class MainPage(BasePage):
    def click_on_post_title(self, title):
        post_title = MainPageLocators.POST_TITLE.replace("title", title)
        self.wait_until_clickable((By.XPATH, post_title)).click()

    def click_create_post_button(self):
        self.wait_until_clickable(MainPageLocators.CREATE_POST_BUTTON).click()

    def check_post_created_successfully_message(self):
        assert "Blog posted successfully!" in self.wait_until_visible(
            MainPageLocators.CREATE_POST_SUCCESS_MESSAGE).text, \
            "Не отобразилось сообщение об успехе"

    def check_post_exists(self, title):
        post_title = MainPageLocators.POST_TITLE.replace("title", title)
        assert self.wait_until_visible((By.XPATH, post_title)), "Пост не опубликовался"


class MainPageLocators:
    POST_TITLE = '//h1[text()="title"]'
    CREATE_POST_BUTTON = (By.ID, "new")
    CREATE_POST_SUCCESS_MESSAGE = (By.ID, "alert_div")
    FIRST_POST_TITLE = (By.TAG_NAME, "h1")
