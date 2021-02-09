#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.view.brand_view import BrandView
from src.view.category_view import CategoryView
from src.view.menu_view import MenuView
from src.view.product_view import ProductView
from src.view.store_view import StoreView
from src.view.substitute_view import SubstituteView

class MainView:
    """
        MainView class
        To manage the application interface
    """

    def __init__(self):
        """ Constructor """
        self.brand = BrandView()
        self.category = CategoryView()
        self.menu = MenuView()
        self.product = ProductView()
        self.store = StoreView()
        self.substitute = SubstituteView()

    def start_program(self):
        print("\nBienvenue sur le programme ''Substitution'' !\r")
        print("Ce programme vous permet de trouver des aliments de substitution de meilleure qualité et meilleurs pour votre santé.\n")
        self.menu.display_column_menu()
        self.menu.select_menu()
