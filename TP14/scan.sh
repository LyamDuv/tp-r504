#!/bin/bash

# Chemin vers le fichier de sortie du rapport de vulnérabilités
sortie_texte="/home/user/tp-r504/TP14/result.txt"
sortie_html="/home/user/tp-r504/TP14/result.html"
# Adresse e-mail pour envoi de l'alerte
#adresse_email=

# Exécute la commande debsecan et enregistre le résultat dans le fichier de sortie texte
debsecan --suite=bullseye > "$sortie_texte"
echo "Nombre de CVE:" >> "$sortie_texte"
debsecan --suite=bullseye | wc -l >> "$sortie_texte"
echo "L'heure du scan $(date +'%H:%M:%S')" >> "$sortie_texte"


# Générer le fichier de sortie HTML
echo "<html><head><title>Rapport de vulnérabilités</title>" > "$sortie_html"
echo "<style>body { text-align: center; }</style>" >> "$sortie_html"
echo "</head><body>" >> "$sortie_html"
echo "<h1>Rapport de vulnérabilités</h1>" >> "$sortie_html"
echo "<p>Nombre de CVE: $(debsecan --suite=bullseye | wc -l)</p>" >> "$sortie_html"
echo "<p>L'heure du scan: $(date +'%H:%M:%S')</p>" >> "$sortie_html"

# Vérifier si le nombre de CVE est supérieur à 500
nombre_cve=$(debsecan --suite=bullseye | wc -l)
if [ "$nombre_cve" -gt 500 ]; then
    echo "<p style='color:red;'>Attention! Le nombre de CVE est supérieur à 500. Veuillez vérifier le système.</p>" >> "$sortie_html"
    
    # Envoyer un e-mail d'alerte
    if command -v mail &> /dev/null; then
        echo "Attention! Le nombre de CVE est supérieur à 500. Veuillez vérifier le système." | mail -s "Alerte CVE" "$adresse_email"
        echo "<p>Un e-mail d'alerte a été envoyé à $adresse_email.</p>" >> "$sortie_html"
    else
        echo "<p style='color:red;'>Erreur: la commande 'mail' n'est pas disponible. Impossible d'envoyer un e-mail.</p>" >> "$sortie_html"
    fi
fi


echo "</body></html>" >> "$sortie_html"
