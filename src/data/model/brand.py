#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Brand:
    """
        Brand class
        To manage Brand object
    """

    def __init__(self, brand_name, id=None):
        """ Constructor """
        self.id = id
        self.designation = brand_name

    def get_id(self):
        """ Get Brand() id """
        return self.id

    def get_designation(self):
        """ Get Brand() designation """
        return self.designation
