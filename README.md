# ORIGIN #
This project is an exercise done as part of an OpenClassrooms training course for developers in the Python language.
It corresponds to project 5 of the training.


# GOAL OF THE APPLICATION #
This application makes it possible to choose a food for which one wishes to obtain a better quality substitute, in order to improve one's diet. It's based on the Open Food Facts database. It's a free and collaborative database referencing food products from all over the world.

The Open Food Facts website (FR): https://fr.openfoodfacts.org/


# FEATURES #
* The application connects to the Open Food Facts API and downloads a list of products.
* The application saves these products in a database.
* The user interacts with the application in a console.
* The user can select a product from the database.
* The user can search for a product of better nutritional quality (a substitute).
* The user can save the result of his search for a substitute.
* The user can display a list of all substitutes he has registered.
* The user can empty the database and reload a list of products (substitutes are then lost).
* The user can quit the application.


# USER PATH #
The user is on the console. The machine displays the following choices:
1. Replace a food
2. My replacement foods (or substitutes)
3. Reset the application
4. Exit the application

The user selects 1. The application asks the user the following questions and the user selects the answers :
* Select the category.
  => Several proposals associated with a number. The user enters the corresponding number and presses "Enter".
* Select the food.
  => Several proposals associated with a number. The user enters the number corresponding to the selected food and presses "Enter".
* The programme provides a substitute, its description, where to buy it (if available) and a link to the Open Food Facts page for that food.
* The user then has the option to save the result in the database.


# CONSTRAINTS #
* The programming language used is Python.
* The search must be carried out on a MySQL database.
* This database is powered by the Open Food Facts API. Once the data has been retrieved, the API is no longer connected.
* If the user enters a character that is not a number, the program must repeat the question.


# EXAMPLE OF A PRODUCT DICTIONARY RECOVERED VIA API AFTER FIRST CLEANUP #
The fields kept for the application are therefore, in alphabetical order : 
* brands            (For the user's information)
* categories        (To filter the products)
* code              (To identify the product)
* nova_group        (To determine nutritional quality)
* nutriscore_grade  (To determine nutritional quality)
* product_name      (To identify the product)
* stores            (For the user's information)
* url               (For the user's information)

```python
{'nova_group': 4, 'stores': 'Leclerc,Magasins U, Carrefour', 'url': 'https://fr.openfoodfacts.org/produit/3760049790252/toastiligne-la-boulangere', 'brands': 'la boulangère', 'code': '3760049790252', 'product_name': 'Toastiligne', 'nutriscore_grade': 'a', 'categories': "Aliments et boissons à base de végétaux, Aliments d'origine végétale, Céréales et pommes de terre, Pains, Pains de mie"}
