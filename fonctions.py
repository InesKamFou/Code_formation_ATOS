# def affiche():
#      print("-----------------------------------")
# def addition_entier(a : int , b: int) -> int:
#     """ C'est une fonction qui additionne deux entiers """
#     if isinstance(a, (int)) and isinstance(b, (int)):
#           return a + b
#     else:
#          return None

def calcul_arithmetique(a: float, b: float):
    """
    Calcule les principales opérations arithmétiques entre deux nombres.

    Args:
        a (float): Le premier opérande.
        b (float): Le deuxième opérande.

    Returns:
        tuple:
            - somme (float): Résultat de a + b.
            - difference (float): Résultat de a - b.
            - produit (float): Résultat de a * b.
            - quotient (float | None): Résultat de a / b si b ≠ 0,
              sinon None.

    Raises:
        TypeError: Si `a` ou `b` ne sont pas des nombres.

    Examples:
        >>> calcul_arithmetique(10, 5)
        (15, 5, 50, 2.0)

        >>> calcul_arithmetique(7, 0)
        (7, 7, 0, None)
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres.")

    quotient = a / b if b != 0 else None

    return a + b, a - b, a * b, quotient
# def presentation(x, y):
#      print(f"j'ai reçu en x: {x}, j'ai reçu en y: {y}")

# def incremente(x, step = 1):
#      x += step
#      return x 

# def affiche_valeurs(*args ):
#      print(type(args), args, len(args))
#      for elem in args:
#           print(elem)
# def affiche_valeurs(*args ):
#      print(type(args), args, len(args))
#      for elem in args:
#           print(elem)
# def division_euclidienne( a, b):
#      return a//b, a % b
# def affiche_infos (**arguments):
#      print(type(arguments), arguments)
#      print(arguments['nom'])

# res = addition_entier(7,8)
# print("Résultat: ", res)
# print("2eme résultat: ", addition_entier ("Ines", "kamoun"))
# print(addition_entier(2.3, 3.4))

# help(addition_entier)

# print("1er appel")
# presentation(10,20)
# print("2eme appel")
# presentation(y = 101, x = 80)

# print(incremente(10), end = " * ")
# print(incremente(10,step = 5))
    
# affiche()

# affiche_valeurs(1,3,9,8)
# affiche_valeurs("Ines", "Alain", [101,202])

# affiche_infos(nom= "Kamoun", prenom = "Ines")

# print(division_euclidienne(7,3))
# div, mod = division_euclidienne(7,3)
# print(f"div: {div}, mod: {mod}")


# somme, difference, multi, divsision = calcul_arithmetique(7,6)
# print(somme, difference,multi, divsision)

def fonction():
     global x
     print(x)
def incre():
     global x
     x = x+1

x = 50
incre()
fonction()

