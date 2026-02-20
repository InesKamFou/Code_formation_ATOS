import os

# Afficher le répertoir courant
chemin = os.getcwd()
print(chemin)

# Changer de répartoir
os.chdir('C:\\Users')
print(os.getcwd())
os.chdir('C:\\Users\\GK Student\\Desktop\\Codes_formation_python_ATOS')
print(os.getcwd())

for item in os.listdir(os.getcwd()):
    
    if os.path.isfile(item) and item[-3:]=="txt":
        print("----File txt: ", item)
    if os.path.isfile(item) and item[-3:]=="csv":
        os.remove(item)
    if os.path.isdir(item):
        print("----Dir: ", item)

# Obtenir des informations système
print(os.getlogin())
print(os.getpid())
print(os.getenv("HOME"))
print(os.name)