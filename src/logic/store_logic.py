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

    def get_stores(self):
        """ Get stores object """
        self.service.get_stores()
