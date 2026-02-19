# age = int(input("Donner votre age: "))
# # print(age)
# if age < 18 :
#     print("Mineur")
#     print("Vous n'avez le droit d'accès")
# else:
#     print("Vous êtes majeur")
#     print("Soyez le bienvenu")

# nombre = int(input("Donne un nombre: "))
# if nombre < 0:
#     print(nombre, "est négatif")
# else:
#     if nombre > 0 :
#         print(nombre, "est positf")
#     else:
#         print(nombre, "Nul")

# if nombre < 0:
#     print(nombre, "est négatif")
# elif nombre == 0:
#      print(nombre, "Nul")
# else :
#     print(nombre, "est positf")

# x = 15
# if 10 < x < 20:
#     print(x, "est encadré entre 10 et 20")

mois = 'uhlrgg'

match mois:
    case "Janvier":
        print("Mois: 1")
    case "Février":
        print("Mois: 2")
    case _:
        print("Autre")
 