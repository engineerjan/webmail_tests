#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ContactPage(object):
    def __init__(self, driver):
        self._driver = driver

    def add_contact_button(self):
        return self._driver.find_element_by_css_selector('.wstrzykniety blad button[href="#/abook/contact/new"]')

    def name_input(self):
        return self._driver.find_element_by_css_selector('input[name="firstname"]')

    def lastname_input(self):
        return self._driver.find_element_by_css_selector('input[name="lastname"]')

    def fn_input(self):
        return self._driver.find_element_by_css_selector('input[name="fn"]')

    def email_inputs(self):
        return self._driver.find_elements_by_css_selector('input[name="email_value"]')

    def another_email_button(self):
        return self._driver.find_element_by_css_selector(
            'a[ng-click="contactFormDirectiveController.addField(ContactFormController.contact.data.email)"]')

    def phone_input(self):
        return self._driver.find_element_by_css_selector('input[name="tel_value"]')

    def another_address_button(self):
        return self._driver.find_element_by_css_selector(
            'a[ng-click="contactFormDirectiveController.addField(ContactFormController.contact.data.adr)"]')

    def address_forms(self):
        return self._driver.find_elements_by_css_selector(
            'li[ng-repeat="field in collection_adr=ContactFormController.contact.data.adr track by $index"]')

    def street_inputs(self):
        return self._driver.find_elements_by_css_selector('input[name="adr_street"]')

    def region_inputs(self):
        return self._driver.find_elements_by_css_selector('input[name="adr_region"]')

    def postcode_inputs(self):
        return self._driver.find_elements_by_css_selector('input[name="adr_code"]')

    def city_inputs(self):
        return self._driver.find_elements_by_css_selector('input[name="adr_city"]')

    def country_inputs(self):
        return self._driver.find_elements_by_css_selector('input[name="adr_country"]')

    def email_dropdown_menues(self):
        return self._driver.find_elements_by_css_selector('select[name="email_type"]')

    def phone_dropdown_menu(self):
        return self._driver.find_element_by_css_selector('select[name="tel_type"]')

    def address_dropdown_menues(self):
        return self._driver.find_elements_by_css_selector('select[name="adr_type"]')

    def note_input(self):
        return self._driver.find_element_by_class_name('Textarea')

    def save_contact_button(self):
        return self._driver.find_element_by_css_selector('button[ng-click="ContactFormController.save()"]')

    def contact_list(self):
        return self._driver.find_elements_by_css_selector('li[class^="Contact-item List-item FlexGrid ng-scope"]')

    def fullname(self, element):
        return element.find_element_by_css_selector('.Contact-fullname span').text

    def meta(self, element):
        return element.find_element_by_css_selector('div[class="FlexGrid-cell u-flexMax Contact-meta"]')

    def contact_details(self):
        return self._driver.find_element_by_class_name('Contact-details')

    def added_emails(self):
        return self._driver.find_elements_by_css_selector(
            'li[ng-repeat="item in ContactController.resource.contact.data.email track by $index"] a')

    def added_phone(self):
        return self._driver.find_element_by_css_selector(
            'li[ng-repeat="item in ContactController.resource.contact.data.tel track by $index"] div')

    def added_street(self):
        return self._driver.find_elements_by_css_selector('div[ng-if="::item.street"]')

    def added_city(self):
        return self._driver.find_elements_by_css_selector('div[ng-if="::item.code"]')

    def more_options_button(self):
        return self._driver.find_element_by_css_selector(
            'div[class="Contact-header FlexGrid"] button[nh-dropdown="abook/contact-options-dropdown"]')

    def delete_contact_button(self):
        return self._driver.find_element_by_css_selector('button[ng-click="delete({contacts: item}); __hideDropdown()"]')

    def first_contact(self):
        return self._driver.find_element_by_css_selector('li[class^="Contact-item List-item"]')

    def abook_button(self):
        return self._driver.find_element_by_css_selector('.GlobalNavigation a[href="#/conversations/list?label=1"]')