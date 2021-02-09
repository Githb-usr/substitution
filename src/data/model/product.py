#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Product class """

class Product:
    """
        Product class
        To manage Product object
    """

    def __init__(self, code, product_name, nutriscore_grade, nova_group, product_url, brand_name=None, brand_id=None):
        """ Constructor """
        self.id = code
        self.designation = product_name
        self.brand_name = brand_name
        self.nutriscore = nutriscore_grade
        self.novascore = nova_group
        self.url = product_url
        self.brand_id = brand_id

    def get_id(self):
        """ Get Product id """
        return self.id

    def get_designation(self):
        """ Get Product designation """
        return self.designation

    def get_brand_name(self):
        """ Get Product brand_name """
        return self.brand_name

    def get_nutriscore(self):
        """ Get Product nutriscore """
        return self.nutriscore

    def get_novascore(self):
        """ Get Product novascore """
        return self.novascore

    def get_url(self):
        """ Get Product url """
        return self.url

    def get_brand_id(self):
        """ Get Product brand_id """
        return self.brand_id
