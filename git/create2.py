import mysql.connector

# Informations de connexion à la base de données
DB_USER = "etudiant"
DB_PASS = "Abricotdu7"
DB_NAME = "GestionParcInformatique"

# Connexion à la base de données MySQL
conn = mysql.connector.connect(user=DB_USER, password=DB_PASS)
cursor = conn.cursor()


# Chemin du fichier SQL
sql_file_path = "/etc/sae51.sql"

# Lecture du contenu du fichier SQL
with open(sql_file_path, "r") as sql_file:
    sql_commands = sql_file.read().split(';')[:-1]  # Divise les commandes SQL

# Exécution des commandes SQL
for command in sql_commands:
    cursor.execute(command)

# Fermer la connexion à la base de données
cursor.close()
conn.close()
