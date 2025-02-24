import pytest
import shutil
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    download_path = fr'{os.getcwd()}\tmp'
    print(f"\ncreate temp folder for downloads {download_path}")
    os.makedirs(download_path)
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    browser = webdriver.Chrome(options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(f"\nremove temp folder for downloads {download_path}")
    shutil.rmtree(download_path)
