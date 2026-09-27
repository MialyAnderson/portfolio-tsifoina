# Portfolio de Tsifoina RANDRIANARIVONANTOANINA

Site Flask, une seule page, palette bleu marine.

## Lancer en local

    pip install -r requirements.txt
    python app.py

Puis ouvrir http://127.0.0.1:5000

## Modifier le contenu

Tout le texte est dans `content.py` (profil, parcours, expériences, projets, contact).
Les images sont dans `static/img/`. Pour ajouter une photo à un projet, déposez-la
dans ce dossier et ajoutez son nom à la liste `images` du projet.

Le lien LinkedIn est vide pour l'instant : renseignez `CONTACT["linkedin"]["url"]`.

## Déployer sur Render

- Build command : `pip install -r requirements.txt`
- Start command : `gunicorn app:app`

## Structure

    app.py            routes Flask
    content.py        tout le contenu
    templates/        base.html, index.html, 404.html
    static/css/       style.css (couleurs dans :root)
    static/js/        menu mobile, onglets des projets, visionneuse d'images
    static/img/       photos optimisées
