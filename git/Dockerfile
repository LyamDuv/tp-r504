# Utiliser l'image Ubuntu 22.04
FROM ubuntu:22.04

# Installer sudo
RUN apt-get update

# Installer python3 et MySQL
RUN apt-get install -y python3
RUN apt-get install -y  mysql-server
RUN apt-get install -y  python3-pip

# Installer le connecteur MySQL pour Python
RUN pip install mysql-connector-python



# Créer un utilisateur MySQL nommé 'etudiant' avec le mot de passe 'Abricotdu7'
RUN service mysql start && \
    mysql -e "CREATE USER 'etudiant'@'localhost' IDENTIFIED BY 'Abricotdu7';" && \
    mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'etudiant'@'localhost';" && \
    mysql -e "FLUSH PRIVILEGES;"
    
RUN echo "[mysqld]" >> /etc/mysql/my.cnf && \
    echo "bind-address = 0.0.0.0" >> /etc/mysql/my.cnf

# Copier les fichiers t.py et e.py
COPY create1.py /app/create1.py
COPY import.py /app/import.py
COPY donnees_utilisateurs.csv /etc/donnees_utilisateurs.csv
COPY donnees_affectations.csv /etc/donnees_affectations.csv
COPY donnees_logiciels.csv /etc/donnees_logiciels.csv
COPY donnees_maintenance.csv /etc/donnees_maintenance.csv
COPY donnees_misesajour.csv /etc/donnees_misesajour.csv
COPY donnees_ordinateurs.csv /etc/donnees_ordinateurs.csv
COPY donnees_problemes.csv /etc/donnees_problemes.csv
COPY request.py /app/request.py
COPY /shared/sae51.sql /etc/sae51.sql
COPY create2.py /app/create2.py


# Définir le répertoire de travail
WORKDIR /etc

CMD service mysql start && mysql -e "CREATE USER 'etudiant'@'%' IDENTIFIED BY 'Abricotdu7';" && mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'etudiant'@'%';"  && python3 /app/create2.py && python3 /app/import.py && bash
