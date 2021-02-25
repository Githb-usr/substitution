#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.category_service import CategoryService

class CategoryLogic:
    """
        CategoryLogic class
        To manage the Category object in the application
    """
    def __init__(self):
        """ Constructor """
        self.service = CategoryService()
        
    def insert(self, category):
        """ Insert substitute data in database """
        return self.service.insert(category)
        
    def get_all(self):
        """ Get all categories object """
        return self.service.get_all()
    
    def get_categories_to_select(self):
        """ Get categories to select """
        return self.service.get_categories_to_select()
