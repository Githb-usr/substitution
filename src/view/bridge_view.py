#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.view import menu_view
from src.view.utilities_view import UtilitiesView

class BridgeView:
    """
        BridgeView class
        To manage the transition between two searches
    """

    def make_transition(self):
        proceed = True

        print("\nVotre recherche d'aliment de substitution est terminée.\r")
        selected_menu = input("\nTapez une lettre du menu pour faire une nouvelle recherche, "
              "voir vos aliments de substitution ou quittere.\r")
        UtilitiesView.display_line_menu()

        while proceed:
            if selected_menu.upper() in ('A', 'B', 'C'):
                menu_view.MenuView.action_from_choice(selected_menu.upper())
            else:
                print("\nVous n'avez pas saisi le numéro d'un des produits proposées, "
                    "veuillez recommencer s'il vous plait.\n")

            proceed = False 
