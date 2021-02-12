#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UtilitiesView:
    """
        UtilitiesView class
        Useful functions in the application interface
    """

    @staticmethod
    def display_line_menu():
        menu_str = '------\nMENU : A : Remplacer un aliment | B : Aliments de remplacement | C : Quitter\n------'

        return print(menu_str)
