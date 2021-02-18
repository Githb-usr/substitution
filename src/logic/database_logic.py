#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.database_service import DatabaseService

class DatabaseLogic:
    """
        DatabaseLogic class
        To manage the Database object in the application
    """

    def __init__(self):
        """ Constructor """
        self.service = DatabaseService()
        
    def empty_database(self):
        """ Delete all data in database """
        return self.service.empty_database()