#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HomePage(object):
    def __init__(self, driver):
        self._driver = driver

    def contacts_button(self):
        return self._driver.find_element_by_css_selector('.GlobalNavigation a[href="#/abook/list?tab=contacts"]')

    def logo(self):
        return self._driver.find_element_by_class_name('Logo')

    def new_message_button(self):
        return self._driver.find_element_by_css_selector('button[href="#/compose/draft?type=new"]')
