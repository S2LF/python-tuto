import sqlite3

# Ouverte une connexion à la base de données
conn = sqlite3.connect('database.db')

# Crée un curseur pour parcourir les données
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employees2 (
    prenom TEXT,
    nom TEXT,
    salaire INTEGER
)
""")

employees = {"prenom": "Paul", "nom": "Durand", "salaire": 10000}

c.execute("INSERT INTO employees2 VALUES (:prenom, :nom, :salaire)", employees)
employees_edit = {"prenom": "Pierre", "nom": "Dupond", "salaire": 20000}

c.execute("UPDATE employees2 SET salaire = :salaire WHERE prenom = :prenom AND nom = :nom", employees_edit)

c.execute("SELECT * FROM employees2")

# On récupère une liste de tuples
donnees = c.fetchall()
print(donnees)

c.execute("DELETE FROM employees2 WHERE prenom = :prenom AND nom = :nom", employees)

c.execute("SELECT * FROM employees2")

donnees = c.fetchall()
print(donnees)

# Delete TOUT
c.execute("DELETE FROM employees2")

c.execute("SELECT * FROM employees2")
donnees = c.fetchall()
print(donnees)


# c.execute("SELECT * FROM employees")
# prems = c.fetchone()
# print(prems)
# deux = c.fetchone()
# print(deux)

# Ajoute une ligne à la table
conn.commit()

# Ferme la connexion
conn.close()
