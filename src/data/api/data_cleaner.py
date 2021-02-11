#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.api.open_food_api import OpenFoodApi

from config.settings import FIELDS_OF_PRODUCT_LIST

class DataCleaner:
    """
        DataCleaner class
        To manage data cleaning from the Open Food Facts API
    """

    def __init__(self):
        """ Constructor """
        self.products_dict_list = []
        self.clean_brands = []
        self.clean_categories = []
        self.clean_stores = []
        self.brand_of_products = []
        self.cats_of_products = []
        self.stores_of_products = []

    def create_products_dict_list(self):
        """
            Products are retrieved via the Open Food Facts API,
            but only those with all the required fields.
            :return: A list of dictionaries is obtained, one dictionary per product.
            :rtype: list()
        """
        complete_data = []

        off_api = OpenFoodApi()
        all_data = off_api.get_full_api_products()
        complete_data = [
            product for product in all_data
            if len(product) == len(FIELDS_OF_PRODUCT_LIST) and all(product.values())            
            ]

        for data in complete_data:
            self.products_dict_list.append(data)

        return self.products_dict_list

    def clean_fields(self, field_string):
        """
            The strings of the products_dict_list containing several values
            are transformed into a list
            after standardization of the spaces.
            :param field_string: string with several values separated by commas
            :return: A list of values is obtained instead of a string
            :rtype: list()
        """
        clean_field_list = []

        field_split = field_string.split(',')
        for value in field_split:
            value_strip = value.strip().capitalize()
            clean_field_list.append(value_strip)

        clean_field_list = list(set(clean_field_list))

        return clean_field_list

    def clean_brands_field(self, field_string):
        """
            Strings in the product brand field containing several values are transformed
            into strings containing a single value (the first one).
            :param field_string: string with several values separated by commas
            :return: A string with one brand only
            :rtype: string
        """
        clean_field_list = self.clean_fields(field_string)
        first_brand = clean_field_list[0].title()

        return first_brand
    
    def extract_strings_field(self):
        """
            xxx
            from the product stores retrieved via the Open Food Facts API.
        """
        for product in self.products_dict_list:
            product_clean_brand = self.clean_brands_field(product['brands'])
            self.brand_of_products.append((product['code'], product_clean_brand))
            if product_clean_brand != '':
                self.clean_brands.append(product_clean_brand)
            self.clean_brands = list(set(self.clean_brands))
            
            product_clean_categories = self.clean_fields(product['categories'])
            self.cats_of_products.append((product['code'], product_clean_categories))
            for category in product_clean_categories:
                if category != '':
                    self.clean_categories.append(category)
                self.clean_categories = list(set(self.clean_categories))
            
            product_clean_stores = self.clean_fields(product['stores'])
            self.stores_of_products.append((product['code'], product_clean_stores))
            for store in product_clean_stores:
                if store != '':
                    self.clean_stores.append(store)
                self.clean_stores = list(set(self.clean_stores))
