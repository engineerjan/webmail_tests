#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_objects.notification_page import NotificationPage
from selenium.common.exceptions import StaleElementReferenceException


class NotificationActions(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.notification = NotificationPage(driver)
        self.wait = WebDriverWait(driver, config.timeout)
        self.long_wait = WebDriverWait(driver, config.long_timeout)

    def notifications_check(self):
        wait = self.long_wait
        long_wait = self.long_wait
        notification = self.notification
        wait.until(lambda d: notification.notifications())
        self.driver.implicitly_wait(0.5)
        while True:
            try:
                print notification.notifications().get_attribute('class')
                if 'success' in notification.notifications().get_attribute('class'):
                    wait.until(EC.staleness_of(self.notification.notification('success')))
                    break
                elif 'info' in notification.notifications().get_attribute('class'):
                    wait.until(EC.staleness_of(self.notification.notification('info')))
                    break
                elif 'progress' in notification.notifications().get_attribute('class'):
                    long_wait.until(EC.staleness_of(self.notification.notification('progress')), 
                        message="wysylanie wiadomosci trwalo zbyt dlugo")
                elif 'warning' in notification.notifications().get_attribute('class'):
                    print 'warning'
                elif 'error' in notification.notifications().get_attribute('class'):
                    raise Exception('Notification Error')
                else:
                    continue
            except StaleElementReferenceException as EX:
                print EX
                continue
        self.driver.implicitly_wait(30)
