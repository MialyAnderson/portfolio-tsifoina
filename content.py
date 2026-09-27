"""Tout le contenu du portfolio. Modifier ce fichier suffit pour mettre le site à jour."""

PROFILE = {
    "name": "Tsifoina",
    "surname": "RANDRIANARIVONANTOANINA",
    "roles": ["Communication", "Coordination de projets", "Entrepreneuriat"],
    "tagline": "Transformer les idées en projets, et les projets en actions.",
    "intro": [
        "Je suis une jeune professionnelle engagée dans des projets à la croisée de la "
        "communication, de la coordination, du développement des compétences et de l'entrepreneuriat.",
        "Mon parcours m'a permis d'évoluer dans des environnements variés (projets jeunesse, "
        "événements, communication digitale, enseignement, recherche et entrepreneuriat) avec un "
        "même fil conducteur : faire avancer les projets et contribuer à leur impact.",
    ],
    "portrait": "portrait.jpg",
}

DIMENSIONS = [
    {"verb": "Communiquer", "text": "Donner une identité, une visibilité et une voix aux projets."},
    {"verb": "Coordonner", "text": "Transformer une idée en organisation concrète et mobiliser les personnes autour d'un objectif commun."},
    {"verb": "Transmettre", "text": "Partager des connaissances, accompagner les apprentissages et contribuer au développement des compétences."},
    {"verb": "Entreprendre", "text": "Créer, expérimenter et transformer une idée personnelle en initiative concrète."},
]

JOURNEY = [
    "Sciences humaines & politiques",
    "Recherche & environnement institutionnel",
    "Communication & événementiel",
    "Coordination de projets jeunesse",
    "Transmission & formation",
    "Entrepreneuriat créatif",
]

EXPERIENCES = [
    {
        "title": "Coordonner & comprendre",
        "items": [
            {"org": "CENI Madagascar", "role": "Stagiaire", "year": "2024"},
            {"org": "ALTEC Madagascar", "role": "Assistante administrative et recherche", "year": "2024"},
            {"org": "HCDDED", "role": "Stagiaire", "year": "2025"},
            {
                "org": "Youth for Global Impact · PAISJ",
                "role": "Coordonnatrice nationale du Programme Intégré pour l'Autonomisation et l'Insertion Socio-économique des Jeunes",
                "year": "2026",
            },
        ],
    },
    {
        "title": "Communiquer & valoriser",
        "items": [
            {"org": "Madagascar MUN 2026", "role": "Community manager", "year": "2026"},
            {"org": "FilGOOD & Déco by AT", "role": "Community manager", "year": ""},
        ],
    },
    {
        "title": "Transmettre & accompagner",
        "items": [
            {"org": "Lycée Moderne Ampefiloha | Lycée Technique Ampefiloha", "role": "Enseignante stagiaire de français", "year": "2026"},
            {"org": "CEG Andoharanofotsy | Collège Charles Renel Mahajanga", "role": "Enseignante stagiaire de français", "year": "2025"},
        ],
    },
]

PROJECT_GROUPS = [
    {
        "id": "communication",
        "label": "Communication",
        "headline": "Donner une voix et une identité aux projets",
        "intro": "La communication est l'un des fils conducteurs de mon parcours. À travers mes expériences "
                 "associatives, événementielles et entrepreneuriales, j'ai travaillé sur la stratégie, la création "
                 "de contenus, les réseaux sociaux et la valorisation de projets.",
        "skills": ["Adobe Express", "Canva", "CapCut", "IA générative"],
        "projects": [
            {
                "title": "Madagascar MUN 2026",
                "role": "Responsable étudiante de la communication & community manager",
                "text": ["Mon implication dans Madagascar MUN m'a permis de participer à la communication d'un "
                         "événement en travaillant à la fois sur la stratégie et sur la production de contenus."],
                "list_title": "Mes interventions",
                "list": [
                    "Plan de communication",
                    "Ligne éditoriale",
                    "Gestion des réseaux sociaux et création de contenus",
                    "Supports graphiques et charte de l'événement",
                    "Coordination de l'équipe étudiante de communication",
                ],
                "link": {"label": "Page Facebook de Madagascar MUN", "url": "https://www.facebook.com/MadagascarMUN"},
                "images": ["mun-com-1.jpg", "mun-com-2.jpg", "mun-com-3.jpg"],
            },
            {
                "title": "FilGOOD & Déco by AT",
                "role": "Communication digitale & community management",
                "text": ["Mon projet entrepreneurial m'a également permis de développer une expérience concrète "
                         "en communication digitale."],
                "list_title": "Pour ma propre marque, je travaille sur",
                "list": [
                    "Création de contenus et présence sur les réseaux sociaux",
                    "Stratégie de vente et mise en valeur des produits",
                    "Identité visuelle",
                    "Storytelling",
                    "Communication avec la communauté",
                ],
                "after": "Être entrepreneuse m'a permis de comprendre la communication non seulement comme un "
                         "outil de visibilité, mais comme une manière de créer une relation avec une communauté, "
                         "et d'en engendrer du profit.",
                "images": ["filgood-3.jpg", "filgood-4.jpg", "filgood-5.jpg", "filgood-2.jpg", "filgood-1.jpg"],
            },
        ],
    },
    {
        "id": "coordination",
        "label": "Coordination & événementiel",
        "headline": "Transformer les idées en actions organisées",
        "intro": "La coordination est une dimension centrale de mon parcours. Elle m'amène à travailler sur "
                 "l'organisation, le suivi, la communication entre les acteurs, la logistique et la mise en "
                 "œuvre concrète des projets.",
        "projects": [
            {
                "title": "PAISJ 2026",
                "role": "Coordinatrice nationale du Programme Intégré pour l'Autonomisation et l'Insertion Socio-économique des Jeunes",
                "text": ["Un programme orienté vers l'inclusion, le développement des compétences et l'insertion "
                         "socio-économique des jeunes."],
                "list_title": "Mon rôle",
                "list": [
                    "Coordination des activités du programme au niveau national",
                    "Organisation et suivi des formations",
                    "Coordination avec les partenaires, les acteurs impliqués et l'équipe d'organisation",
                    "Suivi des participants",
                    "Appui à la mise en œuvre des activités",
                ],
                "pairs_title": "Une expérience au croisement de plusieurs dimensions",
                "pairs": [
                    ("Coordination", "organiser et faire avancer le programme"),
                    ("Communication", "transmettre les informations aux participants et partenaires"),
                    ("Formation", "contribuer au développement des compétences"),
                    ("Jeunesse", "accompagner et mobiliser les jeunes"),
                    ("Insertion", "contribuer à leur autonomisation"),
                    ("Projet", "transformer les objectifs en actions concrètes"),
                ],
                "images": ["paisj-1.jpg", "paisj-2.jpg", "paisj-3.jpg"],
            },
            {
                "title": "FilGOOD & Déco by AT",
                "role": "Entrepreneuse & porteuse de projet",
                "text": [
                    "L'entrepreneuriat constitue une autre forme de coordination : partir d'une idée, construire "
                    "une identité, développer une offre et organiser sa mise en œuvre.",
                    "Avec FilGOOD & Déco by AT, je développe une initiative autour du crochet artisanal et de la décoration.",
                ],
                "steps": ["Création", "Développement", "Communication", "Marketing", "Relation client", "Vente"],
                "after": "Cette expérience m'a appris à porter un projet avec une vision à la fois créative et opérationnelle.",
                "award": {
                    "title": "Hasina Bootcamp, Zafy Tody × Nexta",
                    "result": "Deuxième lauréate, 2026",
                    "text": "Participation à un bootcamp consacré à l'entrepreneuriat dans les industries culturelles et créatives.",
                    "image": "hasina-bootcamp.jpg",
                    "link": {"label": "Voir la vidéo", "url": "https://www.facebook.com/reel/2211431609610766/?app=fbl"},
                },
            },
            {
                "title": "Madagascar MUN 2026",
                "role": "Vice-présidente de l'Assemblée générale",
                "list": [
                    "Présidence de séances de simulation de l'Assemblée générale des Nations Unies",
                    "Gestion logistique et technique des procédures",
                    "Coordination entre l'organisation hôte et les participants",
                ],
                "images": ["mun-vp-1.jpg", "mun-vp-2.jpg", "mun-vp-3.jpg"],
            },
            {
                "title": "I-AKO",
                "role": "Modération & événementiel",
                "text": ["Participation à la préparation et à la modération de la conférence I-AKO, interview "
                         "culturelle de l'IEP Madagascar."],
                "tags_title": "Cette expérience m'a permis de mobiliser",
                "tags": ["Préparation", "Prise de parole", "Gestion des échanges", "Communication événementielle"],
                "images": ["iako-1.jpg", "iako-2.jpg"],
            },
        ],
    },
    {
        "id": "engagement",
        "label": "Engagement social & associatif",
        "headline": "Transmettre pour contribuer",
        "intro": "Au-delà de la communication événementielle, mon engagement me sert surtout à aider les jeunes comme moi.",
        "projects": [
            {
                "title": "Enseignement du français",
                "role": "Transmettre & accompagner",
                "text": ["Mes stages d'enseignement au Lycée Moderne Ampefiloha et au Lycée Technique Ampefiloha "
                         "m'ont permis d'expérimenter directement la transmission des connaissances."],
                "list": [
                    "Enseignement du français en classes de quatrième, troisième, seconde et terminale",
                    "Préparation de fiches pédagogiques",
                    "Préparation et animation des cours",
                    "Adaptation des contenus aux apprenants",
                ],
                "images": ["enseignement-1.jpg", "enseignement-2.jpg"],
            },
            {
                "title": "Programme PAISJ",
                "role": "Figure représentative du programme · Développement des compétences & autonomisation des jeunes",
                "list": [
                    "Structuration des contenus de formation",
                    "Contribution au développement de compétences utiles à l'insertion et à l'autonomie des jeunes",
                ],
                "tags_title": "Les trois axes du programme",
                "tags": [
                    "Compétences transversales",
                    "Compétences numériques essentielles",
                    "Employabilité et insertion professionnelle",
                ],
                "images": ["paisj-formation-1.jpg", "paisj-formation-2.jpg"],
            },
        ],
    },
]

CONTACT = {
    "headline": "Construisons la suite.",
    "text": "Mon parcours continue de se construire autour de projets qui réunissent communication, "
            "coordination, transmission et entrepreneuriat. Si vous souhaitez échanger autour d'un projet, "
            "d'une collaboration ou d'une opportunité professionnelle, parlons-en.",
    "email": "randriatoandri@gmail.com",
    "phone": "032 66 056 11",
    "phone_link": "+261326605611",
    # Remplacer par l'URL réelle du profil LinkedIn
    "linkedin": {"label": "Tsifoina RANDRIANARIVONANTOANINA", "url": ""},
}
