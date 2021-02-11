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
