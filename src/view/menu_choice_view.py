#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.view.category_view import CategoryView
from src.view.product_view import ProductView

class MenuChoiceView:
    """
        MenuChoiceView class
        To manage menu choices
    """

    def __init__(self):
        """ Constructor """
        self.category = CategoryView()
        self.product = ProductView()

    def replace_product(self):
        selected_category = self.category.select_a_category()
        selected_product = self.product.select_product(selected_category)
        show_substitutes = self.product.show_substitutes(selected_category.get_id(), selected_product)
        selected_substitute = self.product.select_substitute(selected_category.get_id(), selected_product)
        self.product.save_substitute(selected_product, selected_substitute)

    def see_substituted_products(self):
        pass

    def quit_application(self):
        print("\nLe programme \"Substitution\" va être fermé. Merci de l'avoir utilisé, et à bientôt !\n")
        sys.exit(0)