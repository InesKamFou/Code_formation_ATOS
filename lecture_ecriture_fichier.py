# lecture
with open("presentation_python.txt", mode = 'r', encoding='utf-8') as input:
    lignes = input.readlines()
# traitement
liste_num = list()
for num, texte in enumerate(lignes, 1):
    #print(num, texte)
    if 'Python' in texte:
        liste_num.append(num)
#print(liste_num)
# ecriture
with open("index.txt", mode ='w') as output:
    for val in liste_num:
        print(val,  file = output)
