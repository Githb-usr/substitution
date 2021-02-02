#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ProductCategory:
    """
        ProductCategory class
        To manage ProductCategory object
    """

    def __init__(self, product_id, category_id):
        """ Constructor """
        self.product_id = product_id
        self.category_id = category_id

    def get_product_id(self):
        """ Get ProductCategory() product_id """
        return self.product_id

    def get_category_id(self):
        """ Get ProductCategory() category_id """
        return self.category_id
