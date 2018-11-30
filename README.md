# MOPS TP01 - Détecter les sites de phishing
## Détecter un site de phishing
**Variables:**
- Variation d'url
- Js malveillant
- Orthographe
- Google traduction
- Verification d'identifiant
- Date de réservation du nom de domaine
- Comparer protocole utilisé
- Mauvaise conf HTTPS
- Protocole de la CA
- Demande de données bancaire
- Utiliser un antivirus
- Comparer les fréquences de visite avec celles attendu
- Conformité RGPD
- Redirection vers des sites URL
- Distance whois
- Comparer l'hébergeur
- Géolocalisation
- Réputation d'IP
- Réputation d'AS
- Comparer distance réseau (traceroute)


## Filtres
**Les filtres sont triés par ordre de priorités, le premier étant le plus prioritaire.**
- Tester service web
  - Validation si il y a une réponse du port 80 ou 443
- Tester si il y a une redirection
  -  Refus si redirection vers un autre domaine
- Analyse des liens (href)
  - Validation si le pourcentage de domaine (contenu sur la page) est suffisant pour être valide. Si le site de phishing posséde aucun lien href vers son domaine, alors il ne sera pas validé.
- Analyse ip et/ou domaine
  - Validation du domain ou de l'IP si il/elle n'est pas blacklisté
- Variation d'url, lib python

## Evaluation d'un site
- Chaque filtre retourne 1 ou 0, (1 si une menace est détéctée)
- On fait la moyenne (nombre de menaces / nombres de filtres), ce qui nous donne le taux de menace/
- Si, le taux de menace est trop élvevé (à defini), alors on léve une alerte.
- Ajout de l'alerte dans le fichier de log, ex { DateTime ; site ; niveau de menace, filtre }

## Implémentation
- Creation des filtres, utiisation de lib
- Evaluation de l'url
- Création de log
