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

    def get_categories(self):
        """ Get categories object """
        self.service.get_categories()
