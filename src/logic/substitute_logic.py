#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.substitute_service import SubstituteService

class SubstituteLogic:
    """
        SubstituteLogic class
        To manage the Substitute object in the application
    """

    def __init__(self):
        """ Constructor """
        self.service = SubstituteService()

    def insert(self, substitute):
        """ Insert substitute data in database """
        return self.service.insert(substitute)
    
    def get_all(self):
        """ Get all substitutes objects """
        return self.service.get_all()
