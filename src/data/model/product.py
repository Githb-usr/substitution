#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Product class """

class Product:
    """
        Product class
        To manage Product object
    """

    def __init__(self, code, product_name, nutriscore_grade, nova_group, product_url):
        """ Constructor """
        self.id = code
        self.designation = product_name
        self.nutriscore = nutriscore_grade
        self.novascore = nova_group
        self.url = product_url

    def get_id(self):
        """ Get Product() id """
        return self.id

    def get_designation(self):
        """ Get Product() designation """
        return self.designation

    def get_nutriscore(self):
        """ Get Product() nutriscore """
        return self.nutriscore

    def get_novascore(self):
        """ Get Product() novascore """
        return self.novascore

    def get_url(self):
        """ Get Product() url """
        return self.url
