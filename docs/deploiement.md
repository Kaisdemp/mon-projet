# Procédure de déploiement — VotezPour

## 🎯 Objectif
Déployer l'application VotezPour sur une VM Debian et la rendre accessible.

## 📋 Prérequis
- VM Debian à jour
- Accès Internet
- Le code sur le dépôt Git : <url-de-ton-repo>

## Étape 1 — Préparer l'environnement

1. Mettre à jour le système :
```bash
   sudo apt update && sudo apt upgrade -y
```
2. Installer Python, pip et Git :
```bash
   sudo apt install python3 python3-pip git -y
```
3. Vérifier les installations :
```bash
   python3 --version
   pip3 --version
   git --version
```

## Étape 2 — Récupérer et installer l'application

1. Cloner le dépôt :
```bash
   git clone <url-de-ton-repo>
   cd votepour
```
2. Installer les dépendances :
```bash
   pip3 install -r requirements.txt
```

## Étape 3 — Lancer l'application (local)

1. Démarrer le serveur :
```bash
   python3 app.py
```
2. Vérifier : ouvrir `http://127.0.0.1:5000` sur la VM
3. Pour garder l'app active en continu :
```bash
   nohup python3 app.py &
```

## Étape 4 — Rendre accessible sur le réseau local (LAN)

1. Modifier le lancement dans `app.py` :
```python
   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
```
2. Ouvrir le port dans le pare-feu :
```bash
   sudo apt install ufw -y
   sudo ufw allow 5000
   sudo ufw enable
   sudo ufw status
```
3. Récupérer l'adresse IP de la VM :
```bash
   ip a
```
4. Tester depuis un autre PC du réseau : http://<IP-de-la-VM>:5000

## Étape 5 — Mettre en ligne (bonus, optionnel)

1. Installer cloudflared :
```bash
   wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
   sudo dpkg -i cloudflared-linux-amd64.deb
```
2. Lancer le tunnel :
```bash
   cloudflared tunnel --url http://localhost:5000
```
3. Partager l'URL publique obtenue (type `https://xxxx.trycloudflare.com`)

## ✅ Validation
- [ ] La page d'accueil s'affiche
- [ ] On peut créer un sondage
- [ ] On peut voter
- [ ] Les résultats s'affichent avec les barres de progression
- [ ] (LAN) Accessible depuis un autre PC
- [ ] (Bonus) Accessible en ligne via Cloudflare

## 🔒 Checklist sécurité appliquée
- [ ] Requêtes SQL paramétrées (vérifié dans `database.py`)
- [ ] Secrets dans `.env`, ignoré par Git
- [ ] `debug=False` avant la démo / mise en ligne
- [ ] Pare-feu : seul le port 5000 ouvert
