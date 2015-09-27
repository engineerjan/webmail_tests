#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import ast
import os
import re
import datetime

from selenium import webdriver


class Config:
    config = ConfigParser.ConfigParser()
    config.read('configuration/config.ini')
    user_login = config.get('user', 'login')
    user_password = config.get('user', 'password')
    contacts = ast.literal_eval(config.get('contacts', 'contact'))
    timeout = int(config.get('timeout_settings', 'standard_timeout'))
    short_timeout = int(config.get('timeout_settings', 'short_timeout'))
    long_timeout = int(config.get('timeout_settings', 'long_timeout'))
    implicitly_wait = int(config.get('timeout_settings', 'implicitly_wait'))
    pageload_timeout = int(config.get('timeout_settings', 'page_timeout'))
    url = ast.literal_eval(config.get('url', 'url'))

    def __init__(self):
        self.profile = self.set_preferences()
        
    def set_preferences(self):
        preferences = ast.literal_eval(self.config.get('profile', 'preferences'))
        profile = webdriver.FirefoxProfile()
        for p in preferences:
            profile.set_preference(p, preferences[p])
        profile.update_preferences()
        return profile
