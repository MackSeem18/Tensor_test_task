from pages.base_page import BasePage
from pages.tensor_pages.locators import AboutPageLocators
from error_messages import ErrorMessages as Em


class TensorAboutPage(BasePage):
    def should_be_working_block(self):
        assert self.is_element_present(AboutPageLocators.WORKING_BLOCK), \
            Em.element_is_not_presented('working block', 'Tensor About Page')
        working_block = self.browser.find_element(*AboutPageLocators.WORKING_BLOCK)

        self.scroll_to_element(AboutPageLocators.WORKING_BLOCK)

        assert self.is_element_visible(AboutPageLocators.WORKING_BLOCK), \
            Em.element_is_not_visible('working block', 'Tensor About Page')

    def pictures_on_working_block_should_be_the_same_sizes(self):
        pictures_elements = self.browser.find_elements(*AboutPageLocators.PICTURES_IN_WORKING_BLOCK)
        widths, heights = [], []
        for element in pictures_elements:
            widths.append(element.value_of_css_property('width'))
            heights.append(element.value_of_css_property('height'))
        for i in range(len(widths) - 1):
            assert widths[i] == widths[i + 1],\
                Em.elements_parameters_do_not_match("width", f"{i} picture width",
                                                    widths[i], f"{i + 1} picture width", widths[i + 1])
            assert heights[i] == heights[i + 1],\
                Em.elements_parameters_do_not_match("height", f"{i} picture height",
                                                    heights[i], f"{i + 1} picture height", heights[i + 1])

