#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.model.brand import Brand
from src.data.model.category import Category
from src.data.model.product import Product
from src.data.model.store import Store
from src.data.model.product_category import ProductCategory
from src.data.model.product_store import ProductStore
from src.logic.brand_logic import BrandLogic
from src.logic.category_logic import CategoryLogic
from src.logic.product_logic import ProductLogic
from src.logic.store_logic import StoreLogic
from src.data.api.data_cleaner import DataCleaner


class ObjectsFactory:
    """
        ObjectsFactory class
        To manage the creation of objects linked to the MySQL database
    """

    def __init__(self):
        """ Constructor """
        self.data_cleaner = DataCleaner()
        self.brand_logic = BrandLogic()
        self.category_logic = CategoryLogic()
        self.product_logic = ProductLogic()
        self.store_logic = StoreLogic()
        self.brand_object_list = []
        self.product_object_list = []
        self.category_object_list = []
        self.store_object_list = []
        
    def create_brand_object_list(self):
        """
            We create the brand objects from the list of the brands of products
            :return: the brand object list
            :rtype: list()
        """
        # we get the list of all the brands
        self.data_cleaner.create_products_dict_list()
        self.data_cleaner.extract_strings_field()
        brands_of_products_list = self.data_cleaner.clean_brands

        # we create the Brand objects
        for product_brd in brands_of_products_list:
            brand = Brand(brand_name=product_brd)
            self.brand_object_list.append(brand)

        return self.brand_object_list

    def create_product_object_list(self):
        """
            We create the product objects from the initial dictionary list
            :return: the product object list
            :rtype: list()
        """
        # we get the list of all the products
        products_dict_list = self.data_cleaner.products_dict_list

        # we create the Product objects
        for prod_dict in products_dict_list:
            for brand in self.data_cleaner.brand_of_prod:
                if brand[0] == prod_dict['code']:
                    product = Product(
                        code = prod_dict['code'],
                        product_name = prod_dict['product_name'],
                        nutriscore_grade = prod_dict['nutriscore_grade'].capitalize(),
                        nova_group = prod_dict['nova_group'],
                        product_url = prod_dict['url'],
                        brand_name = brand[1],
                        brand_id = self.brand_logic.get_id_per_name(brand[1])
                        )
                    self.product_object_list.append(product)

        return self.product_object_list

    def create_category_object_list(self):
        """
            We create the category objects from the list of the categories of products
            :return: the category object list
            :rtype: list()
        """
        # we get the list of all the categories
        categories_of_products_list = self.data_cleaner.clean_categories

        # we create the Category objects
        for product_cat in categories_of_products_list:
            category = Category(cat_name=product_cat)
            self.category_object_list.append(category)

        return self.category_object_list
    
    def create_product_category_object_list(self):
        """
            We create the product_category objects from product and category lists
            :return: the product_category object list
            :rtype: list()
        """        
        # xxx
        cats_of_prod = self.data_cleaner.cats_of_prod
        product_category_object_list = []

        for cats_prod in cats_of_prod:
            for cat in cats_prod[1]:
                prod_cat = ProductCategory(cats_prod[0], self.category_logic.get_id_per_name(cat))
                product_category_object_list.append(prod_cat)

        return product_category_object_list

    def create_store_object_list(self):
        """
            We create the store objects from the list of the stores of products
            :return: the store object list
            :rtype: list()
        """
        # we get the list of all the stores
        stores_of_products_list = self.data_cleaner.clean_stores

        # we create the Store objects
        for product_sto in stores_of_products_list:
            store = Store(store_name=product_sto)
            self.store_object_list.append(store)

        return self.store_object_list

    def create_product_store_object_list(self):
        """
            We create the product_store objects from product and stores lists
            :return: the product_store object list
            :rtype: list()
        """
        # xxx
        stores_of_prod = self.data_cleaner.stores_of_prod
        product_store_object_list = []

        for sto_prod in stores_of_prod:
            for sto in sto_prod[1]:
                prod_store = ProductStore(sto_prod[0], self.store_logic.get_id_per_name(sto))
                product_store_object_list.append(prod_store)

        return product_store_object_list
