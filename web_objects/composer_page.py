#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ComposerPage(object):
    def __init__(self, driver):
        self._driver = driver

    def composer_form(self):
        return self._driver.find_element_by_css_selector('form[class="composer ng-pristine ng-valid"] .composer__body')

    def recipient_input(self):
        return self._driver.find_element_by_css_selector(
            '.Composer-row[ng-if="draftFormDirectiveController.fieldsVisibility.to"] input[class="Composer-input"]')
    
    def suggestion_overlay(self):
        return self._driver.find_element_by_css_selector('div[class="Suggestion Suggestion--overlay"]')

    def recipients_sugestion(self):
        return self._driver.find_elements_by_css_selector('li[ng-repeat="item in recipients.suggestions"] strong')
