#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.product_service import ProductService

class ProductLogic:
    
    def __init__(self):
        """ Constructor """
        self.service = ProductService()
    
    def get_products(self):
        self.service.get_products()
