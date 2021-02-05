#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.logic.product_logic import ProductLogic

class CategoryView:
    """
        ProductView class
        To manage the display of products in the application interface
    """
    
    def __init__(self):
        """ Constructor """
        self.logic = ProductLogic()
        
    def show_categories(self):
        products = self.logic.get_all()
        for product in products:
            print("{0} - {1}".format(product.id, product.designation))
        
        print("Selectionner un produit en tapant son numéro : ")
