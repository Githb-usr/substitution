#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.db.connector import Connector
from src.data.model.product import Product

class ProductService:
    """
        ProductService class
        To manage the relationship between the Product object and the MySQL database
    """

    def insert(self, product):
        """ Insert product data in database """
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ('''INSERT INTO products(
                                    id,
                                    designation,
                                    nutriscore,
                                    novascore,
                                    url_
                                    )
                    VALUES(%s, %s, %s, %s, %s)'''
                )

        cursor.execute(query, (
                        product.id,
                        product.designation,
                        product.nutriscore,
                        product.novascore,
                        product.url
                        )
                       )
        cnx.commit()

        cursor.close()
        connector.close()

    def get_products(self):
        """ Get products object from database """
        products = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = 'SELECT id, designation, nutriscore, novascore, url_ FROM products'

        cursor.execute(query)

        for product in cursor:
            product = Product('id', 'designation', 'nutriscore', 'novascore', 'url_')
            products.append(product)

        cursor.close()
        connector.close()

        return products
