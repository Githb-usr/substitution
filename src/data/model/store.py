#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Store:
    """
        Store class
        To manage Store object
    """

    def __init__(self, store_name):
        """ Constructor """
        self.id = None
        self.designation = store_name

    def get_id(self):
        """ Get Store() id """
        return self.id

    def get_designation(self):
        """ Get Store() designation """
        return self.designation
