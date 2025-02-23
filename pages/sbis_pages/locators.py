from selenium.webdriver.common.by import By

class BasePageLocators:
    pass


class MainPageLocators:
    CONTACTS_BUTTON = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu')
    CONTACTS_LINK_BUTTON = (By.CSS_SELECTOR, '[href="/contacts"].sbisru-link')


class ContactsPageLocators:
    TENSOR_LOGO = (By.CSS_SELECTOR,
                   '#contacts_clients>.sbis_ru-container img[alt="Разработчик системы Saby — компания «Тензор»"]')
    REGION_CHANGE_LINK = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
    KAMCHATKA_REGION_LINK = (By.CSS_SELECTOR, '[title="Камчатский край"] > span')
    PARTNERS_LIST = (By.CSS_SELECTOR, '#city-id-2')