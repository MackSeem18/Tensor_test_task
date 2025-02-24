from selenium.webdriver.common.by import By


class MainPageLocators:
    CONTACTS_BUTTON = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu')
    CONTACTS_LINK_BUTTON = (By.CSS_SELECTOR, '[href="/contacts"].sbisru-link')
    DOWNLOAD_LOCAL_VERSIONS_LINK = (By.CSS_SELECTOR, '[href="/download"]')


class ContactsPageLocators:
    TENSOR_LOGO = (By.CSS_SELECTOR,
                   '#contacts_clients>.sbis_ru-container img[alt="Разработчик системы Saby — компания «Тензор»"]')
    REGION_CHANGE_LINK = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
    KAMCHATKA_REGION_LINK = (By.CSS_SELECTOR, '[title="Камчатский край"] > span')
    PARTNERS_LIST = (By.CSS_SELECTOR, '#city-id-2')


class DownloadPageLocators:
    WEB_INSTALLER_LINK = (By.XPATH, ".//div/h3[text()='Веб-установщик ']/parent::div/following::div[1]//a")
