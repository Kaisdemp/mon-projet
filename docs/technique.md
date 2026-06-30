# Documentation technique — VotezPour

## 🏗️ Architecture
Navigateur → Flask (app.py) → database.py → Base SQLite (donnees.db)

(Schéma Draw.io à insérer ici)

## 🛠️ Stack technique
- Langage : Python 3.x
- Framework web : Flask
- Base de données : SQLite
- Hébergement : Debian
- Versioning : Git / GitHub

## 📁 Structure du projet
mon-projet/
├── app.py              # routes et lancement
├── database.py         # gestion base de données
├── requirements.txt    # dépendances
├── templates/           # pages HTML (index, sondage, resultats)
└── static/
└── style.css        # design

## 🗄️ Base de données

### Table : sondages
| Colonne | Type | Description |
|---------|------|-------------|
| id | INTEGER | Clé primaire |
| question | TEXT | La question posée |
| code_partage | TEXT | Code unique utilisé dans l'URL de partage |

### Table : options
| Colonne | Type | Description |
|---------|------|-------------|
| id | INTEGER | Clé primaire |
| sondage_id | INTEGER | Référence vers le sondage parent |
| texte | TEXT | Le texte de l'option proposée |

### Table : votes
| Colonne | Type | Description |
|---------|------|-------------|
| id | INTEGER | Clé primaire |
| option_id | INTEGER | Référence vers l'option votée |

## 🔗 API / Routes

| Méthode | URL | Rôle | Paramètres |
|---------|-----|------|------------|
| GET | / | Page de création de sondage | - |
| POST | /creer | Créer un nouveau sondage | question, option1, option2, option3 |
| GET | /sondage/<code> | Afficher le sondage et voter | - |
| POST | /voter/<code> | Enregistrer un vote | option_id |
| GET | /resultats/<code> | Afficher les résultats en direct | - |

## 💻 Installation (environnement de développement)
1. git clone https://github.com/Kaisdemp/mon-projet
2. cd mon-projet
3. pip install -r requirements.txt
4. python app.py
5. Ouvrir http://127.0.0.1:5000
