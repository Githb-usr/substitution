#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.api.open_food_api import OpenFoodApi
from src.data.model.category import Category
from src.data.model.product import Product
from src.data.model.product_category import ProductCategory

from config.settings import FIELDS_OF_PRODUCT_LIST

class DataCleaner:
    """
        DataCleaner class
        To manage data cleaning from the Open Food Facts API
    """
    
    def __init__(self):
        """ Constructor """
        self.products_dict_list = []
    
    def create_products_dict_list(self):
        """
            Products are retrieved via the Open Food Facts API, but only those with all the required fields.
            :return: A list of dictionaries is obtained, one dictionary per product.
            :rtype: list()
        """
        off_api = OpenFoodApi()
        all_data = off_api.get_full_api_products()
        complete_data = []
        complete_data = [product for product in all_data if all(key in product for key in FIELDS_OF_PRODUCT_LIST)]
        
        for data in complete_data:
            self.products_dict_list.append(data)

        return self.products_dict_list

    def clean_fields(self, field_string):
        """
            The strings of the products_dict_list containing several values are transformed into a list
            after standardization of the spaces.
            :param field_string: string with several values separated by commas
            :return: A list of values is obtained instead of a string
            :rtype: list()
        """
        clean_field_list = []

        field_split = field_string.split(',')
        for value in field_split:
            value_strip = value.strip()
            clean_field_list.append(value_strip)
        
        clean_field_list = list(set(clean_field_list))
        
        return clean_field_list

    def create_categories_of_products_list(self):
        """
            The list of categories to be included in the database is created (after cleaning)
            from the product categories retrieved via the Open Food Facts API.
            :return: A list of categories is obtained, without duplicates
            :rtype: list()
        """
        categories_of_products_list = []

        for product in self.products_dict_list:
            clean_categories = self.clean_fields(product['categories'])
            for category in clean_categories:
                if category != '':
                    categories_of_products_list.append(category)
        
        categories_of_products_list = list(set(categories_of_products_list))
        
        return categories_of_products_list
    
    def create_brands_of_products_list(self):
        """
            The list of brands to be included in the database is created (after cleaning)
            from the product brands retrieved via the Open Food Facts API.
            :return: A list of brands is obtained, without duplicates
            :rtype: list()
        """
        brands_of_products_list = []
        
        for product in self.products_dict_list:
            clean_brands = self.clean_fields(product['brands'])
            for brand in clean_brands:
                if brand != '':
                    brands_of_products_list.append(brand)
        
        brands_of_products_list = list(set(brands_of_products_list))
        
        return brands_of_products_list
    
    def create_stores_of_products_list(self):
        """
            The list of stores to be included in the database is created (after cleaning)
            from the product stores retrieved via the Open Food Facts API.
            :return: A list of stores is obtained, without duplicates
            :rtype: list()
        """
        stores_of_products_list = []
        
        for product in self.products_dict_list:
            clean_stores = self.clean_fields(product['stores'])
            for store in clean_stores:
                if store != '':
                    stores_of_products_list.append(store)
        
        stores_of_products_list = list(set(stores_of_products_list))
        
        return stores_of_products_list
