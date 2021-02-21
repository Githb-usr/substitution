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
        already_exist = self.check_if_already_registered(substitute)
        
        if already_exist == None:
            connector = Connector()
            cnx = connector.connection()
            cursor = cnx.cursor()
            
            query = ("INSERT INTO substitutes(initial_product_id, substituted_product_id) VALUES(%s, %s)")
            cursor.execute(query, (substitute.initial_product_id, substitute.substituted_product_id))
            cnx.commit()               

            cursor.close()
            cnx.close()
            
        return already_exist
        
    def check_if_already_registered(self, substitute):
        """ xxx """
        already_exist = None
        
        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()
        
        query = ("SELECT s.initial_product_id, s.substituted_product_id, \
                    p1.designation AS initial_product, p2.designation AS substituted_product \
                FROM substitutes AS s \
                INNER JOIN products AS p1, products AS p2 \
                WHERE initial_product_id = (%s) AND substituted_product_id = (%s) \
                    AND (p1.id = initial_product_id) AND (p2.id = substituted_product_id)")
        cursor.execute(query, (substitute.initial_product_id, substitute.substituted_product_id))
        
        for element in cursor:
            if element:
                already_exist = "\nAttention : ce produit de substitution {substituted_product} est déjà associé en base de données comme remplaçant du produit {initial_product}, il n\'a donc pas été enregistré.".format(substituted_product=element[2], initial_product=element[3])

        cursor.close()
        cnx.close()
        
        return already_exist

    def get_all(self):
        """ Get all susbtitutes objects from database """
        susbtitutes = []

        connector = Connector()
        cnx = connector.connection()
        cursor = cnx.cursor()

        query = (            
                "SELECT \
                sub.* \
                FROM ( \
                    SELECT \
                    s.id AS ID, \
                    s.initial_product_id, \
                    s.substituted_product_id, \
                    p.designation, \
                    p.brand, \
                    p.nutriscore, \
                    p.novascore, \
                    p.url_ \
                    FROM products p \
                    INNER JOIN substitutes s \
                    ON (s.substituted_product_id = p.id) \
                    UNION ALL \
                    SELECT \
                    s.id AS ID, \
                    s.initial_product_id, \
                    s.substituted_product_id, \
                    p.designation AS Produit, \
                    p.brand AS Marque, \
                    p.nutriscore AS Nutriscore, \
                    p.novascore AS Novascore, \
                    p.url_ AS Lien_vers_la_fiche_OFF \
                    FROM products p \
                    INNER JOIN substitutes s \
                    ON (s.initial_product_id = p.id) \
                    )sub \
                ORDER BY ID ASC"
            )
        cursor.execute(query)

        for element in cursor:
            susbtitute = Substitute(
                id=element[0],
                initial_product_id=element[1],
                substituted_product_id=element[2],
                name=element[3],
                brand=element[4],
                nutriscore=element[5],
                novascore=element[6], 
                url=element[7],
                )
            susbtitutes.append(susbtitute)

        cursor.close()
        connector.close()

        return susbtitutes
