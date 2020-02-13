#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A simple Python wrapper client for the Dragos portal API"""
import requests

from configparser import RawConfigParser

class DragosPortalAPI:
    """auth object for Dragos portal API - basically an API wrapper/implementation"""
    def __init__(self, access_token, access_key):
        self.access_token = access_token
        self.access_key = access_key

        self.api_headers = {
            "Api-Token": self.access_token,
            "Api-Secret": self.access_key
        }


    def get_intel_report(self, report_id):
        r = requests.get("https://portal.dragos.com/api/v1/products/" + report_id, headers=self.api_headers)
        return r.json()


    def get_intel_reports(self):
        """https://portal.dragos.com/api/v1/doc/#!/products/Api_V1_Products_index_get_1"""
        reports = []

        page = 1
        total_pages = page
        while page <= total_pages:
            r = requests.get("https://portal.dragos.com/api/v1/products?page={}&page_size=500".format(page), headers=self.api_headers)
            data = r.json()
            total_pages = data["total_pages"]
            page += 1

            reports += data["products"]

        return reports


    def get_report_indicators(self, report_id):
        """https://portal.dragos.com/api/v1/doc/#!/indicators/Api_V1_Indicators_index_get_0"""
        r = requests.get("https://portal.dragos.com/api/v1/indicators?page_size=1000&serial=" + report_id, headers=self.api_headers)
        return r.json()


    def lookup_indicator(self, value, indicator_type=""):
        url = "https://portal.dragos.com/api/v1/indicators?value=" + value
        if indicator_type:
            url += "&type=" + indicator_type
        r = requests.get(url, headers=self.api_headers)
        return r.json()


def load_api_config(config_filename):
    """get API creds from py INI config file (no quotes in config)"""
    portal_config = RawConfigParser()
    try:
        portal_config.read(config_filename)
    except FileNotFoundError:
        print("missing Dragos portal config file")
        exit(1)

    try:
        access_token = portal_config.get("dragos portal", "access_token")
        access_key = portal_config.get("dragos portal", "access_key")
        return DragosPortalAPI(access_token, access_key)
    except:
        print("error reading Dragos API config")
        exit(1)
