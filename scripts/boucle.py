# i = 1
# while i<= 5:
#     print(i)#, end = ' ')
#     i += 1

fin = 5
i = fin
while i >= 0:
    print(i)
    if not i:
        print("SURPISE !!!")

    i -= 1

ch_vide = ''
if not ch_vide:
    print("chaine vide")

for i in range(1,6):
    print(i, "Bonjour")

for nombre in range(10,0,-2):
    print("Nombre: ", nombre)

chaine = "Python"

# Ce n'est pas python
for i in range(len(chaine)):
    print(chaine[i])

# Python c'est ça
for lettre in chaine:
    print(lettre)

# Afficher tous les nombres pais entre 0 et 40
for valeur in range(40):
    if not valeur % 2 :
        print(valeur)
# Boucle pour remplacer le do--while
# while True:
#     age = int(input("Donnez votre âge: "))
#     if age <= 0:
#         print("Valeur éronnée")
#     else:
#         break

# test = False
# while not test:
#     age = int(input("Donnez votre âge: "))
#     if age <= 0:
#         print("Valeur éronnée")
#     else:
#         test = True

compteur = 100
while compteur > 0:
    print("compteur ",compteur)
    compteur -= 50
    for i in range(5):
        compteur = compteur + i
        print ("compteur boucle for : ",compteur)
        if compteur == 16:
            print("fin par break")
            break # arrête la for
print ("fin boucle while")

for i in range(10):
    print(i, "Python")
    if i ==3:
        continue
    print("GK")
    print("Ines")

for n in range(1, 100):
    if n == 5:
        print("On saute 5")
        continue       # Passe au tour suivant
    if n == 8:
        print("On arrête la boucle à 8")
        break          # Arrête la boucle
    print("Nombre :", n)

# Affichage avec format
nb_enfants = 2
nom = "Kamoun"
prenom = "Ines"

print(nom,",",prenom,"a", nb_enfants, "enfants") # ce n'est pas python
print(nom+', '+prenom+" a "+str(nb_enfants)+" enfants") # autre manière

print("{}, {} a {} enfants".format(nom, prenom, nb_enfants)) # ancienne version

print(f"{nom}, {prenom} a {nb_enfants} enfants") # TOP !!!