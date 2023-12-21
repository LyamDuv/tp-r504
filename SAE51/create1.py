import mysql.connector

# Informations de connexion à la base de données
DB_USER = "etudiant"
DB_PASS = "Abricotdu7"
DB_NAME = "GestionParcInformatique"

# Connexion à la base de données MySQL
conn = mysql.connector.connect(user=DB_USER, password=DB_PASS)
cursor = conn.cursor()

# Commande pour créer la base de données
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
conn.database = DB_NAME

# Table Ordinateurs
cursor.execute("""
CREATE TABLE IF NOT EXISTS Ordinateurs (
  id int NOT NULL AUTO_INCREMENT,
  nom_ordinateur varchar(255) NOT NULL,
  configuration_materielle text,
  systeme_exploitation varchar(255),
  date_achat date,
  date_fin_garantie date,
  derniere_mise_a_jour date,
  playbook_ansible varchar(255),
  marque_ordinateur varchar(255),
  ram_gb int,
  PRIMARY KEY (id)
)
""")

# Table Logiciels
cursor.execute("""
CREATE TABLE IF NOT EXISTS Logiciels (
  id int NOT NULL AUTO_INCREMENT,
  nom_logiciel varchar(255) NOT NULL,
  version varchar(255) NOT NULL,
  cle_licence varchar(255),
  date_installation date,
  id_ordinateur int,
  PRIMARY KEY (id),
  FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id)
);""")

# Table Utilisateurs
cursor.execute("""
CREATE TABLE IF NOT EXISTS Utilisateurs (
  id int NOT NULL AUTO_INCREMENT,
  nom_utilisateur varchar(255) NOT NULL,
  email varchar(255),
  numero_telephone varchar(255),
  PRIMARY KEY (id)
);
""")

# Table Affectations
cursor.execute("""
CREATE TABLE IF NOT EXISTS Affectations (
  id int NOT NULL AUTO_INCREMENT,
  id_ordinateur int,
  id_utilisateur int,
  date_affectation date,
  PRIMARY KEY (id),
  FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id),
  FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id)
)
""")

# Table Maintenance
cursor.execute("""
CREATE TABLE IF NOT EXISTS Maintenance (
  id int NOT NULL AUTO_INCREMENT,
  id_ordinateur int,
  date_maintenance date,
  description_maintenance text,
  actions_effectuees text,
  technicien varchar(255),
  PRIMARY KEY (id),
  FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id)
)
""")

# Table Problemes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Problemes (
  id int NOT NULL AUTO_INCREMENT,
  id_ordinateur int,
  date_probleme date,
  description_probleme text,
  actions_prises text,
  PRIMARY KEY (id),
  FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id)
)
""")

# Table MisesAJour
cursor.execute("""
CREATE TABLE IF NOT EXISTS MisesAJour (
  id int NOT NULL AUTO_INCREMENT,
  id_ordinateur int,
  date_mise_a_jour date,
  description_mise_a_jour text,
  PRIMARY KEY (id),
  FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id)
)
""")

# Fermer la connexion à la base de données
cursor.close()
conn.close()
