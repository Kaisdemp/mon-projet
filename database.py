import sqlite3
import secrets

DB = "donnees.db"

def get_connexion():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # pour accéder aux colonnes par nom
    return conn

def init_db():
    conn = get_connexion()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sondages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            code_partage TEXT UNIQUE NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sondage_id INTEGER NOT NULL,
            texte TEXT NOT NULL,
            FOREIGN KEY (sondage_id) REFERENCES sondages(id)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            option_id INTEGER NOT NULL,
            FOREIGN KEY (option_id) REFERENCES options(id)
        )
    """)
    conn.commit()
    conn.close()

def creer_sondage(question, liste_options):
    conn = get_connexion()
    cur = conn.cursor()
    code = secrets.token_urlsafe(6)  # ex: "Xk3p9A"
    cur.execute(
        "INSERT INTO sondages (question, code_partage) VALUES (?, ?)",
        (question, code)
    )
    sondage_id = cur.lastrowid
    for texte_option in liste_options:
        cur.execute(
            "INSERT INTO options (sondage_id, texte) VALUES (?, ?)",
            (sondage_id, texte_option)
        )
    conn.commit()
    conn.close()
    return code

def get_sondage_par_code(code):
    conn = get_connexion()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sondages WHERE code_partage = ?", (code,))
    sondage = cur.fetchone()
    conn.close()
    return sondage

def get_options(sondage_id):
    conn = get_connexion()
    cur = conn.cursor()
    cur.execute("SELECT * FROM options WHERE sondage_id = ?", (sondage_id,))
    options = cur.fetchall()
    conn.close()
    return options

def ajouter_vote(option_id):
    conn = get_connexion()
    cur = conn.cursor()
    cur.execute("INSERT INTO votes (option_id) VALUES (?)", (option_id,))
    conn.commit()
    conn.close()

def get_resultats(sondage_id):
    conn = get_connexion()
    cur = conn.cursor()
    cur.execute("""
        SELECT options.texte, COUNT(votes.id) as nb_votes
        FROM options
        LEFT JOIN votes ON votes.option_id = options.id
        WHERE options.sondage_id = ?
        GROUP BY options.id
        ORDER BY nb_votes DESC
    """, (sondage_id,))
    resultats = cur.fetchall()
    conn.close()
    return resultats
