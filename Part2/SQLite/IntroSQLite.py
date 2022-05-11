import sqlite3

# Ouverte une connexion à la base de données
conn = sqlite3.connect('database.db')

# Crée un curseur pour parcourir les données
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employees (
    prenom TEXT,
    nom TEXT
)
""")

employees = {"prenom": "Pierre", "nom": "Dupond"}

# c.execute("INSERT INTO employees VALUES (:prenom, :nom)", employees)

c.execute("SELECT * FROM employees")

# On récupère une liste de tuples
donnees = c.fetchall()
print(donnees)

c.execute("SELECT * FROM employees")
prems = c.fetchone()
print(prems)
deux = c.fetchone()
print(deux)

# Ajoute une ligne à la table
conn.commit()

# Ferme la connexion
conn.close()
