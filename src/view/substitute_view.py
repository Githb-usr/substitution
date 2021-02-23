#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.logic.store_logic import StoreLogic
from src.data.model.substitute import Substitute
from src.logic.substitute_logic import SubstituteLogic
from src.view import menu_view

from config.settings import MENU_LETTERS

class SubstituteView:
    """
        SubstituteView class
        To manage the display of substitutes in the application interface
    """

    def __init__(self):
        """ Constructor """
        self.menu = menu_view.MenuView()
        self.store_logic = StoreLogic()
        self.substitute_logic = SubstituteLogic()

    def show_all_substitutes(self):
        """
        We display substitutes and the products they replace
        """
        # Get the list of substitutes and replaced products
        substitutes = self.substitute_logic.get_all()
        i = 1
        j = 1

        if substitutes == []:
            print("\nIl n'y a aucun substitut enregistré pour le moment.")
            print("Pour enregistrer un substitut, choississez le menu 'A'.")
            # The menu is displayed to continue
            self.menu.display_menu()
        else:
            print('\nVoici, ci-dessous, la liste de tous les substituts enregistrés.')
            print('Ils sont affichés du plus ancien au plus récent, '
                  'les plus récemment enregistrés sont donc en bas de la liste.\n')

            for substitute in substitutes:
                stores_name = []
                
                if i % 2 != 0:
                    # Get list of stores of the substitute
                    stores = self.store_logic.get_stores_of_product(substitute.get_substituted_product_id())
                    for store in stores:
                        stores_name.append(store.get_designation().title())

                    stores_string = ', '.join(stores_name)
                    print(f'SUBSTITUT {j}')
                    print('_______________________________________________________________________________________________________________________________')
                    print(f'| S : {substitute.get_name()[0:41]!s:<43} | {substitute.get_brand()[0:17]!s:<17} | {substitute.get_nutriscore()!s:<1} | {substitute.get_novascore()!s:<1} | {stores_string!s:<46}|')
                    print('|     --------------------------------------------+-------------------+---+---+-----------------------------------------------|')
                    print(f'|     {substitute.get_url()!s:<120}|')
                    print('|-----------------------------------------------------------------------------------------------------------------------------|')
                    i = i + 1
                else:
                    # Get list of stores of the initial product
                    stores = self.store_logic.get_stores_of_product(substitute.get_initial_product_id())
                    for store in stores:
                        stores_name.append(store.get_designation().title())

                    stores_string = ', '.join(stores_name)
                    print(f'| P : {substitute.get_name()[0:41]!s:<43} | {substitute.get_brand()[0:17]!s:<17} | {substitute.get_nutriscore()!s:<1} | {substitute.get_novascore()!s:<1} | {stores_string!s:<46}|')
                    print('|     --------------------------------------------+-------------------+---+---+-----------------------------------------------|')
                    print(f'|     {substitute.get_url()!s:<120}|')
                    print('|-----------------------------------------------------------------------------------------------------------------------------|')
                    print(f'|     Substitut (S) ou Produit remplacé (P) | Marque | Nutriscore | Novascore | Magasins qui vendent le produit               |')
                    print(f'|     Lien vers la fiche produit                                                                                              |')
                    print('|_____________________________________________________________________________________________________________________________|\n')                
                    
                    i = i + 1
                    j = j + 1

        # The menu is displayed to continue
        self.menu.display_menu()

        return substitutes
