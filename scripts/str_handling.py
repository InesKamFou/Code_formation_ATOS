ch1 = "bonjour"
ch2 = 'à tous'
ch3 = "Aujourd'hui c'est mercredi"
# """ch4 = "\nAujoud'hui c'est l'anniversaire de \"Ines\""
# chemin = 'c:\\\\Users\\GK Student'"""
# print("""---------------------------------
# ---------------- Bonjour -----------
# ------------------------------------""")
# print(chemin)
# print(ch4)
print(ch1+' '+ch2)
print(ch1*3)
ch4 = " "*100
print(ch4+"*")
print("affiche: ", ch1[0])
print("affiche: ", ch1[2])
print("affiche: ", ch1[-1])
print("affiche: ", ch1[-7])
print(len(ch1))
print("Dernier caractère: ",  ch1[len(ch1)-1]) # Emprunté des autres languages
car = "a"
print(type(car))


ch1 = 'abcdefghij'
ch2 = 'zt'
print(ch1<ch2)

print("recherche d'une sous chaine: ", "cde" in ch1)
print("recherche d'une sous chaine: ", "Cde" in ch1)

ch1 = "0123456789"
print("slicing: ", ch1[1:7])
print("slicing: ", ch1[0:10])
print("slicing: ", ch1[0:10:2])
print("slicing: ", ch1[::2])
print("slicing: ", ch1[1::3])
print("slicing: ", ch1[10:-5:-1])
print("Ines"[-1])

ch= "        BonJour       "
print("Ma chaine en miniscule: ", ch.lower())
minuscule = ch.lower()
print(ch, minuscule)
print("Ma chaine sans espaces: ", ch.strip())
print("Ma chaine après remplacement: ", ch.replace("Jour","Soir").strip())
print("Ma chaine après remplacement: ", ch.replace("jour","Soir")) # la chaine ne sera pas modifiée car "jour" n'est pas dns la chaine
ch = "     bonjour   ici     il fait   18° C    "

ch_cleaned = ch.strip().replace("  "," ").replace("  "," ").replace("  "," ").replace("18", "4")
print(ch_cleaned)

file1 = "bla.txt"
file2 = "script.py"
print(file1.endswith(".txt"))
print(file2.endswith(".txt"))
