#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.model.product import Product
from src.data.model.substitute import Substitute
from src.logic.product_logic import ProductLogic
from src.logic.substitute_logic import SubstituteLogic
from src.view import menu_view

class ProductView:
    """
        ProductView class
        To manage the display of products in the application interface
    """
    
    def __init__(self):
        """ Constructor """
        self.menu = menu_view.MenuView()
        self.product_logic = ProductLogic()
        self.substitute_logic = SubstituteLogic()
        self.codes_prod__of_selected_category = []
        self.codes_sub_of_selected_product = []
        
    def show_products_of_selected_category(self, selected_category):
        try:
            products = self.product_logic.get_all_products_of_category(selected_category.get_id())
            
            i = 1
        
            print('\n')
            print('N° - Nom - Nutriscore - Novascore - Marque')
            print('-------------------------------------------------------------------------------------------------------------------------------')
            for product in products:
                self.codes_prod__of_selected_category.append((i, product.get_id()))
                print(
                    f'| {i!s:>2} - {product.get_designation()[0:80]!s:<82} | {product.get_nutriscore()} | {product.get_novascore()} | {product.get_brand()!s:<25} |'
                    )
                print('-------------------------------------------------------------------------------------------------------------------------------')

                i = i + 1

            print('N° - Nom - Nutriscore - Novascore - Marque\n')
            
            print("\nMerci !")
            print('Vous avez choisi la catégorie "{}".\r'.format(selected_category.get_designation()))
            
            return products

        except:
            print("Il y a eu un problème d'accès à la base de données. "
                  "Nous n'avons pas pu afficher les produits de la catégorie demandée.")
            self.menu.display_menu()
    
    def select_product(self, selected_category):
        selected_product = None
        proceed = True

        products_of_selected_category_list = self.show_products_of_selected_category(selected_category)
        number_of_products = len(products_of_selected_category_list)

        while proceed:
            selected_number = input("\nSélectionnez un produit en tapant son numéro "
                                    "(ou bien tapez 'M' pour revenir au menu) puis validez avec \"Entrée\" : ")

            if selected_number.upper() == 'M':
                proceed = False
                self.menu.display_menu()
            elif selected_number.isnumeric() == False or int(selected_number) not in range(1, number_of_products + 1):
                print("\nVous n'avez pas saisi l'un des choix proposés, veuillez recommencer s'il vous plait.\n")
            else:
                for code_prod in self.codes_prod__of_selected_category:
                    if code_prod[0] == int(selected_number):
                        for product in products_of_selected_category_list:
                            if code_prod[1] == product.get_id():
                                selected_product = product
                                break

                proceed = False

        return selected_product

    def show_potential_substitutes(self, category_id, selected_product):
        substitutes_list = self.product_logic.get_potential_substitutes_list(category_id, selected_product)
        i = 1
        
        if len(substitutes_list) > 0:
            print('\nN° - Nom - Nutriscore - Novascore - Marque')
            print('-------------------------------------------------------------------------------------------------------------------------------')
            for substitute in substitutes_list:
                self.codes_sub_of_selected_product.append((i, substitute.get_id()))
                print(
                    f'| {i!s:>2} - {substitute.get_designation()[0:80]!s:<82} | {substitute.get_nutriscore()} | {substitute.get_novascore()} | {substitute.get_brand()!s:<25} |'
                    )
                print('-------------------------------------------------------------------------------------------------------------------------------')
                i = i + 1

            print('N° - Nom - Nutriscore - Novascore - Marque\n')
            print("\nMerci !")
            print("Vous avez choisi le produit suivant : ")
            print(
                f'==> {selected_product.get_designation()} - {selected_product.get_nutriscore()} - {selected_product.get_novascore()} - {selected_product.get_brand()}'
                )
            print('\nVous avez, ci-dessus, une liste de produits de meilleure qualité nutritionnelle que celui que vous avez choisi.')
            print('Ces produits sont classés par nutriscores puis novascore décroissants. Les produits les plus intéressants sont donc les derniers de la liste.\n')
        else:
            print("\nMerci !")
            print("Vous avez choisi le produit suivant : ")
            print(
                f'==> {selected_product.get_designation()} - {selected_product.get_nutriscore()} - {selected_product.get_novascore()} - {selected_product.get_brand()}'
                )
            print("\nVous avez choisi un excellent produit dans cette catégorie, nous n'en avons pas de meilleur à vous proposer !")
        
        return substitutes_list
    
    def select_substitute(self, category_id, selected_product):
        selected_substitute = ()
        proceed = True

        substitutes_list = self.show_potential_substitutes(category_id, selected_product)
        number_of_products = len(substitutes_list)

        if number_of_products == 0:
            # The menu is displayed to continue
            self.menu.display_menu()
        else :
            while proceed:
                select_number = input("\nSélectionner un produit de substitution tapant son numéro "
                                    "(ou bien tapez un code du menu) puis validez avec \"Entrée\" : ")

                if select_number.upper() == 'M':
                    proceed = False
                    self.menu.display_menu()
                elif select_number.isnumeric() == False or int(select_number) not in range(1, number_of_products + 1):
                    print("\nVous n'avez pas saisi le numéro d'un des produits proposées, veuillez recommencer s'il vous plait.\n")
                else:
                    for code_sub in self.codes_sub_of_selected_product:
                        if code_sub[0] == int(select_number):
                            for substitute in substitutes_list:
                                if code_sub[1] == substitute.get_id():
                                    selected_substitute = substitute
                                    break

                    print("\nMerci !")
                    print('Vous avez choisi le produit "{}" (produit n° {}).'.format(selected_product.get_designation(), select_number))

                    proceed = False

        return selected_substitute

    def save_substitute(self, selected_product, selected_substitute):
        substitute = Substitute(selected_product.get_id(), selected_substitute.get_id())
        proceed = True
        
        while proceed:
            print('\nSouhaitez-vous enregistrer ce substitut afin de pouvoir le rtrouver plus tard ?')
            save_or_not = input("Tapez 'O' pour oui, 'N' pour non puis validez avec \"Entrée\" : ")
            
            if save_or_not.upper() == 'O' or save_or_not == str(0):
                insert = self.substitute_logic.insert(substitute)
                if insert == None:
                    print("\nCe produit de substitution vient d'être sauvegardé, vous pourrez le retrouver, "
                        "avec tous les autres produits enregistrés, en choisissant le menu 'B' "
                        "(Mes aliments de remplacement)")
                    proceed = False
                else:
                    print(insert)
                    proceed = False
            elif save_or_not.upper() == 'N':
                proceed = False
            else:
                print("\nVous n'avez pas saisi une des lettres proposées, veuillez recommencer s'il vous plait.\n")

        # The menu is displayed to continue
        self.menu.display_menu()
