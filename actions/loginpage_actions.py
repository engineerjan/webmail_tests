#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import traceback
import pytest
import sys

from selenium.webdriver.support.ui import WebDriverWait
from web_objects.login_page import LoginPage
from web_objects.home_page import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from allure.constants import AttachmentType


class Login(unittest.TestCase):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.wait = WebDriverWait(self.driver, self.config.timeout)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.actions = ActionChains(self.driver)

    @pytest.allure.step('Logowanie do poczty')
    def login(self):
        try:
            self.driver.get(self.config.url['main_url'])
            self.wait.until(lambda d: self.login_page.email_input().is_displayed(), message='Brak pola do wpisywania adresu')
            self.login_page.email_input().clear()
            self.login_page.email_input().send_keys(self.config.user_login)
            self.wait.until(lambda d: self.login_page.password_input().is_displayed(), message='Brak pola do wpisywania hasla')
            self.login_page.password_input().clear()
            self.login_page.password_input().send_keys(self.config.user_password)
            self.login_page.login_submit().click()
            self.wait.until(lambda d: self.driver.current_url != self.config.url['main_url'])
            assert 'conversation' in self.driver.current_url
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, 
                self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Wylogowanie z poczty')
    def logout(self):
        try:
            self.wait.until(EC.visibility_of(self.home_page.userkit_button()))
            self.actions.move_to_element(self.home_page.userkit_button()).perform()
            self.home_page.userkit_button().click()
            self.wait.until(lambda d: self.home_page.logout_button().is_displayed(), message='przycisk wylogowania jest niewidoczny')
            self.home_page.logout_button().click()
            self.wait.until(lambda d: "wylogowano" in self.driver.current_url)
            self.driver.get(self.config.url['main_url'])
            self.wait.until(lambda d: self.login_page.email_input().is_displayed(), message='Brak pola do wpisywania adresu')
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, 
                self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise
