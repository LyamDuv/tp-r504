from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Informations de connexion à la base de données (mettez-les en haut de votre fichier)
DB_USER = "etudiant"
DB_PASS = "Abricotdu7"
DB_NAME = "GestionParcInformatique"
DB_HOST = "SAE51"
DB_PORT = 3306

# Fonction pour exécuter les requêtes (mettez-la en haut de votre fichier)
def execute_query(query):
    conn = mysql.connector.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT, database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Route de base
@app.route('/')
def index():
    return """
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: black;">SAE 51 : Solution Technique</h1>
        <br><br>
        <h2 style="color: cyan;">Bienvenue dans la site de notre base de données "Gestion Parc Informatique"</h2>
        <br><br>
        Cliquer sur <a href='/query1' style="text-decoration: underline; color: red;">query1</a> pour afficher la liste de toutes les machines de marque HP.
        <br>
        Cliquer sur <a href='/query2' style="text-decoration: underline; color: red;">query2</a> pour afficher la liste de toutes les machines achetées entre 2018 et 2020.
        <br>
        Cliquer sur <a href='/query3' style="text-decoration: underline; color: red;">query3</a> pour afficher la liste de toutes les machines de marque HP achetées entre 2019 et 2020.
        <br>
        Cliquer sur <a href='/query4' style="text-decoration: underline; color: red;">query4</a> pour afficher le nombre de machines de marque Dell dans l’ensemble du parc.
        <br>
        Cliquer sur <a href='/query5' style="text-decoration: underline; color: red;">query5</a> pour afficher la liste de toutes les machines ayant entre 4GB et 8GB de RAM.
        <br>
        Cliquer sur <a href='/query6' style="text-decoration: underline; color: red;">query6</a> pour afficher la liste des logiciels installés sur la machine n°1234.
        <br>
        Cliquer sur <a href='/query7' style="text-decoration: underline; color: red;">query7</a> pour afficher la liste des logiciels installés sur la machine attribuée à M. Duchmoll.
        <br>
        Cliquer sur <a href='/query8' style="text-decoration: underline; color: red;">query8</a> pour afficher la liste des utilisateurs utilisant une machine de marque HP.
        <br>
        Cliquer sur <a href='/query9' style="text-decoration: underline; color: red;">query9</a> pour afficher la liste des utilisateurs utilisant une machine de marque HP avec un OS "Windows 10".
        <br>
        Cliquer sur <a href='/query10' style="text-decoration: underline; color: red;">query10</a> pour afficher la Liste des machines sur lesquelles il y a eu intervention technique entre le 10/10/2021 et le 10/12/2021.
        <br>
        Cliquer sur <a href='/query11' style="text-decoration: underline; color: red;">query11</a> pour afficher la liste de machines sur lesquelles le technicien Jean Neymar a fait de la maintenance.
        <br>
        Cliquer sur <a href='/query12' style="text-decoration: underline; color: red;">query12</a> pour afficher la liste de machines sur lesquelles le technicien Jean Neymar a fait de la maintenance en 2021.
        <br><br><br>
        <b>Ibrahim Al Kaisi, Lyam Duval & Laurent Juhasz<br>IUT de Rouen (Site Elbeuf)<br>BUT3 Réseaux et Télécommunications</b>
    </div>
"""


# Exemple de route pour la requête 1
@app.route('/query1')
def query1():
    query = "SELECT * FROM Ordinateurs WHERE marque_ordinateur = 'HP'"
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 2
@app.route('/query2')
def query2():
    query = "SELECT * FROM Ordinateurs WHERE date_achat BETWEEN '2018-01-01' AND '2020-12-31'"
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 3
@app.route('/query3')
def query3():
    query = "SELECT * FROM Ordinateurs WHERE marque_ordinateur = 'HP' AND date_achat BETWEEN '2019-01-01' AND '2020-12-31'"
    result = execute_query(query)
    return jsonify(result)
    
# Exemple de route pour la requête 4
@app.route('/query4')
def query4():
    query = "SELECT COUNT(*) FROM Ordinateurs WHERE marque_ordinateur = 'Dell'"
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 5
@app.route('/query5')
def query5():
    query = "SELECT * FROM Ordinateurs WHERE ram_gb BETWEEN 4 AND 8"
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 6
@app.route('/query6')
def query6():
    query = "SELECT * FROM Logiciels WHERE id_ordinateur = 1234"
    result = execute_query(query)
    return jsonify(result)
    
# Exemple de route pour la requête 7
@app.route('/query7')
def query7():
    query = """
SELECT Logiciels.*
FROM Logiciels
JOIN Affectations ON Affectations.id_ordinateur = Logiciels.id_ordinateur
JOIN Utilisateurs ON Utilisateurs.id = Affectations.id_utilisateur
WHERE Utilisateurs.nom_utilisateur = 'M. Duchmoll'
"""
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 8
@app.route('/query8')
def query8():
    query = """
SELECT Utilisateurs.*
FROM Utilisateurs
JOIN Affectations ON Affectations.id_utilisateur = Utilisateurs.id
JOIN Ordinateurs ON Ordinateurs.id = Affectations.id_ordinateur
WHERE Ordinateurs.marque_ordinateur = 'HP'
"""
    result = execute_query(query)
    return jsonify(result)
    
# Exemple de route pour la requête 9
@app.route('/query9')
def query9():
    query = """
SELECT Utilisateurs.*
FROM Utilisateurs
JOIN Affectations ON Affectations.id_utilisateur = Utilisateurs.id
JOIN Ordinateurs ON Ordinateurs.id = Affectations.id_ordinateur
WHERE Ordinateurs.marque_ordinateur = 'HP' AND Ordinateurs.systeme_exploitation = 'Windows 10'
"""
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 10
@app.route('/query10')
def query10():
    query = """
SELECT * FROM Ordinateurs
WHERE id IN (SELECT id_ordinateur FROM Maintenance WHERE date_maintenance BETWEEN '2021-10-10' AND '2021-12-10')
"""
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 11
@app.route('/query11')
def query11():
    query = """
SELECT Ordinateurs.*
FROM Ordinateurs
JOIN Maintenance ON Maintenance.id_ordinateur = Ordinateurs.id
WHERE Maintenance.technicien = 'Jean Neymar'
"""
    result = execute_query(query)
    return jsonify(result)

# Exemple de route pour la requête 12
@app.route('/query12')
def query12():
    query = """
SELECT Ordinateurs.*
FROM Ordinateurs
JOIN Maintenance ON Maintenance.id_ordinateur = Ordinateurs.id
WHERE Maintenance.technicien = 'Jean Neymar' AND YEAR(Maintenance.date_maintenance) = 2021
"""
    result = execute_query(query)
    return jsonify(result)

# Répétez le même processus pour chaque requête...

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
