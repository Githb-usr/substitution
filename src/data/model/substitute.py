#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Substitute class """

class Substitute:
    """
        Substitute class
        To manage Substitute object
    """

    def __init__(self,
                 initial_product_id,
                 substituted_product_id,
                 id=None,
                 name=None, 
                 brand=None,
                 nutriscore=None,
                 novascore=None,
                 url=None
                 ):
        """ Constructor """
        self.id = id
        self.initial_product_id = initial_product_id
        self.substituted_product_id = substituted_product_id
        self.name = name
        self.brand = brand
        self.nutriscore = nutriscore
        self.novascore = novascore
        self.url = url

    def get_id(self):
        """ Get Substitute id """
        return self.id

    def get_initial_product_id(self):
        """ Get Substitute initial product's id """
        return self.initial_product_id

    def get_substituted_product_id(self):
        """ Get Substitute substituted product's id """
        return self.substituted_product_id
    
    def get_name(self):
        """ Get Substitute's name """
        return self.name
    
    def get_brand(self):
        """ Get Substitute's brand """
        return self.brand
    
    def get_nutriscore(self):
        """ Get Substitute's nutriscore """
        return self.nutriscore
    
    def get_novascore(self):
        """ Get Substitute's novascore """
        return self.novascore
    
    def get_url(self):
        """ Get Substitute's url """
        return self.url
