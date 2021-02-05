#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.brand import Brand

class BrandService:
    """
        BrandService class
        To manage the relationship between the Brand object and the MySQL database
    """

    def insert(self, brand):
        """ Insert brand data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("INSERT INTO brands(designation) VALUES(%s)")
        cursor.execute(query, (brand.designation,))
        cnx.commit()

        query = ("SELECT id from brands")
        cursor.execute(query)

        for brand_id in cursor:
            brand.id = brand_id[0]

        cursor.close()
        cnx.close()

    def get_all(self):
        """ Get all brands object from database """
        brands = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = 'SELECT designation FROM brands'

        cursor.execute(query)

        for brand in cursor:
            brand = Brand('designation')
            brands.append(brand)

        cursor.close()
        connector.close()

        return brands
