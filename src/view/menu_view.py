#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.view import bridge_view
from src.view import category_view
from src.view import product_view
from src.view.utilities_view import UtilitiesView

class MenuView:
    """
        MenuView class
        To manage the main interface menu
    """
    def __init__(self):
        """ Constructor """
        self.category = category_view.CategoryView()
        self.product = product_view.ProductView()

    def display_column_menu(self):
        menu_str = "------\nMENU : \
            \nA : Remplacer un aliment \
            \nB : Mes aliments de remplacement \
            \nC : Quitter\n------"

        print(menu_str)

    def select_menu(self):
        proceed = True
        menus = ['A', 'B', 'C']

        while proceed:
            selected_string = input("\nSelectionner un code du menu puis valider avec \"Entrée\" : ").upper()

            if selected_string not in menus:
                print("\nVous n'avez pas saisi le code d'un menu, veuillez recommencer s'il vous plait.\n")
                UtilitiesView.display_line_menu()
            else:
                self.action_from_choice(selected_string)

                proceed = False
                
    def action_from_choice(self, selected_menu):
        if selected_menu == 'A':
            self.replace_product()
        elif selected_menu == 'B':
            self.see_substituted_products()
        elif selected_menu == 'C':
            self.quit_application()

    def replace_product(self):
        selected_category = self.category.select_a_category()
        selected_product = self.product.select_product(selected_category)
        show_substitutes = self.product.show_substitutes(selected_category.get_id(), selected_product)
        selected_substitute = self.product.select_substitute(selected_category.get_id(), selected_product)
        self.product.save_substitute(selected_product, selected_substitute)

    def see_substituted_products(self):
        pass

    def quit_application(self):
        print("\nLe programme \"Substitution\" va être fermé. Merci de l'avoir utilisé, et à bientôt !\n")
        sys.exit(0)
