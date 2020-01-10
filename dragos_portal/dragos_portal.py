#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A simple Python wrapper client for the Dragos portal API"""
import requests

from configparser import RawConfigParser

# auth object for Dragos portal API - basically an API wrapper/implementation
class DragosPortalAPI:
    def __init__(self, access_token, access_key):
        self.access_token = access_token
        self.access_key = access_key

        self.api_headers = {
            "Api-Token": self.access_token,
            "Api-Secret": self.access_key
        }


    def get_wv_reports(self):
        headers = self.api_headers

        # https://portal.dragos.com/api/v1/doc/#!/products/Api_V1_Products_index_get_1
        r = requests.get("https://portal.dragos.com:443/api/v1/products?page=1&page_size=500", headers=headers)
        reports = r.json()
        #print(report)

        return reports


    def report_has_indicators(self, report_id):
        headers = self.api_headers

        # https://portal.dragos.com/api/v1/doc/#!/indicators/Api_V1_Indicators_index_get_0
        r = requests.get("https://portal.dragos.com:443/api/v1/indicators?serial=" + report_id, headers=headers)
        indicators = r.json()

        if indicators["total"] > 0:
            return True
        elif indicators["total"] == 0:
            return False


def dragosportal_api_config():
    # get wv API creds from py INI config file (no quotes in config)
    wv_config = RawConfigParser()
    try:
        wv_config.read("dragos_portal.cfg")
    except FileNotFoundError:
        print("missing worldview config file")
        exit(1)

    try:
        access_token = wv_config.get("worldview", "access_token")
        access_key = wv_config.get("worldview", "access_key")
        return DragosPortalAPI(access_token, access_key)
    except:
        print("error reading atlassian API config")
        exit(1)
