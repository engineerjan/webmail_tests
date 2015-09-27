#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import sys

from selenium.webdriver.support.ui import WebDriverWait
from actions.notification_actions import NotificationActions
from web_objects.home_page import HomePage
from allure.constants import AttachmentType


class HomepageActions(object):
    def __init__(self, driver, config):
        self.config = config
        self.driver = driver
        self.wait = WebDriverWait(driver, config.timeout)
        self.long_wait = WebDriverWait(driver, config.long_timeout)
        self.home_page = HomePage(driver)
        self.notification = NotificationActions(driver, config)

    @pytest.allure.step('Otwieranie strony z kontaktami')
    def open_contacts_page(self):
        try:        
            home_page = self.home_page
            self.wait.until(lambda d: home_page.contacts_button().is_displayed(),
                message="Przycisk otwierajacy strone z kontaktami jest niewidoczny")
            home_page.contacts_button().click()
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, 
                self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Otwieranie okna do komponowania nowej wiadomosci')
    def open_new_message_composer(self):
        try:        
            home_page = self.home_page
            self.wait.until(lambda d: home_page.new_message_button().is_displayed(),
                message="Przycisk otwierajacy strone do \
                komponowania wiadomosci jest niewidoczny")
            home_page.new_message_button().click()
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, 
                self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise
