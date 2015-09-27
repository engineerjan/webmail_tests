#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from configuration.config import Config
from configuration.initialization import Initialization
from actions.loginpage_actions import Login
from actions.contactpage_actions import ContactpageActions
from actions.homepage_actions import HomepageActions
from actions.composerpage_actions import ComposerpageActions
from selenium.webdriver.support.ui import WebDriverWait


class TestEngineeringThesis(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.initialization = Initialization(self.config)

    def test_engineering_thesis(self):

        driver = self.initialization.driver
        login = Login(driver, self.config)
        wait = WebDriverWait(driver, self.config.timeout)
        contactpage_actions = ContactpageActions(driver, self.config)
        homepage_actions = HomepageActions(driver, self.config)
        composerpage_actions = ComposerpageActions(driver, self.config)
        login.login()
        homepage_actions.open_contacts_page()
        contactpage_actions.add_contact()
        contactpage_actions.open_abook_page()
        homepage_actions.open_new_message_composer()
        composerpage_actions.check_suggested_recipient()
        homepage_actions.open_contacts_page()
        contactpage_actions.validate_contact()
        contactpage_actions.delete_contact()

    def tearDown(self):
        self.initialization.shutdown()

if __name__ == "__main__":
    unittest.main()
