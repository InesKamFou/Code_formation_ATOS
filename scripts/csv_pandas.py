import pandas as pd # pd : alias

df = pd.read_csv("../input/personnes.csv")
print(df)
# Les noms

df_nom = df['Nom']
print(df_nom)

# Filter les personnes par pays
df_france = df[(df['Pays']=='France') & (df['Sexe']=='F')]
print(df_france)
print(len(df_france))
df_france.to_csv("../output/Personnes_françaises.csv", sep= ';', index = False )

