# Copyright 2022 Appdiff Inc.

"""A brief example demonstrating the basic capabilities of test.ai enhanced Selenium."""

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
    accessories_nav_link = driver.find_element_by_id("menu-item-671", "accessories_nav_link")
    accessories_nav_link.click()

    sleep(2)

    anchor_bracelet = driver.find_element_by_xpath('//*[@id="main"]/div/ul/li[1]/div[1]/a', "anchor_bracelet")
    anchor_bracelet.click()

    sleep(2)

    add_to_cart = driver.find_element_by_xpath('//*[@id="product-2707"]/div[2]/form/button', "add_to_cart")
    add_to_cart.click()

    sleep(2)

    view_cart = driver.find_element_by_css_selector("#main > div > div.woocommerce-notices-wrapper > div > a", "view_cart")
    view_cart.click()

    # Done
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    _main()
