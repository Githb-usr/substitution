#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.logic.store_logic import StoreLogic

class StoreView:
    """
        StoreView class
        To manage the display of stores in the application interface
    """
    
    def __init__(self):
        """ Constructor """
        self.logic = StoreLogic()
        
    def show_stores(self):
        stores = self.logic.get_all()
        for store in stores:
            print("{0} - {1}".format(store.id, store.designation))
        
        print("Selectionner un magasin en tapant son numéro : ")
