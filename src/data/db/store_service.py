#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.store import Store

class StoreService:
    """
        StoreService class
        To manage the relationship between the Store object and the MySQL database
    """

    def insert(self, store):
        """ Insert stores data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("INSERT INTO stores(designation) VALUES(%s)")
        cursor.execute(query, (store.designation,))
        cnx.commit()

        cursor.close()
        cnx.close()

    def get_all(self):
        """ Get all stores object from database """
        stores = []
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = 'SELECT id, designation FROM stores'
        cursor.execute(query)

        for element in cursor:
            store = Store(id=element[0], store_name=element[1])
            stores.append(store)

        cursor.close()
        connector.close()

        return stores
    
    def get_stores_of_product(self, product_id):
        """ Get all the stores that sell a given product """
        stores = []
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = (
            "SELECT id, designation \
            FROM stores AS s \
            INNER JOIN products_stores AS ps \
            ON ps.store_id = s.id \
            WHERE ps.product_id = (%s)"
        )
        cursor.execute(query, (product_id,))

        for element in cursor:
            store = Store(id=element[0], store_name=element[1])
            stores.append(store)

        cursor.close()
        connector.close()

        return stores
