#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.category import Category

class CategoryService:
    """
        CategoryService class
        To manage the relationship between the Category object and the MySQL database
    """
    
    def insert(self, category):
        """ Insert category data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()
        
        query = ("INSERT INTO categories(designation) VALUES(%s)")
        cursor.execute(query, (category.designation,))
        cnx.commit()
        
        query = ("SELECT id from categories")
        cursor.execute(query)

        for cat_id in cursor:
            category.id = cat_id[0]
        
        cursor.close()
        cnx.close()

    def get_categories(self):
        """ Get categories object from database """
        categories = []
        
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = 'SELECT designation FROM categories'

        cursor.execute(query)
        
        for category in cursor:
            category = Category('designation')
            categories.append(category)
        
        cursor.close()
        connector.close()
        
        return categories
