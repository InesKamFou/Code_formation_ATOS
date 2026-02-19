# 
# 
# 
# 

valid_loop = True
while valid_loop:
    nom = str(input("Saisissez votre nom de famille : "))
    if not nom.isalpha():
      print("seules les valeurs aphabetiques sont acceptées ")
    else:
      break

# a = value_if_true if condition else value_if_false
# nom = str(input("Saisissez votre nom de famille")) if not nom.isalpha() else print("seules les valeurs aphabetiques sont acceptées ")

valid_loop = True
while valid_loop:
    prenom = str(input("Saisissez votre prenom : "))
    if not prenom.isalpha():
       print("seules les valeurs aphabetiques sont acceptées ")
    else:
       break


valid_loop = True
while valid_loop:
    age = input("Saisissez votre age : ")
    if not age.isdigit():
       print("seules les valeurs correctes d'ages sont acceptées ")
    elif not 0 < int(age) < 119:
        print("seules les valeurs correctes d'ages sont acceptées ")
    else:
       age = int(age)
       break

valid_loop = True
while valid_loop:
    taille = input("Saisissez votre taille en centimètres : ")
    if not (taille.replace(".","").isdigit() and 1.40 < float(taille) < 2.2):
        print("seules les valeurs correctes de taille sont acceptées ")
    else:
       taille = float(taille)
       break

print(f"{prenom.capitalize()} {nom.upper()} a {age} ans \n Sa taille est de {taille}")

