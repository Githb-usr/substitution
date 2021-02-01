#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.store_service import StoreService

class StoreLogic:
    
    def __init__(self):
        """ Constructor """
        self.service = StoreService()
    
    def get_stores(self):
        self.service.get_stores()
