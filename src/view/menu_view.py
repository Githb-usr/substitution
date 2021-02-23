#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.view import category_view
from src.view import product_view
from src.view import substitute_view
from src.data.db.helpers import Helpers

from config.settings import MENU_LETTERS

class MenuView:
    """
        MenuView class
        To manage the interface menu
    """

    def display_column_menu(self):
        menu_str = "--------------------------------\nMENU \
            \nA : Remplacer un aliment \
            \nB : Mes aliments de remplacement \
            \nC : Réinitialiser l'application \
            \nD : Quitter l'application\n--------------------------------"

        print(menu_str)

    def select_menu(self):
        proceed = True

        while proceed:
            selected_menu = input("\nSélectionnez un code du menu puis validez avec \"Entrée\" : ").upper()

            if selected_menu not in MENU_LETTERS:
                print("\nVous n'avez pas saisi le code d'un menu, veuillez recommencer s'il vous plait.\n")
            else:
                if selected_menu == 'A':
                    self.replace_product()
                elif selected_menu == 'B':
                    self.see_substituted_products()
                elif selected_menu == 'C':
                    self.reset_database()
                elif selected_menu == 'D':
                    self.quit_application()

                proceed = False
                
    def display_menu(self):
        print("\n\nChoisissez un menu pour continuer.\r")        
        self.display_column_menu()
        self.select_menu()

    def replace_product(self):
        category = category_view.CategoryView()
        product = product_view.ProductView()
        
        selected_category = category.select_a_category()
        selected_product = product.select_product(selected_category)
        selected_substitute = product.select_substitute(selected_category.get_id(), selected_product)
        product.save_substitute(selected_product, selected_substitute)

    def see_substituted_products(self):
        substitute = substitute_view.SubstituteView()
        substitute.show_all_substitutes()

    def reset_database(self):
        reset = Helpers()
        proceed = True

        print("\nL'application va être réinitialisée. "
              "Etes-vous certain(e) de vouloir faire cela ? "
              "Cela va effacer tous les produits et tous les substituts enregistrés.")

        while proceed:
            warning = input("\nTapez 'O' pour continuer et réinitialiser l'application ou 'M' pour revenir au menu : \n")
            if warning.upper() == 'O' or warning == str(0):
                proceed = False
                print("Cela va prendre quelques minutes, merci de bien vouloir patienter.")
                reset.empty_database()
                reset.populate_database()
                print("\nLa réinitialisation est terminée, vous pouvez à nouveau utiliser l'application.\n")
                self.display_menu()
            elif warning.upper() == 'M':
                proceed = False
                self.display_menu()
            else:
                print("Vous n'avez pas saisi l'une des lettres proposées, "
                        "veuillez recommencer s'il vous plait.\n")

    def quit_application(self):
        proceed = True

        print("\nEtes-vous certain(e) de vouloir fermer l'application ?")
        while proceed:
            warning = input("\nTapez 'O' pour continuer et fermer ou 'M' pour revenir au menu : \n")
            if warning.upper() == 'O' or warning == str(0):
                proceed = False
                print("\nL'application \"Substitution\" va être fermée. Merci de l'avoir utilisé, et à bientôt !\n")
                sys.exit(0)
            elif warning.upper() == 'M':
                proceed = False
                self.display_menu()
            else:
                print("Vous n'avez pas saisi l'une des lettres proposées, "
                        "veuillez recommencer s'il vous plait.\n")
