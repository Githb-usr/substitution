#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

from src.data.model.product import Product

from config.settings import API_BASE_URL, PAGE_SIZE, PAGE_NUMBER, FIELDS_OF_PRODUCT

class OpenFoodApi:
    """
        OpenFoodApi class
        To manage Open Food Facts API data recovery
    """
    
    def get_api_products(self, page_number):
        """
            We retrieve the raw data (products) from the api
            :return: json data
            :rtype: list()
        """
        params = {
            'action': 'process',
            'json': 'true',
            'page_size': PAGE_SIZE,
            'page': page_number,
            'fields': FIELDS_OF_PRODUCT,
            'sort_by': 'unique_scans_n'
            }
        headers = {'User-Agent': 'NameOfYourApp - Android - Version 1.0 - www.yourappwebsite.com'}
        result = requests.get(API_BASE_URL, headers = headers, params = params)
        print(result.status_code)
        data = result.json()
        products_data = data['products']
        
        return products_data
   
    def get_full_api_products(self):
        """
            We recover as many pages of raw data as defined in the application configuration (see settings file).
            :return: json data
            :rtype: list()
        """
        full_products_data = []
        
        for i in range(1, PAGE_NUMBER + 1):
            products_data = self.get_api_products(i)
            for data in products_data:
                full_products_data.append(data)

        return full_products_data        
