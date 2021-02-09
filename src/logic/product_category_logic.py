#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.product_category_service import ProductCategoryService

class ProductCategoryLogic:
    """
        ProductCategoryLogic class
        To manage the ProductCategory object in the application
    """

    def __init__(self):
        """ Constructor """
        self.service = ProductCategoryService()
        
    def insert(self, product_category):
        """ Insert product_category data in database """
        return self.service.insert(product_category)
