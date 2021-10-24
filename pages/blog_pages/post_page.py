from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PostPage(BasePage):
    def check_post_text(self, text):
        post_text = self.wait_until_visible(PostPageLocators.POST_TEXT)
        assert post_text.text == text, "Неверный текст"


class PostPageLocators:
    POST_TEXT = (By.CSS_SELECTOR, ".container p+p")
