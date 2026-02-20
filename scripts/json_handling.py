import json
donnees_initiales = {
    "entreprise": "TechNova",
    "employes": [
        {
            "id": 1,
            "nom": "Alice",
            "poste": "Développeuse",
            "competences": ["Python", "SQL"]
        },
        {
            "id": 2,
            "nom": "Martin",
            "poste": "Analyste",
            "competences": ["Excel", "Power BI"]
        }
    ],
    "localisation": {
        "pays": "France",
        "ville": "Lyon"
    }
}

with open("../output/donnees.json", "w", encoding="utf-8") as f:
    json.dump(donnees_initiales, f, indent=4, ensure_ascii=False)

with open('../input/donnees.json', mode = 'r', encoding = 'utf-8') as f:
    data = json.load(f)
print(data)
