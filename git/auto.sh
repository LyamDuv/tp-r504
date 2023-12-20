#!/bin/bash

#sudo apt-get update 
#sudo apt-get install -y python3 python3-pip 
#sudo pip3 install faker 
echo "Génération des données..."
python3 Donnees.py 
echo "Génération terminée"
sleep 30

echo "création du SVG+SQL"
./run_converter.sh

echo "Creation réseau docker nommée web_net"
docker network create web_net

echo "Création de la base de données"
docker build -t mysql_sae51 .
docker run  -it -d -p 3306:3306 --network web_net --name SAE51 mysql_sae51

#docker exec -it SAE51 bash
echo "Attente : mise en place des données"
sleep 1m
echo "Base de données focntionnel"

python3 request.py 

echo "Création de la page web"
docker build -t web -f Dockerfile2 .
docker run -d --network web_net -p 5000:5000 -p 80:80 --name flask web

./url.sh
