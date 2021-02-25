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
        
    def insert(self, product):
        """ Insert substitute data in database """
        return self.service.insert(product)

    def get_all_products_of_category(self, category_id):
        """ Get all products of selected category """
        return self.service.get_all_products_of_category(category_id)
    
    def get_potential_substitutes_list(self, category_id, selected_product):
        """ Get substitutes of selected product """
        return self.service.get_potential_substitutes_list(category_id, selected_product)
