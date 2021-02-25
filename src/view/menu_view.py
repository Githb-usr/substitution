#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.view import category_view
from src.view import product_view
from src.view import substitute_view
from src.data.db.helpers import Helpers

from config.settings import MENU_NUMBERS

class MenuView:
    """
        MenuView class
        To manage the interface menu
    """
    def display_column_menu(self):
        """ Display the menu """
        menu_str = "--------------------------------\nMENU \
            \n1 - Remplacer un aliment \
            \n2 - Mes aliments de remplacement \
            \n3 - Réinitialiser l'application \
            \n4 - Quitter l'application\n--------------------------------"

        print(menu_str)

    def select_menu(self):
        """ Interaction with the user to choose a menu and then redirect to the display corresponding to the user's choice """
        proceed = True

        while proceed:
            selected_menu = input("\nSélectionnez un chiffre du menu puis validez avec \"Entrée\" : ")

            if selected_menu.isalpha() or int(selected_menu) not in MENU_NUMBERS:
                print("\nVous n'avez pas saisi le chiffre d'un menu, veuillez recommencer s'il vous plait.\n")
            else:
                if int(selected_menu) == 1:
                    self.replace_product()
                elif int(selected_menu) == 2:
                    self.see_substituted_products()
                elif int(selected_menu) == 3:
                    self.reset_database()
                elif int(selected_menu) == 4:
                    self.quit_application()

                proceed = False
                
    def display_menu(self):
        """ Display the menu with the input field """
        print("\n\nChoisissez un chiffre du menu pour continuer.\r")        
        self.display_column_menu()
        self.select_menu()

    def replace_product(self):
        """ The entire sequence of interactions with the user to find a substitute for a given product """
        category = category_view.CategoryView()
        product = product_view.ProductView()
        
        selected_category = category.select_a_category()
        selected_product = product.select_product(selected_category)
        selected_substitute = product.select_substitute(selected_category.get_id(), selected_product)
        product.save_substitute(selected_product, selected_substitute)

    def see_substituted_products(self):
        """ Displays the list of all registered substitutes """
        substitute = substitute_view.SubstituteView()
        substitute.show_all_substitutes()

    def reset_database(self):
        """ Reset the database by deleting all data and downloading a new set of data via the API """
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
        """ Close the application """
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
