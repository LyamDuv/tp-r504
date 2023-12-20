import mysql.connector
import csv

# Informations de connexion à la base de données
DB_USER = "etudiant"
DB_PASS = "Abricotdu7"
DB_NAME = "GestionParcInformatique"

# Connexion à la base de données MySQL
conn = mysql.connector.connect(user=DB_USER, password=DB_PASS)
cursor = conn.cursor()

conn.database = DB_NAME

def insert_data_from_csv(csv_filename, table_name, delimiter=';'):
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        next(csv_reader)  # Pour sauter la ligne d'en-tête
        for row in csv_reader:
            # Créez la commande SQL d'insertion
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})"
            cursor.execute(insert_query, row)

# Insérer des données dans la table Ordinateurs à partir du fichier CSV avec des délimiteurs de point-virgule
insert_data_from_csv('donnees_ordinateurs.csv', 'Ordinateurs', delimiter=';')

insert_data_from_csv('donnees_logiciels.csv', 'Logiciels', delimiter=';')

insert_data_from_csv('donnees_maintenance.csv', 'Maintenance', delimiter=';')

insert_data_from_csv('donnees_misesajour.csv', 'MisesAJour', delimiter=';')

insert_data_from_csv('donnees_utilisateurs.csv', 'Utilisateurs', delimiter=';')

insert_data_from_csv('donnees_problemes.csv', 'Problemes', delimiter=';')

insert_data_from_csv('donnees_affectations.csv', 'Affectations', delimiter=';')



# Insérer des données dans d'autres tables de la même manière

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()
