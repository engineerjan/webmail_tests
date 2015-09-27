#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import sys

from selenium.webdriver.support.ui import WebDriverWait
from web_objects.contact_page import ContactPage
from web_objects.home_page import HomePage
from actions.notification_actions import NotificationActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from allure.constants import AttachmentType


class ContactpageActions(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.timeout)
        self.long_wait = WebDriverWait(driver, config.long_timeout)
        self.notification = NotificationActions(driver, config)
        self.contact_page = ContactPage(driver)
        self.home_page = HomePage(driver)
        self.contact = config.contacts
        self.url = config.url

    @pytest.allure.step('Dodawanie kontaktu')
    def add_contact(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            wait.until(lambda d: contact_page.add_contact_button().is_displayed(), 
                message="przycisk dodawania kontaktow nie zostal wyswietlony")
            contact_page.add_contact_button().click()
            self.fill_basic_contact_details()
            self.fill_email()
            self.fill_phone()
            self.fill_address()
            self.fill_note()
            wait.until(lambda d: contact_page.save_contact_button().is_displayed(), 
                message="przycisk zapisywania kontaktow jest niewidoczny")
            contact_page.save_contact_button().click()
            self.notification.notifications_check()
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Wypelnianie podstawowych danych kontaktowych')
    def fill_basic_contact_details(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            contact = self.contact[0]
            wait.until(lambda d: contact_page.name_input().is_displayed(), 
                message="pole do wpisywania imienia nie zostalo wyswietlone")
            contact_page.name_input().send_keys(contact['name'])
            wait.until(lambda d: contact_page.lastname_input().is_displayed(), 
                message="pole do wpisywania nazwiska nie zostalo wyswietlone")
            contact_page.lastname_input().send_keys(contact['lastname'])
            wait.until(lambda d: contact_page.fn_input().is_displayed(), 
                message="pole do wpisywania pseudonimu nie zostalo wyswietlone")
            contact_page.fn_input().send_keys(contact['fn'])
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Wypelnianie pola z adresem skrzynki pocztowej')
    def fill_email(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            wait.until(lambda d: contact_page.another_email_button().is_displayed(), 
                message="brak przycisku dodaj kolejny email")
            contact_page.another_email_button().click()
            wait.until(lambda d: len(contact_page.email_inputs()) > 1)
            for i in range(2):
                contact = self.contact[i]
                wait.until(lambda d: contact_page.email_inputs()[i].is_displayed(), 
                    message=" nie zostal wyswietlony")
                contact_page.email_inputs()[i].send_keys(contact['email'])
                wait.until(lambda d: contact_page.email_dropdown_menues()[i].is_displayed(), 
                    message="menu kategorii adresu mailowego nie zostalo wyswietlone")
                select = Select(contact_page.email_dropdown_menues()[i])
                select.select_by_value(contact['type'])
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Wypelnianie pola z numerem telefonu')
    def fill_phone(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            contact = self.contact[0]
            wait.until(lambda d: contact_page.phone_input().is_displayed(),
                message="pole do wpisywania numeru tel nie zostalo wyswietlone")
            contact_page.phone_input().send_keys(contact['phone'])
            wait.until(lambda d: contact_page.phone_dropdown_menu().is_displayed(), 
                message="phone dropdown menu jest niewidoczne")
            select = Select(contact_page.phone_dropdown_menu())
            select.select_by_value(contact['type'])
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Wypelnianie pola z adresem')
    def fill_address(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            wait.until(lambda d: contact_page.another_address_button().is_displayed(), message="brak buttona another adress")
            contact_page.another_address_button().click()
            wait.until(lambda d: len(contact_page.address_forms()) > 1)
            for i in range(2):
                contact = self.contact[i]
                wait.until(lambda d: contact_page.street_inputs()[i].is_displayed(), message="pole ulica jest niewidoczne")
                contact_page.street_inputs()[i].send_keys(contact['street'])
                wait.until(lambda d: contact_page.region_inputs()[i].is_displayed(), message="pole wojewodztwo jest niewidoczne")
                contact_page.region_inputs()[i].send_keys(contact['region'])
                wait.until(lambda d: contact_page.postcode_inputs()[i].is_displayed(), message="pole kod pocztowy jest niewidoczne")
                contact_page.postcode_inputs()[i].send_keys(contact['postcode'])
                wait.until(lambda d: contact_page.city_inputs()[i].is_displayed(), message="pole miasto jest niewidoczne")
                contact_page.city_inputs()[i].send_keys(contact['city'])
                wait.until(lambda d: contact_page.country_inputs()[i].is_displayed(), message="pole kraj jest niewidoczne")
                contact_page.country_inputs()[i].send_keys(contact['country'])
                wait.until(lambda d: contact_page.address_dropdown_menues()[i].is_displayed(), 
                    message="menu kategorii adresu nie zostalo wyswietlone")
                select = Select(contact_page.address_dropdown_menues()[i])
                select.select_by_value(contact['type'])
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Wypelnianie pola z notatka')
    def fill_note(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            wait.until(lambda d: contact_page.note_input().is_displayed(), message="pole notatki jest niewidoczne")
            contact_page.note_input().send_keys('Przykladowa notatka')
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Walidacja dodanego kontaktu')
    def validate_contact(self):
        try:
            actions = ActionChains(self.driver)
            wait = self.wait
            contact_page = self.contact_page
            added_contact = self.open_added_contact()
            contact = self.contact
            actions.move_to_element(added_contact).perform()
            actions.click(contact_page.meta(added_contact)).perform()
            wait.until(lambda d: contact_page.contact_details().is_displayed())
            assert contact[0]['phone'] in contact_page.added_phone().text
            for i in range(2):
                assert contact[i]['email'] in contact_page.added_emails()[i].text
                assert contact[i]['street'] in contact_page.added_street()[i].text
                assert contact[i]['postcode'] in contact_page.added_city()[i].text
                assert contact[i]['city'] in contact_page.added_city()[i].text
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Usuwanie kontaktu')
    def delete_contact(self):
        try:
            contact_page = self.contact_page
            actions = ActionChains(self.driver)
            wait = self.wait
            wait.until(lambda d: contact_page.more_options_button().is_displayed(), message="przycisk: wiecej opcji jest niewidoczny")
            actions.move_to_element(contact_page.more_options_button()).perform()
            contact_page.more_options_button().click()
            wait.until(lambda d: contact_page.delete_contact_button().is_displayed(), message="brak przycisku usuwanaia kontaktu")
            contact_page.delete_contact_button().click()
            self.notification.notifications_check()
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.step('Otwieranie dodanego kontaktu')
    def open_added_contact(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            contact = self.contact[0]
            wait.until(lambda d: len(contact_page.contact_list()) > 0, message="lista kontaktów nie zostala wyswietlona")
            for c in contact_page.contact_list():
                if contact['fn'] in contact_page.fullname(c):
                    return c
            else:
                raise Exception('Brak dodanego kontaktu')
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise       

    @pytest.allure.step('Otwieranie strony z wiadomosciami')
    def open_abook_page(self):
        try:
            wait = self.wait
            contact_page = self.contact_page
            wait.until(lambda d: contact_page.abook_button().is_displayed(),
                message="Brak przycisku do otwierania strony z wiadomosciami")
            contact_page.abook_button().click()
        except Exception:
            pytest.allure.attach(sys._getframe().f_code.co_name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise   