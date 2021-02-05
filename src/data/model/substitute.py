#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Substitute class """

class Substitute:
    """
        Substitute class
        To manage Substitute object
    """

    def __init__(self, initial_product_id, substitute_product_id, id=None):
        """ Constructor with id attribute """
        self.id = id
        self.initial_product_id = initial_product_id
        self.substitute_product_id = substitute_product_id

    def get_id(self):
        """ Get Substitute id """
        return self.id

    def get_initial_product_id(self):
        """ Get Substitute initial_product_id """
        return self.initial_product_id

    def get_substitute_product_id(self):
        """ Get Substitute substitute_product_id """
        return self.substitute_product_id
