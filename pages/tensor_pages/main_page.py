from pages.base_page import BasePage
from pages.tensor_pages.locators import MainPageLocators
from error_messages import ErrorMessages as Em


class TensorMainPage(BasePage):
    def should_be_power_in_people_block(self):
        assert self.is_element_present(MainPageLocators.POWER_IN_PEOPLE_BLOCK), \
            Em.element_is_not_presented('power in people block', 'Tensor Main Page')
        assert self.is_element_visible(MainPageLocators.POWER_IN_PEOPLE_BLOCK), \
            Em.element_is_not_visible('power in people block', 'Tensor Main Page')
        self.scroll_to_element(MainPageLocators.POWER_IN_PEOPLE_BLOCK)

    def go_to_about_page(self):
        assert self.click_element(MainPageLocators.ABOUT_LINK), \
            Em.cant_click_element('about link', 'Tensor Main Page')
