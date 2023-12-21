from faker import Faker
import random
import datetime
import uuid 

fake = Faker()

# Choix de configurations matérielles
configurations_materielles = [
    "Processeur : Intel Core i5 | Stockage : SSD 256 Go | Carte graphique : Intégrée | Écran : 21 pouces | Connectivité : Wi-Fi, Ethernet",
    "Processeur : AMD Ryzen 9 5900X |  Stockage : SSD 1 To + HDD 2 To | Carte graphique : NVIDIA GeForce RTX 3080 | Écran : 27 pouces, 4K, 144 Hz |  Refroidissement : Système de refroidissement liquide | Connectivité : Wi-Fi 6, Ethernet",
    "Processeur : Intel Core i7-12700K | Stockage : SSD NVMe 2 To | Carte graphique : NVIDIA Quadro P5000 | Écran : 32 pouces, 4K, écran tactile |  Périphériques : Tablette graphique, clavier mécanique",
    "Processeur : Intel Core i7-1185G7 |  Stockage : SSD 512 Go | Écran : 13,3 pouces Full HD | Autonomie de la batterie : Jusqu'à 12 heures | Connectivité : Wi-Fi 6, USB-C",
    "Processeur : Dual Intel Xeon E5-2699 v4 |  Stockage : RAID 10 avec 4 disques SSD 1,6 To | Carte réseau : Gigabit Ethernet, carte réseau dédiée | Redondance : Alimentation redondante, refroidissement redondant",
    "Processeur : AMD Ryzen 7 5800X |  Stockage : SSD 1 To + HDD 4 To | Carte graphique : NVIDIA GeForce RTX 3060 | Capture vidéo : Elgato 4K60 Pro | Écran : 32 pouces, 1440p, 144 Hz | Logiciel : Adobe Premiere Pro, OBS Studio"
]

# Génération de données pour la table Ordinateurs
with open("donnees_ordinateurs.csv", "w") as f:
    f.write("id;nom_ordinateur;configuration_materielle;systeme_exploitation;date_achat;date_fin_garantie;derniere_mise_a_jour;playbook_ansible;marque_ordinateur;ram_gb\n")
    noms_ordinateurs = set()
    for i in range(1, 1501):  # Générer 1500 données
        nom_ordinateur = fake.first_name() + "'s Computer"
        if nom_ordinateur in noms_ordinateurs:
            num = 1
            while f"{nom_ordinateur} {num}" in noms_ordinateurs:
                num += 1
            nom_ordinateur = f"{nom_ordinateur} {num}"
        noms_ordinateurs.add(nom_ordinateur)
        ram_gb = random.choice([4, 8, 12, 16, 20, 24, 28, 32])  # RAM entre 4 et 32 Go
        marque = random.choice(['HP', 'Dell', 'Lenovo'])  # Marque HP, Dell ou Lenovo
        date_achat = fake.date_between_dates(
            date_start=datetime.date(2018, 1, 1),
            date_end=datetime.date(2020, 12, 31)
        )  # Achat entre 2018 et 2020
        derniere_mise_a_jour = fake.date_between_dates(
            date_start=date_achat,
            date_end=datetime.date(2025, 12, 31)
        )  # Mises à jour entre ces dates
        configuration_materielle = random.choice(configurations_materielles)  # Sélection aléatoire de la configuration matérielle
        f.write(f"{i};{nom_ordinateur};{configuration_materielle};{random.choice(['Windows 10', 'Ubuntu 20.04', 'macOS'])};{date_achat};{fake.date_between_dates(date_start=date_achat, date_end=datetime.date(2025, 12, 31))};{derniere_mise_a_jour};ansible-{i}.yml;{marque};{ram_gb}\n")



with open("donnees_logiciels.csv", "w") as f:
  f.write("id;nom_logiciel;version;cle_licence;date_installation;id_ordinateur\n")
  id_logiciels = random.sample(range(1, 1501), 1500)

  for i in range(1, 1501):
      date_installation = fake.date_between_dates(
          date_start=datetime.date(2018, 1, 1),
          date_end=datetime.date(2023, 12, 31)
      )
      id_ordinateur = random.randint(1, 1500)

      # Utilisation de uuid.uuid4() pour générer un UUID unique
      cle_licence = uuid.uuid4()

      f.write(f"{i};{fake.word()};{fake.word()}.{random.randint(1, 10)};{cle_licence};{date_installation};{id_ordinateur}\n")


from faker import Faker
import random

fake = Faker("fr_FR")  # Utiliser le français comme locale

# Générer une liste de 1500 noms complets
noms_utilisateurs = [fake.name() for _ in range(1500)]

# Remplacer un nom aléatoire par "M. Duchmoll"
index_duchmoll = random.randint(0, 1499)
noms_utilisateurs[index_duchmoll] = "M. Duchmoll"

# Génération de données pour la table Utilisateurs
with open("donnees_utilisateurs.csv", "w") as f:
    f.write("id;nom_utilisateur;email;numero_telephone\n")

    for i, nom_utilisateur in enumerate(noms_utilisateurs, start=1):  # Générer 1500 données
        email = fake.email()
        numero_telephone = fake.phone_number()
        f.write(f"{i};{nom_utilisateur};{email};{numero_telephone}\n")


with open("donnees_affectations.csv", "w") as f:
  f.write("id;id_ordinateur;id_utilisateur;date_affectation\n")
  id_ordinateurs = random.sample(range(1, 1501), 1500)  # Liste d'ID d'ordinateurs uniques
  id_utilisateurs = random.sample(range(1, 1501), 1500)  # Liste d'ID d'utilisateurs uniques
  for i in range(1, 1501):  # Générer 1500 données
      id_ordinateur = id_ordinateurs.pop()  # Prendre un ID d'ordinateur unique
      id_utilisateur = id_utilisateurs.pop()  # Prendre un ID d'utilisateur unique
      date_affectation = fake.date_between_dates(
          date_start=datetime.date(2018, 1, 1),
          date_end=datetime.date(2023, 12, 31)
      )  # Affectation entre 2018 et 2023
      f.write(f"{i};{id_ordinateur};{id_utilisateur};{date_affectation}\n")



# Liste de choix de descriptions de maintenance
descriptions_maintenance = [
    "Nettoyage de la poussière et des débris accumulés",
    "Mise à jour des logiciels, du système d'exploitation et des pilotes",
    "Remplacement ou mise à niveau du matériel défectueux",
    "Optimisation des performances du disque dur",
    "Gestion de l'espace de stockage et des sauvegardes",
    "Détection et suppression de logiciels malveillants",
    "Correction d'erreurs système et de fichiers corrompus",
    "Gestion de la sécurité et des pare-feu",
    "Réparation ou remplacement de l'alimentation",
    "Vérification de la connectivité des périphériques",
    "Amélioration de la dissipation de chaleur",
    "Configuration du réseau et résolution de problèmes de connectivité",
    "Mise à niveau des composants matériels pour de meilleures performances",
    "Suppression des fichiers inutiles pour libérer de l'espace disque",
    "Résolution des problèmes d'écran, de clavier ou de souris",
    "Gestion de la mémoire virtuelle et de la RAM",
    "Configuration des paramètres d'économie d'énergie",
    "Sauvegarde régulière des données importantes",
    "Optimisation des processus de démarrage et d'arrêt",
    "Assistance pour les problèmes d'impression et de numérisation"
]

import random

# Liste de choix d'actions effectuées
actions_effectuees_list = [
    "Dépoussiérage de l'intérieur de l'ordinateur et de ses composants pour éviter la surchauffe.",
    "Installation des dernières mises à jour pour améliorer la stabilité et la sécurité.",
    "Échange ou amélioration des composants matériels défaillants.",
    "Défragmentation du disque dur et nettoyage des fichiers inutiles.",
    "Organisation des données, suppression de fichiers inutiles et sauvegarde régulière.",
    "Utilisation d'outils antivirus et antimalwares pour éliminer les menaces.",
    "Utilisation d'outils de réparation système pour restaurer la stabilité.",
    "Configuration des paramètres de sécurité pour protéger le système contre les menaces.",
    "Remplacement de l'alimentation défectueuse ou inadéquate.",
    "Diagnostic et résolution des problèmes de connectivité avec des périphériques externes.",
    "Installation de systèmes de refroidissement ou de ventilateurs supplémentaires pour éviter la surchauffe.",
    "Diagnostic et réparation des problèmes de réseau.",
    "Remplacement ou ajout de composants pour augmenter les performances.",
    "Nettoyage du disque dur en supprimant des fichiers inutilisés.",
    "Diagnostic et réparation des problèmes liés aux périphériques d'entrée.",
    "Configuration de la mémoire virtuelle et mise à niveau de la RAM pour des performances optimales.",
    "Optimisation des paramètres d'économie d'énergie pour prolonger la durée de vie de la batterie.",
    "Planification de sauvegardes automatiques pour prévenir la perte de données.",
    "Gestion des programmes au démarrage pour accélérer le processus.",
    "Diagnostic et résolution des problèmes liés aux périphériques de sortie."
]

from faker import Faker
import random
import datetime

fake = Faker("fr_FR")  # Utiliser le français comme locale

# Génération de données pour la table Maintenance
with open("donnees_maintenance.csv", "w") as f:
    f.write("id;id_ordinateur;date_maintenance;description_maintenance;actions_effectuees;technicien\n")

    id_ordinateurs = random.sample(range(1, 1501), 1500)  # Liste d'ID uniques

    # Ajout du technicien Jean Neymar avec une probabilité plus élevée
    techniciens = [fake.first_name() for _ in range(1490)] + ["Jean Neymar"] * 30
    random.shuffle(techniciens)

    for i in range(1, 1501):  # Générer 1500 données
        id_ordinateur = id_ordinateurs.pop()  # Prendre un ID unique
        date_maintenance = fake.date_between_dates(
            date_start=datetime.date(2018, 1, 1),
            date_end=datetime.date(2023, 12, 31)
        )  # Maintenance entre 2018 et 2023
        technicien = techniciens.pop()  # Sélection aléatoire d'un technicien
        description_maintenance = fake.sentence()
        # Utilisation de faker pour générer une description aléatoire
        actions_effectuees = fake.sentence()
        # Utilisation de faker pour générer une action aléatoire
        f.write(f"{i};{id_ordinateur};{date_maintenance};{description_maintenance};{actions_effectuees};{technicien}\n")




import random

# Liste de choix de descriptions de problème
descriptions_probleme_list = [
    "Nettoyage de la poussière et des débris accumulés",
    "Mise à jour des logiciels, du système d'exploitation et des pilotes",
    "Remplacement ou mise à niveau du matériel défectueux",
    "Optimisation des performances du disque dur",
    "Gestion de l'espace de stockage et des sauvegardes",
    "Détection et suppression de logiciels malveillants",
    "Correction d'erreurs système et de fichiers corrompus",
    "Gestion de la sécurité et des pare-feu",
    "Réparation ou remplacement de l'alimentation",
    "Vérification de la connectivité des périphériques",
    "Amélioration de la dissipation de chaleur",
    "Configuration du réseau et résolution de problèmes de connectivité",
    "Mise à niveau des composants matériels pour de meilleures performances",
    "Suppression des fichiers inutiles pour libérer de l'espace disque",
    "Résolution des problèmes d'écran, de clavier ou de souris",
    "Gestion de la mémoire virtuelle et de la RAM",
    "Configuration des paramètres d'économie d'énergie",
    "Sauvegarde régulière des données importantes",
    "Optimisation des processus de démarrage et d'arrêt",
    "Assistance pour les problèmes d'impression et de numérisation"
]

# Génération de données pour la table Problemes
with open("donnees_problemes.csv", "w") as f:
    f.write("id;id_ordinateur;date_probleme;description_probleme;actions_prises\n")

    # Liste d'ID d'ordinateurs uniques
    id_ordinateurs = list(range(1, 1501))
    random.shuffle(id_ordinateurs)  # Mélanger la liste des IDs ordinateurs

    for i in range(1, 1501):  # Générer 1500 données
        id_ordinateur = id_ordinateurs.pop()  # Prendre un ID d'ordinateur unique
        id_probleme = i  # Utiliser simplement l'itération comme ID de problème
        date_probleme = fake.date_between_dates(
            date_start=datetime.date(2018, 1, 1),
            date_end=datetime.date(2023, 12, 31)
        )  # Problème entre 2018 et 2023
        description_probleme = random.choice(descriptions_probleme_list)
        actions_prises = description_probleme
        f.write(f"{id_probleme};{id_ordinateur};{date_probleme};{description_probleme};{actions_prises}\n")



import random

# Liste de choix de descriptions de mise à jour
descriptions_mise_a_jour_list = [
    "Mise à jour du système d'exploitation pour bénéficier des dernières fonctionnalités et correctifs de sécurité",
    "Mise à jour des pilotes matériels (carte graphique, son, réseau, etc.) pour assurer une compatibilité et des performances optimales",
    "Mise à jour des logiciels applicatifs pour bénéficier de nouvelles fonctionnalités et améliorations de stabilité",
    "Mise à jour du firmware du matériel, y compris du BIOS, pour résoudre des problèmes de compatibilité matérielle et de sécurité",
    "Mise à jour des antivirus et des logiciels de sécurité pour maintenir une protection adéquate contre les menaces en ligne",
    "Mise à jour des navigateurs web pour des performances optimales et une meilleure sécurité de navigation",
    "Mise à jour des plug-ins et extensions du navigateur pour éviter les vulnérabilités de sécurité",
    "Mise à jour des bibliothèques système pour garantir la stabilité et la sécurité du système d'exploitation",
    "Mise à jour des paramètres de sécurité pour renforcer la protection des données et de la vie privée",
    "Mise à jour des sauvegardes pour inclure de nouvelles données et assurer leur accessibilité en cas de besoin",
    "Mise à jour des certificats numériques pour garantir la sécurité des connexions chiffrées",
    "Mise à jour des plugins et des extensions du logiciel de productivité (comme Microsoft Office) pour bénéficier de nouvelles fonctionnalités et de correctifs de sécurité",
    "Mise à jour des systèmes de gestion de contenu (CMS) pour maintenir la sécurité et la stabilité des sites web",
    "Mise à jour des applications mobiles pour accéder aux dernières fonctionnalités et corriger les bugs",
    "Mise à jour des paramètres de pare-feu pour une meilleure sécurité du réseau",
    "Mise à jour des paramètres de confidentialité pour protéger les informations personnelles",
    "Mise à jour des paramètres de contrôle parental pour surveiller et protéger les activités en ligne des enfants",
    "Mise à jour des systèmes de virtualisation pour des performances et une sécurité améliorées",
    "Mise à jour des outils de développement pour rester compatibles avec les nouvelles technologies",
    "Mise à jour des systèmes de gestion des données pour optimiser les performances et l'accès aux informations"
]

# Génération de données pour la table MisesAJour
with open("donnees_misesajour.csv", "w") as f:
    f.write("id;id_ordinateur;date_mise_a_jour;description_mise_a_jour\n")
    id_ordinateurs = random.sample(range(1, 1501), 1500)  # Liste d'ID d'ordinateurs uniques
    for i in range(1, 1501):  # Générer 1500 données
        id_ordinateur = id_ordinateurs.pop()  # Prendre un ID d'ordinateur unique
        date_mise_a_jour = fake.date_between_dates(
            date_start=datetime.date(2018, 1, 1),
            date_end=datetime.date(2025, 12, 31)
        )  # Mise à jour entre 2018 et 2025
        description_mise_a_jour = random.choice(descriptions_mise_a_jour_list)  # Sélection aléatoire de la description de mise à jour
        f.write(f"{i};{id_ordinateur};{date_mise_a_jour};{description_mise_a_jour}\n")
