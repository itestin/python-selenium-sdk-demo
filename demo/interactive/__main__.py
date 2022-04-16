# Copyright 2022 Appdiff Inc.

"""A brief example demonstrating the interactive capabilities of test.ai enhanced Selenium."""

__author__ = ('alec@test.ai (Alexander Wu)')
__copyright__ = 'Copyright 2022 Appdiff Inc.'

import logging
import sys

from time import sleep

from test_ai.test_ai import TestAiDriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def _main() -> None:
    """Main driver"""

    # log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    chrome_driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver = TestAiDriver(chrome_driver, sys.argv[1])

    # Navigate to the target website
    driver.get("https://testaistore.com/")
    sleep(2)

    # Find and interact with elements
    store_nav_link = driver.find_by_element_name("store_nav_link")
    store_nav_link.click()

    sleep(2)

    search_products_input = driver.find_by_element_name("search_products_input")
    search_products_input.send_keys("Shoes")

    sleep(2)

    search_button = driver.find_by_element_name("search_button")
    search_button.click()

    sleep(2)

    green_shoes = driver.find_by_element_name("green_shoes")
    green_shoes.click()

    sleep(2)

    add_to_cart = driver.find_by_element_name("add_to_cart")
    add_to_cart.click()

    # Done
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    _main()
