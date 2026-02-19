age = input("donnez votre age: ")
print(age.isdigit())
while not(age.isdigit() and 0 < int(float(age)) < 100):
    print("age invalide merci de fournir un age sous forme de nombre uniquement")
    age = input("donnez votre age: ")
print(age)

nom = input("donnez votre nom: ")
while not(nom and nom.replace("-","").isalpha()):
     print("nom invalide merci de fournir un nom composé de lettres uniquement")
     nom = input("donnez votre nom: ")
print(nom)

prenom = input("donnez votre prenom: ")
while not(prenom and prenom.replace("-","").isalpha()):
     print("Prenom invalide merci de fournir un prénom composé de lettres uniquement")
     prenom = input("donnez votre prenom: ")

ville = input("donnez votre ville: ")
while not(ville and ville.replace("-","").isalpha()):
     print("Ville invalide merci de fournir une ville composée de lettres uniquement")
     ville = input("donnez votre prenom: ")

profession = input("donnez votre profession: ")
while not(profession and profession.replace("-","").isalpha()):
     print("Profession invalide merci de fournir une profession composée de lettres uniquement")
     profession = input("donnez votre profession: ")

taille = input("donnez votre taille: ")
while not(taille.replace(".","").isdigit() and 0.50 < float(taille) < 3.0):
    print("taille invalide merci de fournir une taille au format x.xx entre 0.5 et 3")
    taille = input("donnez votre taille: ")
print(taille)    

print(f"{prenom.capitalize()} {nom.upper()} a {age} ans et habite à {ville.upper()}.\nSa taille est de {taille.replace(".","m")} et c'est un {profession}")