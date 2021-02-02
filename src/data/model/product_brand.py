#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ProductBrand:
    """
        ProductBrand class
        To manage ProductBrand object
    """

    def __init__(self, product_id, brand_id):
        """ Constructor """
        self.product_id = product_id
        self.brand_id = brand_id

    def get_product_id(self):
        """ Get ProductBrand() product_id """
        return self.product_id

    def get_brand_id(self):
        """ Get ProductBrand() brand_id """
        return self.brand_id
