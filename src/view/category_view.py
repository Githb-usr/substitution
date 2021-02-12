#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.model.category import Category
from src.logic.category_logic import CategoryLogic
from src.view import menu_view
from src.view.utilities_view import UtilitiesView

class CategoryView:
    """
        CategoryView class
        To manage the display of categories in the application interface
    """

    def __init__(self):
        """ Constructor """
        self.logic = CategoryLogic()
        # self.menu = MenuView()
        self.codes = []

    def show_categories_to_select(self):
        categories = self.logic.get_categories_to_select()
        i = 0  
             
        print(f"\n{'N°':>4} - {'Catégorie'}")
        print("----------------------------------")
        while i < len(categories):
            if i + 1 < len(categories):
                if i + 2 < len(categories):
                    print(
                        f'{i+1!s:>2} - {categories[i].designation[0:29]!s:<29} \
                        {i+2!s:>2} - {categories[i+1].designation[0:29]!s:<29} \
                        {i+3!s:>2} - {categories[i+2].designation[0:29]!s}\r'
                        )
                    self.codes.append((i+1, categories[i].id))
                    self.codes.append((i+2, categories[i+1].id))
                    self.codes.append((i+3, categories[i+2].id))
                    i = i + 3
                else:
                    print(
                        f'{i+1!s:>2} - {categories[i].designation[0:29]!s:<29} \
                        {i+2!s:>2} - {categories[i+1].designation[0:29]!s:<29}\r'
                        )
                    self.codes.append((i+1, categories[i].id))
                    self.codes.append((i+2, categories[i+1].id))
                    i = i + 2
            else:
                print(
                        f'{i+1!s:>2} - {categories[i].designation[0:29]!s:<29}\r'
                        )
                self.codes.append((i+1, categories[i].id))
                i = i + 1
                
        print("----------------------------------")
        print(f"{'N°':>4} - {'Catégorie'}\n")
        
        return categories

    def select_a_category(self):
        categories_set = set()
        selected_category = ()
        proceed = True

        categories = self.show_categories_to_select()
        number_of_categories = len(categories)

        while proceed:
            UtilitiesView.display_line_menu()
            selected_menu = input("\nSelectionner une catégorie en tapant son numéro "
                                    "(ou bien taper une lettre du menu) : ")

            if selected_menu.upper() in ['A', 'B', 'C']:
                menu_view.MenuView.action_from_choice(selected_menu.upper())
                proceed = False
            elif selected_menu.isnumeric() == False or int(selected_menu) not in range(1, number_of_categories + 1):
                print("Vous n'avez pas saisi le numéro d'une des catégories proposées, "
                      "veuillez recommencer s'il vous plait.\n")
            else:
                for code in self.codes:
                    if code[0] == int(selected_menu):
                        for category in categories:
                            if code[1] == category.get_id():
                                selected_category = category
                                break
                        
                proceed = False

        return selected_category
