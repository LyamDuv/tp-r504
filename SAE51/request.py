import mysql.connector

# Informations de connexion à la base de données
DB_USER = "etudiant"
DB_PASS = "Abricotdu7"
DB_NAME = "GestionParcInformatique"
DB_HOST = "localhost"
DB_PORT = 3306
# Connexion à la base de données MySQL
conn = mysql.connector.connect(user=DB_USER, password=DB_PASS,host=DB_HOST,port=DB_PORT,database=DB_NAME)
cursor = conn.cursor()

# 1. Liste de toutes les machines de marque HP
cursor.execute("SELECT * FROM Ordinateurs WHERE marque_ordinateur = 'HP'")
result_1 = cursor.fetchall()
print("Résultat de la requête 1:")
for row in result_1:
    print(row)

# 2. Liste de toutes les machines achetées entre 2018 et 2020
cursor.execute("SELECT * FROM Ordinateurs WHERE date_achat BETWEEN '2018-01-01' AND '2020-12-31'")
result_2 = cursor.fetchall()
print("\nRésultat de la requête 2:")
for row in result_2:
    print(row)

# 3. Liste de toutes les machines de marque HP achetées entre 2019 et 2020
cursor.execute("SELECT * FROM Ordinateurs WHERE marque_ordinateur = 'HP' AND date_achat BETWEEN '2019-01-01' AND '2020-12-31'")
result_3 = cursor.fetchall()
print("\nRésultat de la requête 3:")
for row in result_3:
    print(row)

# 4. Nombre de machines de marque Dell dans l’ensemble du parc
cursor.execute("SELECT COUNT(*) FROM Ordinateurs WHERE marque_ordinateur = 'Dell'")
result_4 = cursor.fetchone()
print("\nRésultat de la requête 4:")
print("Nombre de machines Dell :", result_4[0])

# 5. Liste de toutes les machines ayant entre 4GB et 8GB de RAM
cursor.execute("SELECT * FROM Ordinateurs WHERE ram_gb BETWEEN 4 AND 8")
result_5 = cursor.fetchall()
print("\nRésultat de la requête 5:")
for row in result_5:
    print(row)

# 6. Liste des logiciels installés sur la machine n°1234
cursor.execute("SELECT * FROM Logiciels WHERE id_ordinateur = 1234")
result_6 = cursor.fetchall()
print("\nRésultat de la requête 6:")
for row in result_6:
    print(row)

# 7. Liste des logiciels installés sur la machine attribuée à M. Duchmoll
cursor.execute("""
SELECT Logiciels.*
FROM Logiciels
JOIN Affectations ON Affectations.id_ordinateur = Logiciels.id_ordinateur
JOIN Utilisateurs ON Utilisateurs.id = Affectations.id_utilisateur
WHERE Utilisateurs.nom_utilisateur = 'M. Duchmoll'
""")
result_7 = cursor.fetchall()
print("\nRésultat de la requête 7:")
for row in result_7:
    print(row)

# 8. Liste des utilisateurs utilisant une machine de marque HP
cursor.execute("""
SELECT Utilisateurs.*
FROM Utilisateurs
JOIN Affectations ON Affectations.id_utilisateur = Utilisateurs.id
JOIN Ordinateurs ON Ordinateurs.id = Affectations.id_ordinateur
WHERE Ordinateurs.marque_ordinateur = 'HP'
""")
result_8 = cursor.fetchall()
print("\nRésultat de la requête 8:")
for row in result_8:
    print(row)

# 9. Liste des utilisateurs utilisant une machine de marque HP avec un OS "Windows 10"
cursor.execute("""
SELECT Utilisateurs.*
FROM Utilisateurs
JOIN Affectations ON Affectations.id_utilisateur = Utilisateurs.id
JOIN Ordinateurs ON Ordinateurs.id = Affectations.id_ordinateur
WHERE Ordinateurs.marque_ordinateur = 'HP' AND Ordinateurs.systeme_exploitation = 'Windows 10'
""")
result_9 = cursor.fetchall()
print("\nRésultat de la requête 9:")
for row in result_9:
    print(row)

# 10. Liste des machines sur lesquelles il y a eu intervention technique entre le 10/10/2021 et le 10/12/2021
cursor.execute("""
SELECT * FROM Ordinateurs
WHERE id IN (SELECT id_ordinateur FROM Maintenance WHERE date_maintenance BETWEEN '2021-10-10' AND '2021-12-10')
""")
result_10 = cursor.fetchall()
print("\nRésultat de la requête 10:")
for row in result_10:
    print(row)

# 11. Liste de machines sur lesquelles le technicien Jean Neymar a fait de la maintenance
cursor.execute("""
SELECT Ordinateurs.*
FROM Ordinateurs
JOIN Maintenance ON Maintenance.id_ordinateur = Ordinateurs.id
WHERE Maintenance.technicien = 'Jean Neymar'
""")
result_11 = cursor.fetchall()
print("\nRésultat de la requête 11:")
for row in result_11:
    print(row)

# 12. Liste de machines sur lesquelles le technicien Jean Neymar a fait de la maintenance en 2021
cursor.execute("""
SELECT Ordinateurs.*
FROM Ordinateurs
JOIN Maintenance ON Maintenance.id_ordinateur = Ordinateurs.id
WHERE Maintenance.technicien = 'Jean Neymar' AND YEAR(Maintenance.date_maintenance) = 2021
""")
result_12 = cursor.fetchall()
print("\nRésultat de la requête 12:")
for row in result_12:
    print(row)

# Fermer la connexion à la base de données
cursor.close()
conn.close()

