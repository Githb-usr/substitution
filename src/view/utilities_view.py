#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UtilitiesView:
    """
        UtilitiesView class
        Useful functions in the application interface
    """

    def display_line_menu(self):
        menu_str = '------\nMENU : 1 : Remplacer un aliment | 2 : Aliments substitués | 3 : Quitter\n------'

        return print(menu_str)

    def press_enter(self):
        internal_proceed = True
        empty_string = input('Appuyez sur "Entrée" pour continuer.')

        while internal_proceed:
            if empty_string != '':
                empty_string = input('Appuyez sur "Entrée" pour continuer (ou bien un code du menu).')
            else:
                internal_proceed = False
