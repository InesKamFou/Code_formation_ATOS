from pathlib import Path
try:
    # Problème : addition d'une str et d'un int → types incompatibles
    resultat = "3" + 2
except TypeError as e:
    print("Exception attrapée :", e)
    # Bonne pratique : convertir explicitement selon l'intention
    resultat_corrige = int("3") + 2
    print("Correction (int('3') + 2) =", resultat_corrige)
try:
    with open("../input/presentation_python.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError as e:
    print("Exception attrapée :", repr(e))
    # Bonne pratique : vérifier l'existence avant d'ouvrir
    chemin = Path("../input/presentation_python.txt")
    if not chemin.exists():
        chemin.write_text("Contenu de démonstration", encoding="utf-8")
    print("Lecture correcte :", chemin.read_text(encoding="utf-8"))
# while True:
#     file = input("Donner le fichier à ouvrir: ")
#     print(file)
#     try:
#         with open(file, mode = 'r', encoding= 'utf-8') as f:
#             contenu = f.read()
#     except FileNotFoundError:
#         print('vérifier le nom du fichier ou le chemin d\'accès')
#     else:
#         break
# print(contenu)
