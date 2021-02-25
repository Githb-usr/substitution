#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.view.menu_view import MenuView

class MainView:
    """
        MainView class
        To manage the application interface
    """
    def __init__(self):
        """ Constructor """
        self.menu = MenuView()

    def start_application(self):
        """ Display at application startup """
        print("\nBienvenue sur le programme ''Substitution'' !\r")
        print("Ce programme vous permet de trouver des aliments de substitution de meilleure qualité et meilleurs pour votre santé.\n")
        self.menu.display_menu()
