#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Category class """

class Category:
    """
        Category class
        To manage Category object
    """

    def __init__(self, cat_name):
        """ Constructor """
        self.id = None
        self.designation = cat_name

    def get_id(self):
        """ Get Category() id """
        return self.id

    def get_designation(self):
        """ Get Category() designation """
        return self.designation
