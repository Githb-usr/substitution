#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.store_service import StoreService

class StoreLogic:
    """
        StoreLogic class
        To manage the Store object in the application
    """
    def __init__(self):
        """ Constructor """
        self.service = StoreService()
        
    def insert(self, store):
        """ Insert store data in database """
        return self.service.insert(store)

    def get_all(self):
        """ Get all stores objects """
        return self.service.get_all()
    
    def get_stores_of_product(self, product_id):
        """ Get all the stores that sell a given product """
        return self.service.get_stores_of_product(product_id)
