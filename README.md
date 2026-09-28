# Basic SQL Injection Lab

Ce projet est un environnement de test minimaliste pour comprendre les attaques par injection SQL (SQLi) et comment s'en protéger. Il contient deux applications Flask distinctes pour comparer directement un code vulnérable et sa version sécurisée.

## Prérequis
- Python 3.x

## Installation

Il est recommandé d'utiliser un environnement virtuel pour ne pas polluer votre installation Python globale.

1. Créez et activez l'environnement virtuel (`venv`) :
   ```bash
   python -m venv venv
   
   # Sur Windows :
   .\venv\Scripts\activate
   # Sur Linux/Mac :
   source venv/bin/activate
   ```

2. Installez la dépendance Flask :
   ```bash
   pip install -r requirements.txt
   ```

3. Initialisez la base de données SQLite locale :
   ```bash
   python init_database.py
   ```
   *Note : Cette commande crée le fichier `database.db` et y insère un compte administrateur de test.*

## Démonstration

### 1. Exploiter la faille
Lancez le premier serveur web :
```bash
python vulnerable.py
```
Allez sur `http://127.0.0.1:5000` et testez ce payload dans le champ **Username** (avec un mot de passe aléatoire) :
`' OR '1'='1`

**Ce qui se passe :** Le code utilise une concaténation basique (`f"SELECT ... '{username}'"`). Le payload modifie la structure même de la requête SQL, rendant la condition toujours vraie. L'authentification est contournée.

### 2. Vérifier la correction
Fermez le serveur précédent (Ctrl+C dans le terminal) et lancez la version sécurisée :
```bash
python secured.py
```
Testez le même payload `' OR '1'='1`. L'attaque va cette fois échouer.

**Ce qui se passe :** Ce code utilise des requêtes préparées (Parameterized queries avec le symbole `?`). Le moteur de la base de données traite les entrées de l'utilisateur strictement comme du texte (des chaînes de caractères littérales) et non comme des commandes SQL exécutables. La faille est neutralisée.

## Identifiants de test
Pour tester le comportement normal de l'application (sans injection), vous pouvez utiliser le compte généré par défaut :
- **Username :** `admin`
- **Password :** `password!`
