from pages.base_page import BasePage
from pages.sbis_pages.locators import MainPageLocators
from error_messages import ErrorMessages as Em


class SbisMainPage(BasePage):
    def should_be_contacts_button(self):
        assert self.is_element_present(MainPageLocators.CONTACTS_BUTTON), ("Contacts button is not "
                                                                           "presented")

    def should_be_contacts_link_button(self):
        assert self.is_element_present(MainPageLocators.CONTACTS_LINK_BUTTON), "Contacts link button is not presented"

    def go_to_contacts_page(self):
        assert self.click_element(MainPageLocators.CONTACTS_BUTTON), \
            Em.cant_click_element('Contacts button', 'Main Page')
        assert self.click_element(MainPageLocators.CONTACTS_LINK_BUTTON), \
            Em.cant_click_element('contacts link button', 'Main Page')
