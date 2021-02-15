#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.view import category_view
from src.view import product_view
from src.view import substitute_view

from config.settings import MENU_LETTERS

class MenuView:
    """
        MenuView class
        To manage the main interface menu
    """

    @staticmethod
    def display_column_menu():
        menu_str = "--------------------------------\nMENU : \
            \nA : Remplacer un aliment \
            \nB : Mes aliments de remplacement \
            \nC : Quitter\n--------------------------------"

        print(menu_str)
        
    @staticmethod
    def display_line_menu():
        menu_str = '-------------------------------------------------------------------------------- \
            \nMENU : A : Remplacer un aliment | B : Mes aliments de remplacement | C : Quitter \
            \n--------------------------------------------------------------------------------'

        return print(menu_str)

    @staticmethod
    def select_menu():
        proceed = True

        while proceed:
            selected_string = input("\nSélectionner un code du menu puis valider avec \"Entrée\" : ").upper()

            if selected_string not in MENU_LETTERS:
                print("\nVous n'avez pas saisi le code d'un menu, veuillez recommencer s'il vous plait.\n")
            else:
                MenuView.action_from_choice(selected_string)

                proceed = False
    
    @staticmethod          
    def action_from_choice(selected_menu):
        if selected_menu == 'A':
            MenuView.replace_product()
        elif selected_menu == 'B':
            MenuView.see_substituted_products()
        elif selected_menu == 'C':
            MenuView.quit_application()

    @staticmethod
    def replace_product():
        category = category_view.CategoryView()
        product = product_view.ProductView()
        
        selected_category = category.select_a_category()
        selected_product = product.select_product(selected_category)
        selected_substitute = product.select_substitute(selected_category.get_id(), selected_product)
        product.save_substitute(selected_product, selected_substitute)

    @staticmethod
    def see_substituted_products():
        substitute = substitute_view.SubstituteView()
        substitute.show_all_substitutes()

    @staticmethod
    def quit_application():
        print("\nLe programme \"Substitution\" va être fermé. Merci de l'avoir utilisé, et à bientôt !\n")
        sys.exit(0)

    @staticmethod
    def make_transition():
        print("\n\nChoisissez un menu pour continuer.\r")        
        MenuView.display_line_menu()
        MenuView.select_menu()
