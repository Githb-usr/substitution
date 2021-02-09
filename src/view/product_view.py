#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.data.model.product import Product
from src.logic.product_logic import ProductLogic
from src.view.utilities_view import UtilitiesView

class ProductView:
    """
        ProductView class
        To manage the display of products in the application interface
    """
    
    def __init__(self):
        """ Constructor """
        self.logic = ProductLogic()
        self.utilites = UtilitiesView()
        self.codes = []
        
    def show_products_of_selected_category(self, category_id):
        products = self.logic.get_all_products_of_category(category_id)
        i = 1
        
        print('\n')
        print('N° - Nom (Nutriscore - Novascore)')
        print('Lien vers la fiche complète du produit')
        print('--------------------------------------\n')
        for product in products:
            self.codes.append((i, product.get_id()))
            print(
                f'{i!s:>2} - {product.get_designation()} ({product.get_brand_name()} / {product.get_nutriscore()} - {product.get_novascore()})'
                )
            print(product.get_url()+"\n")
            i = i + 1

        print('--------------------------------------')
        print('N° - Nom (Nutriscore - Novascore)')
        print('Lien vers la fiche complète du produit\n')
        
        return products
    
    def select_product(self, category_id):
        products_set = set()
        selected_product = ()
        proceed = True

        products = self.show_products_of_selected_category(category_id)
        number_of_products = len(products)

        while proceed:
            self.utilites.display_line_menu()
            select_number = input("\nSelectionner un produit en tapant son numéro (ou bien un code du menu) : ")

            if select_number.isnumeric() == False or int(select_number) not in range(1, number_of_products + 1):
                print("\nVous n'avez pas saisi le numéro d'un des produits proposées, veuillez recommencer s'il vous plait.\n")
            else:
                for code in self.codes:
                    if code[0] == int(select_number):
                        for product in products:
                            if code[1] == product.get_id():
                                selected_product = product
                                break

                print("\nMerci !")
                print('Vous avez choisi le produit "{}" (produit n° {}).'.format(selected_product.get_designation(), select_number))

                self.utilites.press_enter()

                proceed = False

        return selected_product

    def show_substitutes(self, category_id, selected_product):
        substitutes_list = self.logic.get_substitutes_list(category_id, selected_product)
        i = 1
        
        if len(substitutes_list) > 0:
            print('\nN° - Nom (Nutriscore - Novascore)')
            print('Lien vers la fiche complète du produit')
            print('--------------------------------------\n')
            for substitute in substitutes_list:
                self.codes.append((i, substitute.get_id()))
                print(
                    f'{i!s:>2} - {substitute.get_designation()} ({substitute.get_brand_name()} / {substitute.get_nutriscore()} - {substitute.get_novascore()})'
                    )
                print(substitute.get_url()+"\n")
                i = i + 1

            print('--------------------------------------')
            print('N° - Nom (Nutriscore - Novascore)')
            print('Lien vers la fiche complète du produit\n')
            print("Vous avez choisi le produit suivant : ")
            print(
                f'==> {selected_product.get_designation()} ({selected_product.get_brand_name()} / {selected_product.get_nutriscore()} - {selected_product.get_novascore()})'
                )
            print('\nVous avez, ci-dessus, une liste de produits de meilleure qualité nutritionnelle que celui que vous avez choisi.')
            print('Ces produits sont classés par nutriscores puis novascore décroissants. Les produits les plus intéressants sont donc les derniers de la liste.')
        else:
            print("Vous avez choisi le produit suivant : ")
            print(
                f'==> {selected_product.get_designation()} ({selected_product.get_brand_name()} / {selected_product.get_nutriscore()} - {selected_product.get_novascore()})'
                )
            print("\nVous avez déjà choisi le meilleur produit dans cette catégorie, nous n'avons pas d'autre produit à vous proposer !")
        
        return substitutes_list
