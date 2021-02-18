#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector

class DatabaseService:
    """
        DatabaseService class
        To manage the emptying of the database
    """

    def empty_database(self):
        """ Delete all data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("DELETE FROM substitutes")
        cursor.execute(query)
        
        query = ("DELETE FROM products_stores")
        cursor.execute(query)
        
        query = ("DELETE FROM products_categories")
        cursor.execute(query)
        
        query = ("DELETE FROM stores")
        cursor.execute(query)
        
        query = ("DELETE FROM categories")
        cursor.execute(query)
        
        query = ("DELETE FROM products")
        cursor.execute(query)

        cursor.close()
        connector.close()
