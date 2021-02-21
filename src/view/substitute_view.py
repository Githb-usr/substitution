#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
                if i % 2 != 0:
                    print(f'SUBSTITUT {j}')
                    print('_______________________________________________________________________________________________________________________________________________________________________________________________________')
                    print(f'| S : {substitute.get_name()[0:41]!s:<43} | {substitute.get_brand()[0:17]!s:<17} | {substitute.get_nutriscore()!s:<1} | {substitute.get_novascore()!s:<1} | {substitute.get_url()!s:<118}|')
                    print('|-------------------------------------------------|-------------------|---|---|-----------------------------------------------------------------------------------------------------------------------|')
                    i = i + 1
                else:
                    print(f'| P : {substitute.get_name()[0:41]!s:<43} | {substitute.get_brand()[0:17]!s:<17} | {substitute.get_nutriscore()!s:<1} | {substitute.get_novascore()!s:<1} | {substitute.get_url()!s:<118}|')
                    print('|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|')
                    print(f'| Substitut (S) ou Produit remplacé (P) | Marque | Nutriscore | Novascore | Lien vers la fiche produit                                                                                                |')
                    print('|_____________________________________________________________________________________________________________________________________________________________________________________________________|\n')                
                    
                    i = i + 1
                    j = j + 1

        # The menu is displayed to continue
        self.menu.display_menu()

        return substitutes
