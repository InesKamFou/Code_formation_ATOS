import pandas as pd
import re # expression régulière
import json

# ------------------------------------------------
# 1) Lire le fichier CSV
# ------------------------------------------------
df = pd.read_csv("input/personnes.csv")

# ------------------------------------------------
# 2) Construire un Nom complet
# ------------------------------------------------
df["Nom Complet"] = df["Prénom"] + " " + df["Nom"]

# ------------------------------------------------
# 3) Séparer numéro de téléphone
#     Exemple : "+33 134906477"
# ------------------------------------------------

# Extraire préfixe international
df["Prefixe"] = df["Téléphone"].str.extract(r"^(\+\d+)")

# Extraire le numéro national
df["NumeroTelephone"] = df["Téléphone"].str.extract(r"\+\d+\s*(.*)")

# Supprimer les espaces dans le numéro
df["NumeroTelephone"] = df["NumeroTelephone"].str.replace(" ", "", regex=False)

# ------------------------------------------------
# 4) Construire l'adresse complète
# Exemple : "70 Rue de l'Église, Marseille"
# ------------------------------------------------
df["Adresse"] = (
    df["Numéro Rue"].astype(str) # transformer vers une str
    + " "
    + df["Nom Rue"]
    + ", "
    + df["Ville"]
)

# ------------------------------------------------
# 5) Valider les emails
# ------------------------------------------------
regex_email = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$" # expression régulière de validation d'un email
df_valid = df[df["Email"].str.match(regex_email, na=False)]

# ------------------------------------------------
# 6) Sélectionner les colonnes utiles
# ------------------------------------------------
colonnes_utiles = [
    "ID",
    "Nom Complet",
    "Sexe",
    "Date de naissance",
    "Prefixe",
    "NumeroTelephone",
    "Pays",
    "Ville",
    "Adresse",
    "Email",
]

# Convertir en liste de dictionnaires
resultat = df_valid[colonnes_utiles].to_dict(orient="records")

# ------------------------------------------------
# 7) Exporter en JSON propre
# ------------------------------------------------
with open("personnes_propre.json", "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=2)

print("Traitement terminé.")
print("Personnes valides :", len(resultat))
print("Fichier généré : personnes_propre.json")