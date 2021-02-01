#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.category_service import CategoryService

class CategoryLogic:
    
    def __init__(self):
        """ Constructor """
        self.service = CategoryService()
    
    def get_categories(self):
        self.service.get_categories()
