# Procédure de déploiement — VotezPour

## 🎯 Objectif
Déployer l'application VotezPour sur une VM Debian et la rendre accessible.

## 📋 Prérequis
- VM Debian à jour
- Accès Internet
- Le code sur le dépôt Git : https://github.com/Kaisdemp/mon-projet

## Étape 1 — Préparer l'environnement
1. sudo apt update && sudo apt upgrade -y
2. sudo apt install python3 python3-pip git -y
3. Vérifier : python3 --version / pip3 --version / git --version

## Étape 2 — Récupérer et installer l'application
1. git clone https://github.com/Kaisdemp/mon-projet
2. cd mon-projet
3. pip3 install -r requirements.txt

## Étape 3 — Lancer l'application (local)
1. python3 app.py
2. Vérifier : ouvrir http://127.0.0.1:5000 sur la VM
3. Pour garder l'app active en continu : nohup python3 app.py &

## Étape 4 — Rendre accessible sur le réseau (LAN)
1. Modifier app.run(host="0.0.0.0", port=5000) dans app.py
2. sudo apt install ufw -y
3. sudo ufw allow 5000
4. sudo ufw enable
5. Récupérer l'IP : ip a
6. Tester depuis un autre PC : http://[IP]:5000

## Étape 5 — Mettre en ligne (bonus, optionnel)
1. Installer cloudflared
2. cloudflared tunnel --url http://localhost:5000
3. Partager l'URL publique obtenue

## ✅ Validation
- [ ] La page d'accueil s'affiche
- [ ] On peut créer un sondage
- [ ] On peut voter
- [ ] Les résultats s'affichent en direct
- [ ] (LAN) Accessible depuis un autre PC
- [ ] (Bonus) Accessible en ligne

## 🔒 Checklist sécurité appliquée
- [x] Requêtes SQL paramétrées
- [ ] Secrets dans .env (ignoré par Git)
- [ ] debug=False en production
- [ ] Pare-feu : seul le port 5000 ouvert
