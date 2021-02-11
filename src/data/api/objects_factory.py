#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.api.data_cleaner import DataCleaner
from src.data.model.category import Category
from src.data.model.product import Product
from src.data.model.product_category import ProductCategory
from src.data.model.product_store import ProductStore
from src.data.model.store import Store
from src.logic.category_logic import CategoryLogic
from src.logic.store_logic import StoreLogic

class ObjectsFactory:
    """
        ObjectsFactory class
        To manage the creation of objects linked to the MySQL database
    """

    def __init__(self):
        """ Constructor """
        self.data_cleaner = DataCleaner()
        self.category_logic = CategoryLogic()
        self.store_logic = StoreLogic()
        self.product_object_list = []

    def create_product_object_list(self):
        """
            Create the product objects from the initial dictionary list
            :return: the product object list
            :rtype: list()
        """
        # Start downloading data from the Open Food facts API
        self.data_cleaner.create_products_dict_list()
        
        # Get clean data
        self.data_cleaner.extract_strings_field()
        
        # Get the list of all the products
        products_dict_list = self.data_cleaner.products_dict_list

        # Create the products objects
        for prod_dict in products_dict_list:
            for brand in self.data_cleaner.brand_of_products:
                if brand[0] == prod_dict['code']:
                            product = Product(
                                code = prod_dict['code'],
                                product_name = prod_dict['product_name'],
                                brand = brand[1],
                                nutriscore_grade = prod_dict['nutriscore_grade'].capitalize(),
                                nova_group = prod_dict['nova_group'],
                                product_url = prod_dict['url']
                                )
                            self.product_object_list.append(product)

        return self.product_object_list

    def create_category_object_list(self):
        """
            Create the category objects from the list of the categories of products
            :return: the category object list
            :rtype: list()
        """
        category_object_list = []

        # Get the list of all the categories
        categories_of_products_list = self.data_cleaner.clean_categories

        # Create the categories objects
        for product_cat in categories_of_products_list:
            category = Category(cat_name=product_cat)
            category_object_list.append(category)

        return category_object_list

    def create_product_category_object_list(self):
        """
            Create the product_category objects from product and category lists
            :return: the product_category object list
            :rtype: list()
        """
        product_category_object_list = []

        # Get the list of categories associated with the id of each product
        products_categories = self.data_cleaner.cats_of_products
        
        # Get the list of all the categories objects
        categories_object = self.category_logic.get_all()

        # Create the product_category objects
        for prod_cat in products_categories:
            for cat in prod_cat[1]:
                for category_objet in categories_object:
                    if cat == category_objet.get_designation():
                        product_category = ProductCategory(prod_cat[0], category_objet.get_id())
                        product_category_object_list.append(product_category)

        return product_category_object_list

    def create_store_object_list(self):
        """
            Create the store objects from the list of the stores of products
            :return: the store object list
            :rtype: list()
        """
        store_object_list = []

        # Get the list of all the stores
        stores_of_products_list = self.data_cleaner.clean_stores

        # Create the stores objects
        for product_sto in stores_of_products_list:
            store = Store(store_name=product_sto)
            store_object_list.append(store)

        return store_object_list

    def create_product_store_object_list(self):
        """
            Create the product_store object from products and stores lists
            :return: the product_store object list
            :rtype: list()
        """
        product_store_object_list = []

        # Get the list of stores associated with the id of each product
        products_stores = self.data_cleaner.stores_of_products
        
        # Get the list of all the stores objects
        stores_objects = self.store_logic.get_all()

        # Create the product_store objects
        for prod_store in products_stores:
            for store in prod_store[1]:
                for store_objet in stores_objects:
                    if store == store_objet.get_designation():
                        product_store = ProductStore(prod_store[0], store_objet.get_id())
                        product_store_object_list.append(product_store)

        return product_store_object_list
