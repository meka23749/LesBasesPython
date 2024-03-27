pizzas = [("4 fromages", 10.99), ("vegetarienne", 7.99), ("hawai", 5.99), ("calzone", 2.30)]

def afficher(pizzas, nombre_pizza=0):
    print()
    if len(pizzas) == 0:
        print(" ----- AUCUNE PIZZA ----- ")
    else:
        print(" ----- LISTES DES PIZZAS", len(pizzas), "----- ")
        for i in pizzas:
            print(i[0], i[1], "$")
        print()
        print("premiere pizza: ", pizzas[0][0], pizzas[0][1], "$")
        print("derniere pizza: ", pizzas[-1][0], pizzas[-1][1], "$")
        for j in pizzas[0:nombre_pizza]:
            print("Les trois premiere pizza sont: ", j[0], j[1], "$")
def ajouter_pizza_utilisateur(pizzas):
    print()
    nom_pizza = input("Pizza a ajouter: ")
    if pizza_existe(nom_pizza):
        print("Erreur: la pizza existe deja")
        return
    pizzas.append(nom_pizza)
def pizza_existe(nom_pizza):
    for i in pizzas:
        if i == nom_pizza:
            return True

afficher(pizzas,3)
#vide = ()
ajouter_pizza_utilisateur(pizzas)
afficher(pizzas)
afficher(pizzas, 3)
        
