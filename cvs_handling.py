import csv
# lecture des lignes séparemment
# with open("personnes.csv", mode = "r", encoding = "utf-8") as f:
#     lecture = csv.reader(f)
#     print(type(lecture))
#     for ligne in lecture:
#         print(ligne)

# lecture sous forme de dictionnaire
with open("personnes.csv", mode = "r", encoding = "utf-8") as f:
    lecture = csv.DictReader(f)
    for ligne in lecture:
        print(ligne['ID'], ligne['Nom'])

nouveaux = [
    ["id", "nom", "departement", "salaire"],
    [5, "Emma", "Finance", 4100],
    [6, "Leo", "RH", 3950],
	]
with open("salaries.csv", mode = "w", newline = "") as output:
    writer = csv.writer(output, delimiter= ';')
    writer.writerows(nouveaux)