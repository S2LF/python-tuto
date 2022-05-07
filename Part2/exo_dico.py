employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
for id, infos in employes.items():
    if infos["prenom"] == "Patrick":
        del employes[id]
        break

for id, infos in employes.items():
    if infos["prenom"] == "Julie":
        infos["age"] += 1
    if infos["prenom"] == "Paul":
        age_paul = infos["age"]
    if infos["prenom"] == "Patrick":
        del employes[id]
