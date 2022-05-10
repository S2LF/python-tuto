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
# Ajoute une ligne à la table
conn.commit()

# Ferme la connexion
conn.close()
