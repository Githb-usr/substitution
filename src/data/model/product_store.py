#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ProductStore:
    """
        ProductStore class
        To manage ProductStore objects
    """
    
    def __init__(self, product_id, store_id):
        """ Constructor """
        self.product_id = product_id
        self.store_id = store_id
    
    def get_product_id(self):
        """ Get ProductStore() product_id """
        return self.product_id
    
    def get_store_id(self):
        """ Get ProductStore() store_id """
        return self.store_id
