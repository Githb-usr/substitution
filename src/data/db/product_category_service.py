#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.product_category import ProductCategory

class ProductCategoryService:
    """
        ProductCategoryService class
        To manage the relationship between the ProductCategory object and the MySQL database
    """

    def insert(self, product_category):
        """ Insert product_category data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("INSERT INTO products_categories(product_id, category_id) VALUES(%s, %s)")
        cursor.execute(query, (product_category.get_product_id(), product_category.get_category_id()))
        cnx.commit()

        cursor.close()
        cnx.close()
