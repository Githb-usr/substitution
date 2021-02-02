#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.model.brand import Brand
from src.data.model.category import Category
from src.data.model.product import Product
from src.data.model.store import Store
from src.data.model.product_brand import ProductBrand
from src.data.model.product_category import ProductCategory
from src.data.model.product_store import ProductStore
from src.data.api.data_cleaner import DataCleaner

class ObjectsFactory:
    """
        ObjectsFactory class
        To manage the creation of objects linked to the MySQL database
    """

    def __init__(self):
        """ Constructor """
        self.data_cleaner = DataCleaner()
        self.product_object_list = []
        self.category_object_list = []
        self.brand_object_list = []
        self.store_object_list = []

    def create_product_object_list(self):
        """
            We create the product objects from the initial dictionary list
            :return: the product object list
            :rtype: list()
        """
        products_dict_list = self.data_cleaner.create_products_dict_list()

        for product in products_dict_list:
            product = Product(
                code = product['code'],
                product_name = product['product_name'],
                nutriscore_grade = product['nutriscore_grade'].capitalize(),
                nova_group = product['nova_group'],
                product_url = product['url']
                )
            self.product_object_list.append(product)

        return self.product_object_list

    def create_category_object_list(self):
        """
            We create the category objects from the list of the categories of products
            :return: the category object list
            :rtype: list()
        """
        categories_of_products_list = self.data_cleaner.create_categories_of_products_list()

        for product_cat in categories_of_products_list:
            category = Category(cat_name=product_cat)
            self.category_object_list.append(category)

        return self.category_object_list

    def create_brand_object_list(self):
        """
            We create the brand objects from the list of the brands of products
            :return: the brand object list
            :rtype: list()
        """
        brands_of_products_list = self.data_cleaner.create_brands_of_products_list()

        for product_brd in brands_of_products_list:
            brand = Brand(brand_name=product_brd)
            self.brand_object_list.append(brand)

        return self.brand_object_list

    def create_store_object_list(self):
        """
            We create the store objects from the list of the stores of products
            :return: the store object list
            :rtype: list()
        """
        stores_of_products_list = self.data_cleaner.create_stores_of_products_list()

        for product_sto in stores_of_products_list:
            store = Store(store_name=product_sto)
            self.store_object_list.append(store)

        return self.store_object_list

    def create_product_category_object_list(self):
        """
            We create the product_category objects from product and category lists
            :return: the product_category object list
            :rtype: list()
        """
        product_category_object_list = []

        for product in self.data_cleaner.products_dict_list:
            cat_list = list(self.data_cleaner.clean_fields(product['categories']))
            for category in cat_list:
                for cat in self.category_object_list:
                    if cat.designation == category:
                        prod_cat = ProductCategory(product['code'], cat.id)
                        product_category_object_list.append(prod_cat)

        return product_category_object_list

    def create_product_brand_object_list(self):
        """
            We create the product_brand objects from product and brands lists
            :return: the product_brand object list
            :rtype: list()
        """
        product_brand_object_list = []

        for product in self.data_cleaner.products_dict_list:
            brands_list = list(self.data_cleaner.clean_fields(product['brands']))
            for brand in brands_list:
                for brd in self.brand_object_list:
                    if brd.designation == brand:
                        prod_brand = ProductBrand(product['code'], brd.id)
                        product_brand_object_list.append(prod_brand)

        return product_brand_object_list

    def create_product_store_object_list(self):
        """
            We create the product_store objects from product and stores lists
            :return: the product_store object list
            :rtype: list()
        """
        product_store_object_list = []

        for product in self.data_cleaner.products_dict_list:
            stores_list = list(self.data_cleaner.clean_fields(product['stores']))
            for store in stores_list:
                for sto in self.store_object_list:
                    if sto.designation == store:
                        prod_store = ProductStore(product['code'], sto.id)
                        product_store_object_list.append(prod_store)

        return product_store_object_list
