from pages.base_page import BasePage
from pages.sbis_pages.locators import ContactsPageLocators
from selenium.webdriver.support import expected_conditions

from error_messages import ErrorMessages as Em


class SbisContactsPage(BasePage):
    def should_be_tensor_logo(self):
        assert self.is_element_present(*ContactsPageLocators.TENSOR_LOGO), \
            "Tensor logo is not presented"

    def go_to_tensor_page(self):
        assert self.click_element(ContactsPageLocators.TENSOR_LOGO),\
            Em.cant_click_element('tensor logo', 'Contacts Page')

    def switch_to_tensor_window(self):
        tensor_window = self.browser.window_handles[1]
        self.browser.switch_to.window(tensor_window)

    def should_be_expected_region_in_region_change_link(self, expected_region):
        actual_region = self.browser.find_element(*ContactsPageLocators.REGION_CHANGE_LINK).text
        assert actual_region == expected_region,\
            Em.region_does_not_match_expected("change region link", expected_region, actual_region)

    def should_be_expected_region_partners(self, expected_region):
        assert self.is_element_present(ContactsPageLocators.PARTNERS_LIST)
        partners_list_city = self.browser.find_element(*ContactsPageLocators.PARTNERS_LIST).text
        assert partners_list_city == expected_region,\
            Em.region_does_not_match_expected("change region link", expected_region, partners_list_city)

    def change_region_to_kamchatka(self):
        assert self.click_element(ContactsPageLocators.REGION_CHANGE_LINK),\
            Em.cant_click_element("region change link", "Contacts Page")
        assert self.point_and_click_element(ContactsPageLocators.KAMCHATKA_REGION_LINK),\
            Em.cant_click_element('Kamchatka region link', "Contacts Page")
        self.wait.until_not(expected_conditions.presence_of_element_located(ContactsPageLocators.KAMCHATKA_REGION_LINK))

    def should_be_expected_region_in_url(self, expected_region):
        url = self.browser.current_url
        question_mark_index = url.find('?')
        region = url[25:question_mark_index]
        assert region == expected_region,\
            Em.region_does_not_match_expected("url", expected_region, region)

    def should_be_expected_region_in_tab_title(self, expected_region):
        tab_title = self.browser.title
        region = tab_title[16:]
        assert region == expected_region,\
            Em.region_does_not_match_expected("tab title", expected_region, region)



