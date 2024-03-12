#!/bin/bash

# Chemin vers le script de scan
scan_script="/home/user/tp-r504/TP14/scan.sh"

# Chemin vers le fichier de crontab temporaire
tempo="/tmp/temp_cron_file"

# Ligne de crontab à ajouter
crone="30 2 * * * $scan_script"
#crone="* * * * * $scan_script"
# Création du fichier temporaire avec la nouvelle crontab
echo "$crone" > "$tempo"

# Installer la nouvelle crontab
crontab "$tempo"

# Supprimer le fichier temporaire
rm "$tempo"

