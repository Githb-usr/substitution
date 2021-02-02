#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.product_store import ProductStore

class ProductStoreService:
    """
        ProductStoreService class
        To manage the relationship between the ProductStore object and the MySQL database
    """

    def insert(self, product_store):
        """ Insert product_store data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("INSERT INTO products_stores(product_id, store_id) VALUES(%s, %s)")
        cursor.execute(query, (product_store.product_id, product_store.store_id))
        cnx.commit()

        cursor.close()
        cnx.close()

    def get_products_stores(self):
        """ Get products_stores object from database """
        pass
