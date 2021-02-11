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

        cursor.close()
        cnx.close()
