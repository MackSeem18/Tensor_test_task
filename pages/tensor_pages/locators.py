from selenium.webdriver.common.by import By


class MainPageLocators:
    POWER_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4 > .s-Grid-col:first-child')
    ABOUT_LINK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4 a')


class AboutPageLocators:
    WORKING_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-About__block3")
    PICTURES_IN_WORKING_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-About__block3  img")
