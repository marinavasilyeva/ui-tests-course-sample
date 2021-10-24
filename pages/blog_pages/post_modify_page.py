from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PostModifyPage(BasePage):
    def add_title(self, title):
        self.wait_until_clickable(PostPageLocators.TITLE_FIELD).send_keys(title)

    def add_text(self, text):
        self.wait_until_clickable(PostPageLocators.TEXT_FIELD).send_keys(text)

    def add_tags(self, tags):
        self.wait_until_clickable(PostPageLocators.TAGS_FIELD).send_keys(tags)

    def click_submit_button(self):
        self.wait_until_clickable(PostPageLocators.SUBMIT_BUTTON).click()


class PostPageLocators:
    TITLE_FIELD = (By.ID, "title")
    TEXT_FIELD = (By.ID, "text")
    TAGS_FIELD = (By.ID, "tags")
    SUBMIT_BUTTON = (By.ID, "submit")