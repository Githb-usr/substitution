#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.logic.category_logic import CategoryLogic

class CategoryView:
    """
        CategoryView class
        To manage the display of categories in the application interface
    """

    def __init__(self):
        """ Constructor """
        self.logic = CategoryLogic()

    def show_categories_to_select(self):
        categories = self.logic.get_categories_to_select()
        i = 0
        
        print('\n')
        print(f"{'N°':>4} - {'Catégorie'}")
        print("----------------------------------")
        while i < len(categories):
            if i + 1 < len(categories):
                if i + 2 < len(categories):
                    print(
                        f'{categories[i].id!s:>4} - {categories[i].designation[0:29]!s:<29} \
                        {categories[i+1].id!s:>4} - {categories[i+1].designation[0:29]!s:<29} \
                        {categories[i+2].id!s:>4} - {categories[i+2].designation[0:29]!s} \r'
                        )
                    i = i + 3
                else:
                    print(
                        f'{categories[i].id!s:>4} - {categories[i].designation[0:29]!s:<29} \
                        {categories[i+1].id!s:>4} - {categories[i+1].designation[0:29]!s:<29} \r'
                        )
                    i = i + 2
            else:
                print(
                        f'{categories[i].id!s:>4} - {categories[i].designation[0:29]!s:<29} \r'
                        )
                i = i + 1
            
        return categories

    def select_a_category(self):
        categories_set = set()
        selected_category = ()
        id_list = []
        proceed = True

        categories = self.show_categories_to_select()
        for category in categories:
            id_list.append(category.id)
            categories_set.add((category.id, category.designation))

        while proceed:
            category_name = ''
            print('\n')
            select_string = input("Selectionner une catégorie en tapant son numéro : ")

            if select_string.isnumeric() == False or int(select_string) not in id_list:
                print("Vous n'avez pas saisi le numéro d'une des catégories proposées, veuillez recommencer s'il vous plait.")
            else:
                for category in categories_set:
                    if category[0] == int(select_string):
                        category_name = category[1]
                        break
                selected_category = (int(select_string), category_name)
                print("Merci !")
                print('Vous avez choisi la catégorie "{}" (catégorie n° {}).'.format(category_name, select_string))
                proceed = False

        return selected_category
