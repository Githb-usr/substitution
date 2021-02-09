#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Settings file
    To manage application constants
"""

API_BASE_URL = "https://fr.openfoodfacts.org/cgi/search.pl"
PAGE_SIZE = 250
PAGE_NUMBER = 8
FIELDS_OF_PRODUCT = 'code,product_name,brands,categories,nutriscore_grade,nova_group,url,stores'
FIELDS_OF_PRODUCT_LIST = ('code', 'product_name', 'brands', 'categories', 'nutriscore_grade', 'nova_group', 'url', 'stores')
MINIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY = 25
MAXIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY = 75
