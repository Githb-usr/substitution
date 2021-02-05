#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.brand_service import BrandService

class BrandLogic:
    """
        BrandLogic class
        To manage the Brand object in the application
    """

    def __init__(self):
        """ Constructor """
        self.service = BrandService()

    def get_all(self):
        """ Get all brands object """
        self.service.get_brands()
