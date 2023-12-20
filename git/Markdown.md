## Voici le markdown de notre projet SAE51 : Solution technique 

- Le script `Generer.py` a pour fonction de créer les données CSV nécessaires aux différentes tables de notre base de données.

- Le fichier `Run_converter.sh` permet de convertir le fichier DBML de notre base de données en fichiers SQL et SVG. Il lance un conteneur qui effectue cette action et le supprime une fois la tâche réalisée.

- Le script `Donnee.py` est dédié à la création des données.

- `Create.py` est utilisé pour créer la base de données.

- `Import.py` facilite l'importation des données CSV dans les tables de la base de données.

- Le fichier `Dockerfile` est conçu pour créer un conteneur générant un fichier SVG et la base MySQL.

- `Dockerfile` (mentionné à nouveau) est employé pour créer un conteneur Ubuntu sur lequel le serveur MySQL est installé.

- `Dockerfile2` est utilisé pour créer un serveur web.

- `Request.py` permet d'interroger notre base de données, envoyer des requêtes et afficher les résultats.

- `Request2.py` est spécifiquement conçu pour interroger la base de données et afficher les résultats sur le site web.

- Le script `Auto.sh` a pour fonction d'automatiser l'ensemble du processus.

- `Purge.sh` est utilisé pour supprimer tous les conteneurs, les images Docker et les fichiers créés par les autres scripts.

## Développement du Projet

Initialement, Laurent était responsable de la création d'un script pour générer les données CSV et le fichier DBML, tandis que Lyam et Ibrahim travaillaient sur les scripts pour créer la base de données et importer les données CSV dans ses tables, ce qui a été par la suite adapté par Laurent et Lyam pour répondre aux nouvelles conditions demandées. Ensuite, Lyam s'est chargé du Dockerfile de la base de données MySQL, Laurent du Dockerfile pour transformer le fichier DBML en fichiers SQL et SVG. Enfin, Ibrahim s'est occupé du développement du projet pour afficher les données et les requêtes de la base de données sur le web à l'aide d'un script écrit par lui-même et Lyam.

## Comment faire fonctionner notre projet ?


Il suffit de télécharger nos fichiers et de lancer auto.sh !