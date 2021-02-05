#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.view.brand_view import BrandView
from src.view.category_view import CategoryView
from src.view.product_view import ProductView
from src.view.store_view import StoreView
from src.view.substitute_view import SubstituteView

class MainView:
    """
        MainView class
        To manage the application interface
    """

    def __init__(self):
        """ Constructor """
        self.brand = BrandView()
        self.category = CategoryView()
        self.product = ProductView()
        self.store = StoreView()
        self.substitute = SubstituteView()
        
    # def show_categories(self):
    #     categories = self.logic.get_all()
    #     for category in categories:
    #         print("{0} - {1}".format(category.id, category.designation))
        
    #     print("Selectionner une catégorie en tapant son numéro : ")