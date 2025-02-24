from pages.base_page import BasePage
from pages.sbis_pages.locators import DownloadPageLocators
from error_messages import ErrorMessages as Em


class SbisDownloadPage(BasePage):
    def download_file_and_check_size(self):
        assert self.click_element(DownloadPageLocators.WEB_INSTALLER_LINK)
        expected_file_size = float(self.browser.find_element(*DownloadPageLocators.WEB_INSTALLER_LINK).text[13:18])
        actual_file_size = self.get_downloaded_file_size("sbisplugin-setup-web.exe", 300)
        assert actual_file_size,\
            Em.timeout_could_not_download_file("sbisplugin-setup-web.exe", 300)
        assert expected_file_size == round(float(actual_file_size) / (2 ** 20), 2),\
            Em.actual_file_size_is_different_from_expected("Download Plugin Page", "sbisplugin-setup-web.exe",
                                                           expected_file_size, actual_file_size)
