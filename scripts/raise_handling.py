val = input('Donner une valeur positive: ')
if not val.replace('-','').isdigit():
    raise ValueError("Ta valeur n'est pas numérique")
if int(val) < 0 :
    raise Exception("Votre valeur est négative")