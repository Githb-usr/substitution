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
        """ Get all stores object """
        return self.service.get_all()
