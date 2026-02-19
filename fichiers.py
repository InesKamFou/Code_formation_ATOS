with open("presentation_python.txt", encoding = "utf-8") as f:
    contenu = f.read() # lecture de tout le contenu
    print(contenu)
    f.seek(1) # remettre le curseur au début
    print("***************")
    contenu = f.readline()
    print(contenu)
    print(f.readline())
print("-------------------------------")
# with open("presentation_python.txt", encoding = "utf-8") as f:
#     for ligne in f:
#         print(ligne)
# print("-------------------------------")
# with open("presentation_python.txt", encoding = "utf-8") as f:
#     contenu = f.readlines()
#     for num, ligne in enumerate(contenu,1):
#         if 'Python' in ligne:
#              print(f"{num}: {ligne}")

# with open("output.txt", mode="w", encoding='utf-8') as f:
#     f.write("Bonjour\n")





