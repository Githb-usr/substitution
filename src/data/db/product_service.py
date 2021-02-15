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
                                    brand,
                                    nutriscore,
                                    novascore,
                                    url_
                                    )
                    VALUES(%s, %s, %s, %s, %s, %s)'''
                )

        cursor.execute(query, (
                        product.id,
                        product.designation,
                        product.brand,
                        product.nutriscore,
                        product.novascore,
                        product.url
                        )
                       )
        cnx.commit()

        cursor.close()
        connector.close()
        
    def get_all(self):
        """ Get all products object from database """
        products = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = (
                "SELECT id, designation, brand, nutriscore, novascore, url_ \
                FROM products p"
            )
        cursor.execute(query)

        for element in cursor:
            product = Product(
                code=element[0],
                product_name=element[1],
                brande=element[2],
                nutriscore_grade=element[3],
                nova_group=element[4], 
                product_url=element[5]
                )
            products.append(product)

        cursor.close()
        connector.close()

        return products
    
    def get_all_products_of_category(self, category_id):
        """ Get all products object for a single category from database """
        products = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = ("SELECT id, designation, brand, nutriscore, novascore, url_ \
                FROM products p \
                INNER JOIN products_categories pc \
                ON pc.product_id = p.id \
                WHERE pc.category_id = (%s) \
                ORDER BY p.designation ASC"
        )
        cursor.execute(query, (category_id,))

        for element in cursor:
            product = Product(
                code=element[0],
                product_name=element[1],
                brand=element[2],
                nutriscore_grade=element[3],
                nova_group=element[4], 
                product_url=element[5]
                )
            products.append(product)

        cursor.close()
        connector.close()

        return products
    
    def get_potential_substitutes_list(self, category_id, selected_product):
        """ We are looking for a better product than the one selected from database """
        products = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()
        
        query = ("SELECT DISTINCT id, designation, brand, nutriscore, novascore, url_ \
                FROM products p \
                INNER JOIN products_categories pc \
                ON pc.product_id = p.id \
                WHERE pc.category_id = (%s) \
                AND p.nutriscore < (%s) \
                AND p.novascore <= (%s) \
                ORDER BY p.nutriscore DESC, p.novascore DESC"
        )
        cursor.execute(query, (category_id, selected_product.get_nutriscore(),selected_product.get_novascore()))

        for element in cursor:
            product = Product(
                code=element[0],
                product_name=element[1],
                brand=element[2],
                nutriscore_grade=element[3],
                nova_group=element[4], 
                product_url=element[5]
                )
            products.append(product)

        cursor.close()
        connector.close()

        return products
