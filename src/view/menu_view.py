#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.view.category_view import CategoryView
from src.view.product_view import ProductView
from src.view.utilities_view import UtilitiesView

class MenuView:
    """
        MenuView class
        To manage the main interface menu
    """
    
    def __init__(self):
        """ Constructor """
        self.category = CategoryView()
        self.product = ProductView()
        self.utilites = UtilitiesView()
    
    def display_column_menu(self):
        menu_str = "------\nMENU : \
            \n- Remplacer un aliment (Taper M1) \
            \n- Mes aliments substitués (Taper M2) \
            \n- Quitter (Taper M3)\n------"
        
        return print(menu_str)
    
    def select_menu(self):
        proceed = True
        menus = ['M1', 'M2', 'M3']

        while proceed:
            select_string = input("\nSelectionner un code du menu : ").upper()

            if select_string not in menus:
                print("\nVous n'avez pas saisi le code d'un menu, veuillez recommencer s'il vous plait.\n")
                self.utilites.display_line_menu()
            else:
                if select_string == 'M1':
                    self.replace_product()
                elif select_string == 'M2':
                    self.see_substituted_products()
                elif select_string == 'M3':
                    self.quit_application()
                
                proceed = False
    
    def replace_product(self):
        selected_category = self.category.select_a_category()
        selected_product = self.product.select_product(selected_category.get_id())
        show_substitutes = self.product.show_substitutes(selected_category.get_id(), selected_product)
        select_substitute = self.product.select_substitute(selected_category.get_id(), selected_product)

    def see_substituted_products(self):
        pass

    def quit_application(self):
        sys.exit(0)
