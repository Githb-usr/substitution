#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.substitute import Substitute

class SubstituteService:
    """
        SubstituteService class
        To manage the relationship between the Substitute object and the MySQL database
    """

    def insert(self, substitute):
        """ Insert substitute data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("INSERT INTO substitutes(initial_product_id, substitute_product_id) VALUES(%s, %s)")
        cursor.execute(query, (substitute.initial_product_id, substitute.substitute_product_id))
        cnx.commit()

        query = ("SELECT id from substitutes")
        cursor.execute(query)

        for sub_id in cursor:
            substitute.id = sub_id[0]

        cursor.close()
        cnx.close()

    def get_all(self):
        """ Get all Substitute object from database """
        substitutes = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = 'SELECT id, initial_product_id, substitute_product_id FROM substitutes'

        cursor.execute(query)

        for element in cursor:
            substitute = Substitute(element[0], element[1], element[2])
            substitutes.append(substitute)

        cursor.close()
        connector.close()

        return substitutes
