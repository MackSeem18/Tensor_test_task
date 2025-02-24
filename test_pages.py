import pytest
import allure

from pages.sbis_pages.main_page import SbisMainPage
from pages.sbis_pages.contacts_page import SbisContactsPage
from pages.sbis_pages.download_page import SbisDownloadPage
from pages.tensor_pages.about_page import TensorAboutPage
from pages.tensor_pages.main_page import TensorMainPage


@allure.story("Задание 1")
def test_one(browser):
    link = "https://sbis.ru/"
    page = SbisMainPage(browser, link)
    page.open()
    with allure.step('Переходим в раздел "Контакты"'):
        page.go_to_contacts_page()
        page = SbisContactsPage(browser, link)
    with allure.step('Находим баннер Тензор и кликаем по нему'):
        page.go_to_tensor_page()
    with allure.step('Переходим на tensor.ru'):
        page.switch_to_tensor_window()
        link = "https://tensor.ru"
        page = TensorMainPage(browser, link)
    with allure.step('Проверяем, что есть блок "Сила в людях"'):
        page.should_be_power_in_people_block()
    with allure.step('Переходим в блок "Подробнее" и убеждаемся, что открылась https://tensor.ru/about'):
        page.go_to_about_page()
        link = "https://tensor.ru/about"
        page = TensorAboutPage(browser, link)
        page.should_be_expected_url(link)
    with allure.step('Находим блок "Работаем" и проверяем, что у всех фотографий одинаковые высота и ширина'):
        page.should_be_working_block()
        page.pictures_on_working_block_should_be_the_same_sizes()


@allure.story("Задание 2")
def test_two(browser):
    with allure.step('Открываем https://sbis.ru/contacts и проверяем, что открылся наш регион'):
        link = "https://sbis.ru/contacts"
        page = SbisContactsPage(browser, link)
        page.open()
        page.should_be_expected_region_in_region_change_link("Пермский край")
        page.should_be_expected_region_partners("Пермь")
    with allure.step('Меняем регион на "Камчатский край"'):
        page.change_region_to_kamchatka()
    with allure.step('Проверим, что регион сменился'):
        page.should_be_expected_region_in_region_change_link("Камчатский край")
        page.should_be_expected_region_in_url("41-kamchatskij-kraj")
        page.should_be_expected_region_in_tab_title("Камчатский край")
        page.should_be_expected_region_partners("Петропавловск-Камчатский")


@allure.story("Задание 3")
def test_three(browser):
    with allure.step('Открываем https://sbis.ru'):
        link = "https://sbis.ru/"
        page = SbisMainPage(browser, link)
        page.open()
    with allure.step('Переходим на страницу загрузки'):
        page.go_to_download_page()
        page = SbisDownloadPage(browser, link)
    with allure.step('Скачиваем и проверяем файл'):
        page.download_file_and_check_size()
