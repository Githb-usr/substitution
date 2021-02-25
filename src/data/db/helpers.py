#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.api.objects_factory import ObjectsFactory
from src.logic.category_logic import CategoryLogic
from src.logic.database_logic import DatabaseLogic
from src.logic.product_logic import ProductLogic
from src.logic.product_category_logic import ProductCategoryLogic
from src.logic.product_store_logic import ProductStoreLogic
from src.logic.store_logic import StoreLogic

class Helpers:
    """
        Helpers class
        To manage the populating of the MySQL database
    """
    def __init__(self):
        """ Constructor """
        self.objects_factory = ObjectsFactory()

    def insert_products(self):
        """ The product data is inserted into the MySQL database. """
        logic = ProductLogic()
        
        try:
            # We create the list of product objects
            products = self.objects_factory.create_product_object_list()
            products = set(products)

            for product in products:
                logic.insert(product)
        except:
            print('Il y a eu un problème lors de la récupération des données, veuillez rééssayer')

    def insert_categories(self):
        """ The category data is inserted into the MySQL database. """
        logic = CategoryLogic()
        
        # We create the list of category objects
        categories = self.objects_factory.create_category_object_list()
        categories = set(categories)
        
        for category in categories:
            logic.insert(category)

    def insert_products_categories(self):
        """ The product_category data is inserted into the MySQL database. """
        logic = ProductCategoryLogic()
        
        # We create the list of product_category objects
        products_categories = self.objects_factory.create_product_category_object_list()
        products_categories = set(products_categories)

        for p_c in products_categories:
            logic.insert(p_c)

    def insert_stores(self):
        """ The category data is inserted into the MySQL database. """
        logic = StoreLogic()
        
        # We create the list of store objects
        stores = self.objects_factory.create_store_object_list()
        stores = set(stores)
        
        for store in stores:
            logic.insert(store)

    def insert_products_stores(self):
        """ The product_store data is inserted into the MySQL database. """
        logic = ProductStoreLogic()
        
        # We create the list of product_store objects
        products_stores = self.objects_factory.create_product_store_object_list()
        products_stores = set(products_stores)

        for p_c in products_stores:
            logic.insert(p_c)

    def populate_database(self):
        """ Populate the MySQL database in the right order """
        self.insert_products()
        self.insert_categories()
        self.insert_products_categories()
        self.insert_stores()
        self.insert_products_stores()
        
    def empty_database(self):
        """ Delete all data from the database """
        logic = DatabaseLogic()
        logic.empty_database()
