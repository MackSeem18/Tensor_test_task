from selenium.common import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from error_messages import ErrorMessages as Em
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def wait_until_presented(self, locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_until_clickable(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element_to_scroll = self.browser.find_element(*locator)
        ActionChains(self.browser) \
            .scroll_to_element(element_to_scroll) \
            .perform()

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, locator):
        try:
            self.wait_until_presented(locator)
            self.wait_until_clickable(locator)
            self.browser.find_element(*locator).click()
        except (ElementClickInterceptedException, NoSuchElementException, TimeoutException):
            return False
        return True

    def point_and_click_element(self, locator):
        try:
            self.wait_until_presented(locator)
            self.wait_until_clickable(locator)
            element = self.browser.find_element(*locator)
            ActionChains(self.browser) \
                .move_to_element(element) \
                .click() \
                .perform()
        except (ElementClickInterceptedException, NoSuchElementException, TimeoutException):
            return False
        return True

    def is_element_visible(self, locator):
        try:
            is_visible = self.browser.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False
        return is_visible

    def should_be_expected_url(self, expected_url):
        actual_url = self.browser.current_url
        assert actual_url == expected_url, \
            Em.wrong_url(expected_url, actual_url)


