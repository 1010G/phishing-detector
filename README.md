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
  - Validation si le pourcentage de domaine (contenu sur la page) est suffisant pour être valide. Si le site de phishing ne possède aucun lien href vers son domaine, alors il ne sera pas validé.
- Analyse ip et/ou domaine
  - Validation du domain ou de l'IP si il/elle n'est pas blacklisté
- Variation d'url, lib python

## Evaluation d'un site
- Chaque filtre retourne 1 ou 0, (1 si une menace est détectée)
- On fait la moyenne (nombre de menaces / nombres de filtres), ce qui nous donne le taux de menace
- Si le taux de menace est trop élevé (à definir), alors on lève une alerte.
- Ajout de l'alerte dans le fichier de log, ex { DateTime ; site ; niveau de menace, filtre }

### Implémentation
- Creation des filtres, utiisation de lib
    - Filtres dans /src/filters
- Evaluation de l'url
- Création de log
    - todo

### Réalisation et utilisation du script
Contrairement au [projet de x0rz](https://github.com/x0rz/phishing_catcher), nous ne faisons pas qu'analyser le domaine. Nous effectuons aussi des tentatives de connexions sur les sites web, ce qui prend du coup plus de temps.

Il faut du coup faire plus attentions aux vérifications que nous allons effectuer. Par exemple, la vérification de certificat n'est pas pertinente vu que notre entrée vient justement d'un flux de certifications.

Par ailleurs, il est important de ne pas query trop d'informations via diverses API ou web fetch, il faut essayer d'être au maximum rapide sur l'évaluation de l'url. Une autre idée aurait été de limiter le scope de nos URL, en ne prenant qu'un domaine précis, ou un LTD précis.

Pour le moment, analyser 300 URLs nous prend environ 7 minutes, ce qui est déjà assez conséquent. Un fichier de sortie est disponible à cette [URL](https://github.com/DylanGnd/phishing-detector/blob/master/out.json).

#### Sources de sites malveillants
https://feeds.inthreat.com/osint/json/
