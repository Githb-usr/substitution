#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.category import Category

from config.settings import MINIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY, MAXIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY

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
        cursor.execute(query, (category.get_designation(),))
        cnx.commit()

        cursor.close()
        cnx.close()
        
    def get_all(self):
        """ Get all categories object from database """
        categories = []
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("SELECT id, designation FROM categories")
        cursor.execute(query)

        for element in cursor:
            category = Category(id=element[0], cat_name=element[1])
            categories.append(category)

        cursor.close()
        connector.close()

        return categories
    
    def get_categories_to_select(self):
        """ Get categories to select from database """
        categories = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("SELECT DISTINCT id, designation \
                FROM categories c \
                INNER JOIN products_categories pc \
                ON pc.category_id = c.id \
                WHERE ( \
                    SELECT COUNT(product_id) \
                    FROM products_categories pc \
                    WHERE pc.category_id = c.id \
                    ) > (%s) \
                AND ( \
                    SELECT COUNT(product_id) \
                    FROM products_categories pc \
                    WHERE pc.category_id = c.id \
                    ) < (%s) \
                AND ( \
                    SELECT LENGTH(c.designation) < 31 \
                    ) \
                ORDER BY c.designation ASC"
        )
        cursor.execute(query, (MINIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY, MAXIMUM_NUMBER_OF_PRODUCTS_PER_CATEGORY))

        for element in cursor:
            category = Category(id=element[0], cat_name=element[1])
            categories.append(category)

        cursor.close()
        connector.close()

        return categories
