#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.logic.substitute_logic import SubstituteLogic

class SubstituteView:
    """
        SubstituteView class
        To manage the display of substitutes in the application interface
    """
    
    def __init__(self):
        """ Constructor """
        self.logic = SubstituteLogic()
        
    def show_substitutes(self):
        substitutes = self.logic.get_all()
        for substitute in substitutes:
            print("{0} - {1}".format(substitute.id, substitute.initial_product_id, substitute.substitute_product_id))
        
        print("Selectionner un produit de substitution en tapant son numéro : ")
