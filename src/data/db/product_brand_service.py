#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.product_brand import ProductBrand

class ProductBrandService:
    """
        ProductBrandService class
        To manage the relationship between the ProductBrand object and the MySQL database
    """

    def insert(self, product_brand):
        """ Insert product_brand data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()
        
        query = ("INSERT INTO products_brands(product_id, brand_id) VALUES(%s, %s)")
        cursor.execute(query, (product_brand.product_id, product_brand.brand_id))
        cnx.commit()
        
        cursor.close()
        cnx.close()

    def get_products_brands(self):
        """ Get products_brands object from database """
        pass
