#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NotificationPage(object):
    def __init__(self, driver):
        self._driver = driver

    def notifications(self):
        return self._driver.find_element_by_css_selector('div[class^="Notification Notification-"]')

    def notification(self, notification_type):
        return self._driver.find_element_by_css_selector('div[class="Notification Notification-{0}"] p'.format(notification_type))
