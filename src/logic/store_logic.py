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

    def get_all(self):
        """ Get all stores object """
        return self.service.get_stores()
        
    def get_id_per_name(self, name):
        """ Get store's id from name """
        return self.service.get_id_per_name(name)
