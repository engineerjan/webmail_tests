#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LoginPage(object):
    def __init__(self, driver):
        self._driver = driver

    def email_input(self):
        return self._driver.find_element_by_css_selector('#loginForm .TextInput[type="email"]')

    def password_input(self):
        return self._driver.find_element_by_css_selector('#loginForm .TextInput[type="password"]')

    def login_submit(self):
        return self._driver.find_element_by_css_selector('.Button[type="submit"]')
