#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from web_objects.composer_page import ComposerPage
from web_objects.home_page import HomePage
from actions.notification_actions import NotificationActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from allure.constants import AttachmentType


class ComposerpageActions(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.timeout)
        self.long_wait = WebDriverWait(driver, config.long_timeout)
        self.composer_page = ComposerPage(driver)
        self.home_page = HomePage(driver)
        self.actions = ActionChains(driver)
        self.suggested_recipient = config.contacts[0]
        self.notification = NotificationActions(driver, config)

    @pytest.allure.step('Sprawdzenie sugerowanego odbiorcy')
    def check_suggested_recipient(self):
        wait = self.wait
        composer_page = self.composer_page
        recipient = self.suggested_recipient
        wait.until(lambda d: composer_page.recipient_input().is_displayed(), 
            message="pole do wpisywania odbiorcy nie zostalo wyswietlone")
        composer_page.recipient_input().send_keys(recipient['name'][0:3])
        wait.until(lambda d: composer_page.suggestion_overlay().is_displayed(), 
            message="nie zostala wyswietlona lista sugerowanych odbiorcow")
        for i in composer_page.recipients_sugestion():
            if recipient['fn'] in i.text:
                break
            else:
                pass
        else:
            raise Exception('Brak sugerowanego odbiorcy')
