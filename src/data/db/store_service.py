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

        query = ("SELECT id from stores")
        cursor.execute(query)

        for element in cursor:
            store.id = element[0]

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
    
    def get_id_per_name(self, name):
        """ Get store's id from store's name """
        store_id = int()
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("SELECT id FROM stores WHERE designation = (%s)")
        cursor.execute(query, (name,))

        for element in cursor:
            store_id = int(element[0])

        cursor.close()
        connector.close()

        return store_id
