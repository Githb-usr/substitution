#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.product_service import ProductService

class ProductLogic:
    """
        ProductLogic class
        To manage the Product object in the application
    """

    def __init__(self):
        """ Constructor """
        self.service = ProductService()

    def get_products(self):
        """ Get products object """
        self.service.get_products()
