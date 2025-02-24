from pages.base_page import BasePage
from pages.sbis_pages.locators import MainPageLocators
from error_messages import ErrorMessages as Em


class SbisMainPage(BasePage):
    def go_to_contacts_page(self):
        assert self.click_element(MainPageLocators.CONTACTS_BUTTON), \
            Em.cant_click_element('contacts button', 'Main Page')
        assert self.click_element(MainPageLocators.CONTACTS_LINK_BUTTON), \
            Em.cant_click_element('contacts link button', 'Main Page')

    def go_to_download_page(self):
        assert self.click_element(MainPageLocators.DOWNLOAD_LOCAL_VERSIONS_LINK), \
            Em.cant_click_element('download local versions link', 'Main Page')