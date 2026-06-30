# Journal de bord — VotezPour

---

## 📅 MARDI 30 juin 2026

### ✅ Fait aujourd'hui
- Rédaction du PRD en équipe
- Création du dépôt Git et invitation des collaborateurs
- Mise en place de l'environnement Flask (venv, installation des dépendances)
- Structure du projet créée (app.py, database.py, templates/, static/)
- "Hello World" Flask fonctionnel
- Schéma de base de données conçu (sondages, options, votes)
- Routes principales codées : accueil, création de sondage, vote, résultats
- Requêtes SQL paramétrées dans database.py
- Design de l'interface (carte centrée, dégradé, barres de résultats animées)
- Premiers commits poussés sur main



### 🔀 Décisions prises
- Stack imposée : Python + Flask + SQLite + Debian
- Pas de système de comptes pour rester dans le MVP
- Code de partage du sondage généré avec `secrets.token_urlsafe`

### 🤖 Prompts IA utiles
- Génération de la structure SQLite pour sondages/options/votes
- Aide à la création du design CSS (carte centrée, barres de résultats)

### 🎯 Pour demain
- Système : tester le déploiement de l'app sur la VM Debian (Étape 1, en local)
- Dev : nettoyer le code, ajouter la validation des champs vides
- Chef de projet : avancer sur la documentation et préparer le pitch

---

## 📅 MERCREDI
- Installation de Flask sur la VM Debian (résolution de l'erreur "externally-managed-environment" avec --break-system-packages)
- Premier déploiement réussi en local sur la VM
- Test complet du parcours : création de sondage, vote, affichage des résultats

---

## 📅 JEUDI 

- Configuration du mode Bridge sur VirtualBox pour la VM Debian
- Ouverture du port 5000 avec ufw
- Modification de app.py pour écouter sur host="0.0.0.0"
- Mise en place de la gestion des secrets via .env (SECRET_KEY)
- Désactivation du mode debug (debug=False)
- Test réussi : application accessible depuis un autre PC sur le réseau local
- Diagnostic réseau réalisé (ping, curl) pour valider la connectivité

### 🚧 Bloqué sur
- Erreur "Address already in use" sur macOS (AirPlay Receiver) — résolu en changeant de port
- ModuleNotFoundError dotenv sur la VM — résolu en réinstallant les dépendances
---


