#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast

from selenium import webdriver


class Initialization(object):
    def __init__(self, config):
        self.config = config
        self.driver = self.init_driver()

    def init_driver(self):
        profile = self.config.profile
        driver = webdriver.Firefox(profile)
        driver.set_page_load_timeout(self.config.pageload_timeout)
        driver.maximize_window()
        return driver

    def shutdown(self):
        self.driver.quit()
