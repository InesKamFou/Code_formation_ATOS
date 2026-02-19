codes = [101,202,303,404,505]
# ce n'est du python
for i in range(len(codes)):
    print(f"{i} -> {codes[i]}")
# du python pro
for item in codes:
    print(item)

# Bonne pratique
for index, valeur in enumerate(codes, start = 1):
    print(f"{index} -> {valeur}")

erreur = ['SESSION 2026-01-26 12:12:45.760 -----------------------------------------------',
          'eclipse.buildId=unknown',
          'java.version=11.0.20',
          'java.vendor=Oracle Corporation']

for index, ligne in enumerate(erreur):
    if 'version' in ligne:
        print(f"{index} -> {ligne}")

# Kheireddine
codes = [1,2,3,4,1]
for item in codes :
    print(item)
print("*****  fonction enumerate *****")
print()
for index, valeur in enumerate(codes, start= 1) :
    print(f"Index :{index} ==> valeur :{valeur} est à la position {codes.index(valeur)}")

print("enumerate de codes \n",list(enumerate(codes,start=1)))

enregistrement = ("ID123", "Ines", "Femme", "IT", 2026)
ident, *infos, annee = enregistrement  # 'infos' reçoit le milieu
print("Star-unpack -> ident:", ident, "| infos:", infos, "| annee:", annee)

