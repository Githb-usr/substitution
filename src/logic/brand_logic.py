#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.brand_service import BrandService

class BrandLogic:
    
    def __init__(self):
        """ Constructor """
        self.service = BrandService()
    
    def get_brands(self):
        self.service.get_brands()
