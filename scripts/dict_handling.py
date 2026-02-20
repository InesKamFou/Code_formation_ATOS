personnes = [{ 'id': 101, 'nom': 'kamoun',    'prenom': 'Ines',    'age' : 47,    'taille' : 1.55,    'status': True},
             {'id': 202, 'Nom': 'Pitel', 'prenom': 'Thomas', 'status': True}]
print(personnes)
print(personnes[0]['nom'])
print(type(personnes[0]['taille']), personnes[0]['taille'])
taille = personnes[1].get('taille', None)
if taille : 
    print(taille)
else:
    print("taille non renseignée")

# Récupérer les clés
print("----------- Clés")
personne = personnes[0]
print(list(personne.keys()))

for cle in personne.keys():
    print(cle)

# Récupérer les valeurs
print("------ Valeurs")
personne = personnes[0]
print(list(personne.values()))

for val in personne.values():
    print(val)
# ----------- Recherche
print("---------------------- *Recherche")
for personne in personnes:
    nom = personne.get('Nom',None)
    if nom and nom.lower() == 'pitel':
        print(personne)
personnes[0]['domaine'] = 'IT'
print(personnes)
dic_ines = personnes[0]
# Parcours avec les clés et les valeurs
print(dic_ines.items())
for cle, valeur in dic_ines.items():
    print(f"{cle} --> {valeur}")

# zip

noms = ["Ines", "alain", "Thomas", "lotfi"]
codes = [101, 202, 303]
print(dict(zip(codes, noms)))
print(dict(zip(noms, codes)))
dict_personnel = dict(zip(codes, noms))
print(dict_personnel)

# ------- dictionnaires imbriqués

print("-------------- dico impriqué ---------")
doc = {
    "meta": {"ver": 1, "tag": "r5"},
    "data": {
        "items": [
            {"id": "u01", "score": 12},
            {"id": "u02", "score": 7},
            {"id": "u03", "score": 19},
        ]
    }
}

print (len(doc))
print(doc.keys())
# score id 'u02'

print(f"score de  d'id u02: {doc['data']['items'][1]['score']}")
id = 'u02'
for item in doc['data']['items']:
    if item['id'] == id:
        print(f"score de  d'id u02: {item['score']}")

# inverser un dictionnaire

dico = {'id': 202, 'Nom': 'Pitel', 'prenom': 'Thomas', 'status': True}
dico_invers = dict() # dico_invers = {}

for cle, valeur in dico.items():
    dico_invers[valeur] = cle
print(dico_invers)

inverse = {valeur:cle for cle, valeur in dico.items()}
print(inverse)
