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

        for element in cursor:
            brand.id = element[0]

        cursor.close()
        cnx.close()

    def get_all(self):
        """ Get all brands object from database """
        brands = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = 'SELECT id, designation FROM brands'

        cursor.execute(query)

        for element in cursor:
            brand = Brand(id=element[0], brand_name=element[1])
            brands.append(brand)

        cursor.close()
        connector.close()

        return brands
    
    def get_id_per_name(self, name):
        """ Get brand's id from brand's name """
        brand_id = int()
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("SELECT id FROM brands WHERE designation = (%s)")
        cursor.execute(query, (name,))

        for element in cursor:
            brand_id = int(element[0])

        cursor.close()
        connector.close()

        return brand_id
