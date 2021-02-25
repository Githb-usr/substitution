#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.product_store_service import ProductStoreService

class ProductStoreLogic:
    """
        ProductStoreLogic class
        To manage the ProductStore object in the application
    """
    def __init__(self):
        """ Constructor """
        self.service = ProductStoreService()
        
    def insert(self, product_store):
        """ Insert product_store data in database """
        return self.service.insert(product_store)
