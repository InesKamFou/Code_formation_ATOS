import random
#random.seed(42)
print("\n--- Reproductibilité (seed=42) ---")
print("random() ", random.random())
print("random() ", random.random())
print("randint(1, 10) ", random.randint(1, 10))
couleurs = ["rouge", "vert", "bleu", "jaune", "noir"]
# Un seul élément au hasard
c = random.choice(couleurs)
print("Un choix :", c)
# Plusieurs éléments AVEC remise (peut répéter)
# weights / cum_weights permettent de pondérer les probabilités
tirages_ponderes = random.choices(
    population=couleurs,
    weights=[1, 1, 3, 1, 1],  # "bleu" a 3x plus de chances
    k=5
)
print("Plusieurs choix (avec remise, pondérés) :", tirages_ponderes)


# ÉCHANTILLONNAGE (SANS REMISE)
# Prend k éléments distincts (erreur si k > len(population))
echantillon = random.sample(couleurs, k=3)
print("Échantillon sans remise (k=3) :", echantillon)

mot_pass = ''
for i in range(10):
    z = random.randint(65, 122) 
    mot_pass += chr(z) 
print(mot_pass)