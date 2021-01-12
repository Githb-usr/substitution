# ORIGINE #
Ce projet est un exercice fait dans le cadre d'une formation OpenClassrooms de développeur en langage Python.
Il correspond au projet 5 de la formation.


# BUT DU PROGRAMME #
Ce programme  permet de choisir un aliment pour lequel on souhaite obtenir un substitut de meilleure qualité, afin d'améliorer son alimentation.
Il repose sur la base de données d'Open Food Facts. C'est une base de données libre et collaborative référençant les produits alimentaires du monde entier.

Le site (FR) d'Open Food Facts : https://fr.openfoodfacts.org/


# FONCTIONNALITES #
L'utilisateur est sur un terminal. Ce dernier lui affiche les choix suivants :
1. Sélectionner un aliment à remplacer
2. Retrouver mes aliments substitués

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :
* Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.


# CONTRAINTES #
Le langage de programmation utilisé est Python.
La recherche doit s'effectuer sur une base MySQL.
Cette base de données est alimentée grâce à l'API de Open Food Facts. Une fois ces donénes récupérées, on ne se connecte plus à l'API. On récupère seulement une dizaine de catégories d'aliments et une centaine d'aliments de chaque catégorie.

