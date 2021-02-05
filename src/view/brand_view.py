#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.logic.brand_logic import BrandLogic

class BrandView:
    """
        BrandView class
        the display of brands in the application interface
    """
    
    def __init__(self):
        """ Constructor """
        self.logic = BrandLogic()
        
    def show_brands(self):
        brands = self.logic.get_all()
        for brand in brands:
            print("{0} - {1}".format(brand.id, brand.designation))
        
        print("Selectionner une marque en tapant son numéro : ")
