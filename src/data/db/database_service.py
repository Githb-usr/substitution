#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector

from config.settings import TABLES

class DatabaseService:
    """
        DatabaseService class
        To manage the emptying of the database
    """

    def empty_table(self, table):
        """ Delete all data in table """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("DELETE FROM " + table + ";")
        cursor.execute(query)
        cnx.commit()

        cursor.close()
        connector.close()

    def empty_database(self):
        """ Delete all data in database """
        for table in TABLES:
            self.empty_table(table)
