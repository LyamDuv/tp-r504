#!/bin/bash


docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images)
docker network prune -f

rm -f /home/user/shared/dbml-error.log
rm -f /home/user/shared/sae51.sql
rm -f /home/user/shared/sae51.svg
rm -f /home/user/shared/sae51.png
rm -f /home/user/donnees_affectations.csv
rm -f /home/user/donnees_logiciels.csv
rm -f /home/user/donnees_maintenance.csv
rm -f /home/user/donnees_misesajour.csv
rm -f /home/user/donnees_ordinateurs.csv
rm -f /home/user/donnees_problemes.csv
rm -f /home/user/donnees_utilisateurs.csv
