#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.api.data_cleaner import DataCleaner
from src.data.api.objects_factory import ObjectsFactory
from src.data.db.brand_service import BrandService
from src.data.db.category_service import CategoryService
from src.data.db.product_service import ProductService
from src.data.db.store_service import StoreService
from src.data.db.product_category_service import ProductCategoryService
from src.data.db.product_brand_service import ProductBrandService
from src.data.db.product_store_service import ProductStoreService

class Helpers:
    """
        Helpers class
        To manage the populating of the MySQL database
    """
    
    def __init__(self):
        """ Constructor """
        self.data_cleaner = DataCleaner()
        self.objects_factory = ObjectsFactory()
    
    def insert_products(self):
        """ The product data is inserted into the MySQL database. """
        service = ProductService()
        products = self.objects_factory.create_product_object_list()
        products = set(products)

        for product in products:
            service.insert(product)
    
    def insert_categories(self):
        """ The category data is inserted into the MySQL database. """
        service = CategoryService()
        categories = self.objects_factory.create_category_object_list()
        categories = set(categories)

        for category in categories:
            service.insert(category)

    def insert_brands(self):
        """ The category data is inserted into the MySQL database. """
        service = BrandService()
        brands = self.objects_factory.create_brand_object_list()
        brands = set(brands)
        
        for brand in brands:
            service.insert(brand)

    def insert_stores(self):
        """ The category data is inserted into the MySQL database. """
        service = StoreService()
        stores = self.objects_factory.create_store_object_list()
        stores = set(stores)
        
        for store in stores:
            service.insert(store)
    
    def insert_products_categories(self):
        """ The product_category data is inserted into the MySQL database. """
        service = ProductCategoryService()
        products_categories = self.objects_factory.create_product_category_object_list()
        products_categories = set(products_categories)

        for p_c in products_categories:
            service.insert(p_c)
    
    def insert_products_brands(self):
        """ The product_brand data is inserted into the MySQL database. """
        service = ProductBrandService()
        products_brands = self.objects_factory.create_product_brand_object_list()
        products_brands = set(products_brands)
        
        for p_c in products_brands:
            service.insert(p_c)
    
    def insert_products_stores(self):
        """ The product_store data is inserted into the MySQL database. """
        service = ProductStoreService()
        products_stores = self.objects_factory.create_product_store_object_list()
        products_stores = set(products_stores)
        
        for p_c in products_stores:
            service.insert(p_c)
    
    def populate_database(self):
        """ We populate the MySQL database """
        self.insert_products()
        self.insert_categories()
        self.insert_brands()
        self.insert_stores()
        self.insert_products_categories()
        self.insert_products_brands()
        self.insert_products_stores()
