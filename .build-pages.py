#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les 6 pages « type d'application » de webprime.fr.
Nav, tiroir, bottom-nav et footer sont repris tels quels depuis index.html
pour qu'une seule source fasse foi."""
import json
import re

IDX = open('index.html', encoding='utf-8').read()


def cut(src, start, end):
    i = src.index(start)
    j = src.index(end, i + len(start))
    return src[i:j + len(end)]


HEADER = cut(IDX, '    <header class="ent-header">', '    </header>')
DRAWER = cut(IDX, '    <div class="ent-drawer" id="entDrawer">',
             '    <div class="ent-drawer-backdrop" id="entDrawerBackdrop"></div>')
BOTNAV = cut(IDX, '    <nav class="ent-bottom-nav">', '    </nav>')
FOOTER = cut(IDX, '    <footer class="footer">', '    </footer>')
SCRIPT = cut(IDX, '    <script>\n        var entDrawer', '    </script>')

TECH_INTRO = (
    "On ne vend pas une technologie, on résout un problème. WebPrime travaille avec "
    "<strong>tous les langages, tous les frameworks et toutes les bases de données</strong> du marché — "
    "et à chaque projet, on choisit ceux qui vous servent le mieux. "
    "Pas ceux qu'on a l'habitude d'utiliser : ceux qui rendent <em>votre</em> application "
    "la plus rapide, la moins chère à faire tourner et la plus simple à faire évoluer."
)

APPS = [
    dict(
        slug='application-vitrine', num=1, emo='📱', nom='App Vitrine',
        total='987€', acompte='297€', mens='58€', gestion='59€', cle='app-vitrine',
        titre="Création d'application vitrine iOS et Android",
        desc="Application mobile vitrine pour présenter votre activité : catalogue, horaires, appel et itinéraire en un geste, notifications push. 987€ — 297€ à la signature puis 58€/mois.",
        eyebrow="Application vitrine",
        h2="Votre entreprise<br><span>dans la poche de vos clients.</span>",
        intro="L'application la plus simple de notre gamme, et souvent la plus rentable. Elle présente votre activité, vos produits et vos horaires, et met un appel ou un itinéraire à un seul geste. Pas de compte à créer, pas de paiement : l'essentiel, bien fait.",
        pour="Commerces de proximité, artisans, restaurants, cabinets, associations — tous ceux dont les clients ont juste besoin de les joindre vite et bien.",
        features=[
            ("Présentation et catalogue", "Vos services ou vos produits en photos, avec descriptions et tarifs, organisés en catégories."),
            ("Appel, message, itinéraire", "Trois boutons qui lancent directement le téléphone, le SMS ou le GPS de votre client."),
            ("Horaires et actualités", "Vos horaires d'ouverture, vos fermetures exceptionnelles et vos nouveautés, modifiables quand vous voulez."),
            ("Notifications push", "Une promotion, une info, un événement : tous vos clients le reçoivent sur leur écran d'accueil."),
            ("Publication sur les stores", "On s'occupe des fiches App Store et Google Play, des captures et de la validation."),
        ],
        mock=[("📱 App Vitrine", "iOS · Android"), ("Catalogue et photos", "✓ Inclus"),
              ("Appel et itinéraire", "✓ Inclus"), ("Notifications push", "✓ Inclus"),
              ("Compte utilisateur", "— Non"), ("App Store + Google Play", "Publication gérée")],
        tech_angle="Sur une application vitrine, la bonne technologie est celle qui va vite à construire et qui ne coûte presque rien à faire tourner. Inutile de sortir l'artillerie lourde pour afficher un catalogue.",
        tech=[
            ("L'application", "Le plus souvent un seul code pour les deux téléphones : c'est deux fois moins cher qu'écrire une application iPhone et une application Android séparées. On passe au développement natif uniquement si votre projet l'exige.",
             ["Flutter", "React Native", "Swift (iOS)", "Kotlin (Android)"]),
            ("Le serveur", "Pour une vitrine, il n'y a parfois aucun serveur à payer : le contenu voyage avec l'application. Si vous voulez modifier vos textes sans republier, on ajoute un petit back-office très léger.",
             ["Node.js", "PHP", "Sans serveur"]),
            ("Les données", "Pas besoin d'une grosse base pour une dizaine de pages. On prend le plus simple qui tienne la route, quitte à grossir plus tard si votre application évolue.",
             ["Firebase", "SQLite", "Fichiers JSON"]),
        ],
        faq=[
            ("Une application vitrine, est-ce vraiment utile face à un site web ?",
             "Les deux ne font pas le même travail. Un site, on le visite quand on le cherche. Une application, elle reste sur l'écran d'accueil et vous permet d'envoyer une notification — c'est ce qui fait revenir le client."),
            ("Combien de temps avant qu'elle soit sur les stores ?",
             "Comptez en général quatre à six semaines : deux semaines de maquettes et de développement, puis le délai de validation d'Apple et de Google, qui ne dépend pas de nous."),
            ("Pourrai-je changer mes photos et mes horaires moi-même ?",
             "Oui. Vous avez un back-office simple, accessible depuis un navigateur, pour modifier vos textes, vos photos et vos horaires. Et si vous préférez nous l'envoyer par message, les modifications de contenu sont comprises dans la gestion mensuelle."),
        ],
    ),
    dict(
        slug='application-contenu', num=2, emo='🎬', nom='App Contenu & média',
        total='1 987€', acompte='597€', mens='116€', gestion='79€', cle='app-contenu',
        titre="Création d'application de contenu et média (articles, vidéos, podcasts)",
        desc="Application mobile de contenu iOS et Android : articles, vidéos, podcasts, espace abonné, favoris et notifications ciblées. 1 987€ — 597€ à la signature puis 116€/mois.",
        eyebrow="Application contenu & média",
        h2="Vos contenus,<br><span>lus, vus et écoutés.</span>",
        intro="Une application faite pour publier : des articles, des vidéos, des podcasts ou des fiches, que vos abonnés consultent, mettent en favori et retrouvent là où ils s'étaient arrêtés. Vous publiez depuis un back-office, ils reçoivent une notification.",
        pour="Médias, clubs et fédérations, écoles et organismes de formation, coachs qui diffusent des programmes, marques qui publient régulièrement.",
        features=[
            ("Articles, vidéos, podcasts", "Un même fil pour tous vos formats, rangés en catégories et en playlists."),
            ("Comptes et espace abonné", "Inscription, connexion, profil — et la possibilité de réserver certains contenus aux abonnés."),
            ("Favoris et reprise de lecture", "Vos membres mettent de côté et reprennent une vidéo exactement là où ils l'avaient laissée."),
            ("Notifications par catégorie", "Chacun choisit ce qu'il veut suivre : vous ne spammez personne et vos taux d'ouverture montent."),
            ("Back-office de publication", "Vous écrivez, vous programmez, vous publiez — sans nous appeler."),
        ],
        mock=[("🎬 App Contenu", "iOS · Android"), ("Articles et vidéos", "✓ Inclus"),
              ("Espace abonné", "✓ Inclus"), ("Favoris et reprise", "✓ Inclus"),
              ("Notifications ciblées", "✓ Inclus"), ("Back-office de publication", "✓ Inclus")],
        tech_angle="Ici tout se joue sur le confort de lecture : une vidéo qui démarre vite, un article lisible hors connexion, une appli qui ne vide pas la batterie. C'est ça qui dicte les choix techniques, pas la mode du moment.",
        tech=[
            ("L'application", "Un code partagé iOS et Android suffit presque toujours. On bascule en natif quand la lecture hors connexion ou la gestion fine de l'audio en arrière-plan deviennent le cœur du produit.",
             ["Flutter", "React Native", "Swift (iOS)", "Kotlin (Android)"]),
            ("Le serveur", "Il gère vos comptes, vos publications et la distribution des médias. Le langage se choisit selon le volume que vous visez et selon ce que votre équipe sait déjà maintenir.",
             ["Node.js", "Python / Django", "PHP / Symfony", "Laravel"]),
            ("Les données et les médias", "Une base classique pour le catalogue, un cache pour que le fil s'affiche instantanément, et un stockage dédié aux vidéos avec un réseau de diffusion mondial.",
             ["PostgreSQL", "MySQL", "Redis", "Stockage S3 + CDN"]),
        ],
        faq=[
            ("Mes vidéos seront-elles hébergées dans l'application ?",
             "Elles sont stockées sur un service dédié et diffusées par un réseau mondial, pour qu'une vidéo démarre aussi vite à Lille qu'à Marseille. On peut aussi brancher l'application sur votre compte Vimeo ou YouTube si vous en avez déjà un."),
            ("Puis-je faire payer l'accès à certains contenus ?",
             "Oui, par abonnement ou à l'unité. Attention : Apple et Google prélèvent une commission sur les abonnements vendus dans l'application. On en parle avant de choisir le mode de paiement, ça change votre marge."),
            ("Combien de contenus l'application peut-elle encaisser ?",
             "Il n'y a pas de limite pratique. La base et le cache sont dimensionnés dès le départ pour encaisser plusieurs milliers de publications sans que le fil ralentisse."),
        ],
    ),
    dict(
        slug='application-reservation', num=3, emo='📅', nom='App Rendez-vous',
        total='2 987€', acompte='897€', mens='175€', gestion='99€', cle='app-booking',
        titre="Création d'application de réservation et de prise de rendez-vous",
        desc="Application mobile de réservation iOS et Android : agenda temps réel, créneaux, acompte en ligne, rappels automatiques et back-office planning. 2 987€ — 897€ à la signature puis 175€/mois.",
        eyebrow="Application de réservation",
        h2="Votre agenda,<br><span>ouvert 24 heures sur 24.</span>",
        intro="Vos clients réservent quand ils y pensent, à 23h un dimanche, sans vous déranger. L'agenda se met à jour en direct, l'acompte est encaissé, et le rappel automatique fait fondre les rendez-vous non honorés.",
        pour="Salons de coiffure et instituts, coachs et praticiens, restaurants, cabinets, loueurs de matériel, ateliers et garages.",
        features=[
            ("Agenda et créneaux en temps réel", "Vos disponibilités réelles, mises à jour à la seconde : deux clients ne peuvent pas prendre le même créneau."),
            ("Acompte ou paiement à la réservation", "Vous sécurisez votre planning en demandant un acompte, ou le règlement complet à la réservation."),
            ("Rappels automatiques", "Une notification la veille et une heure avant : c'est le levier le plus efficace contre les rendez-vous manqués."),
            ("Gestion des annulations", "Vos règles d'annulation sont appliquées toutes seules, délais et remboursement compris."),
            ("Back-office planning", "Vous voyez la journée, la semaine, vos équipes, et vous bloquez un créneau en deux gestes."),
        ],
        mock=[("📅 App Rendez-vous", "iOS · Android"), ("Agenda temps réel", "✓ Inclus"),
              ("Acompte en ligne", "✓ Inclus"), ("Rappels automatiques", "✓ Inclus"),
              ("Synchro Google Agenda", "✓ En option"), ("Back-office planning", "✓ Inclus")],
        tech_angle="Une application de réservation a un seul vrai ennemi : la double réservation. Deux clients qui cliquent sur le même créneau à la même seconde. C'est ce risque qui commande les choix techniques, pas le reste.",
        tech=[
            ("L'application", "Un code partagé entre iPhone et Android couvre parfaitement le besoin. L'essentiel se joue côté serveur, pas sur le téléphone.",
             ["Flutter", "React Native", "Swift (iOS)", "Kotlin (Android)"]),
            ("Le serveur", "C'est lui qui arbitre les créneaux et qui encaisse. On choisit un socle solide, avec une vraie gestion des accès simultanés et une bibliothèque de paiement éprouvée.",
             ["Node.js", "PHP / Symfony", "Python / Django", "Stripe"]),
            ("Les données", "Ici on écarte volontairement les bases « souples » à la mode : seule une base relationnelle garantit qu'un créneau réservé ne peut pas l'être deux fois. C'est un choix de fiabilité, pas de goût.",
             ["PostgreSQL", "MySQL", "Redis"]),
        ],
        faq=[
            ("Deux clients peuvent-ils réserver le même créneau ?",
             "Non. Le serveur verrouille le créneau le temps de la réservation : le deuxième client voit l'horaire disparaître en direct. C'est précisément pour cette garantie qu'on choisit une base de données relationnelle plutôt qu'une base plus souple."),
            ("L'agenda peut-il se synchroniser avec le mien ?",
             "Oui, avec Google Agenda, Outlook ou Apple Calendrier : une réservation dans l'application apparaît dans votre agenda, et un rendez-vous bloqué dans votre agenda ferme le créneau dans l'application."),
            ("Et si j'ai plusieurs salariés ou plusieurs lieux ?",
             "C'est prévu : chaque personne et chaque lieu a son propre planning, avec ses horaires et ses prestations. Le client choisit avec qui et où il réserve."),
        ],
    ),
    dict(
        slug='application-ecommerce', num=4, emo='🛒', nom='App E-commerce',
        total='4 987€', acompte='1 497€', mens='291€', gestion='149€', cle='app-ecommerce',
        titre="Création d'application e-commerce iOS et Android",
        desc="Application mobile e-commerce iOS et Android : catalogue, panier, paiement sécurisé, suivi de commande, comptes clients et fidélité. 4 987€ — 1 497€ à la signature puis 291€/mois.",
        eyebrow="Application e-commerce",
        h2="Votre boutique,<br><span>sur l'écran d'accueil.</span>",
        intro="Le même produit se vend mieux dans une application que sur un site : le client est déjà connecté, son moyen de paiement est enregistré, et une notification suffit à relancer un panier abandonné. C'est là que se joue le réachat.",
        pour="Boutiques qui vendent déjà en ligne, marques en direct, épiceries et traiteurs, abonnements et box, grossistes qui veulent une appli de commande pour leurs pros.",
        features=[
            ("Catalogue et variantes", "Tailles, couleurs, déclinaisons, stock par variante : votre catalogue réel, pas une version simplifiée."),
            ("Panier et paiement sécurisé", "Carte bancaire, Apple Pay et Google Pay : le paiement se fait en deux gestes, sans ressaisir un numéro."),
            ("Suivi de commande", "Le client suit sa commande de la préparation à la livraison, et reçoit une notification à chaque étape."),
            ("Comptes clients et fidélité", "Historique, adresses enregistrées, points de fidélité et offres réservées aux porteurs de l'application."),
            ("Back-office commandes et stock", "Vous gérez vos produits, vos prix, vos stocks et vos commandes depuis un seul écran."),
        ],
        mock=[("🛒 App E-commerce", "iOS · Android"), ("Catalogue et variantes", "✓ Inclus"),
              ("Apple Pay / Google Pay", "✓ Inclus"), ("Suivi de commande", "✓ Inclus"),
              ("Fidélité", "✓ Inclus"), ("Back-office stock", "✓ Inclus")],
        tech_angle="Dès qu'on encaisse de l'argent, les règles changent : il faut du paiement conforme, une recherche qui trouve vraiment, et un stock qui ne se décale jamais. On choisit donc des briques éprouvées, pas des paris.",
        tech=[
            ("L'application", "Un code partagé pour les deux téléphones, avec les modules de paiement officiels d'Apple et de Google intégrés en natif — c'est ce qui permet le paiement en deux gestes.",
             ["Flutter", "React Native", "Apple Pay", "Google Pay"]),
            ("Le serveur", "Si vous avez déjà une boutique en ligne, on branche l'application dessus plutôt que de tout refaire : votre stock reste à un seul endroit. Sinon, on construit le serveur de commandes.",
             ["Node.js", "Symfony", "Laravel", "Java / Spring", "Shopify", "WooCommerce"]),
            ("Les données", "Une base relationnelle pour les commandes et le stock, un cache pour les paniers, et un moteur de recherche dédié dès que le catalogue dépasse quelques centaines de produits.",
             ["PostgreSQL", "MySQL", "Redis", "Elasticsearch"]),
        ],
        faq=[
            ("J'ai déjà une boutique Shopify ou WooCommerce, faut-il tout refaire ?",
             "Non, et c'est même déconseillé. On branche l'application sur votre boutique existante : vos produits, vos stocks et vos commandes restent au même endroit, et vous continuez à travailler avec les outils que vous connaissez."),
            ("Apple et Google prennent-ils une commission sur mes ventes ?",
             "Pour des produits physiques livrés, non : vous encaissez par carte bancaire comme sur votre site, et les stores ne prennent rien. La commission de 15 à 30% ne s'applique qu'aux contenus et abonnements numériques consommés dans l'application."),
            ("Le stock peut-il se décaler entre l'application et la boutique ?",
             "Non, parce qu'il n'y a qu'un seul stock. L'application ne tient pas son propre compteur : elle interroge votre boutique en direct et se met à jour à chaque commande."),
        ],
    ),
    dict(
        slug='application-marketplace', num=5, emo='🏷️', nom='App Marketplace',
        total='7 987€', acompte='2 397€', mens='466€', gestion='199€', cle='app-marketplace',
        titre="Création d'application marketplace et de petites annonces",
        desc="Application mobile marketplace iOS et Android : dépôt d'annonce, recherche géolocalisée, messagerie interne, modération et commissions. 7 987€ — 2 397€ à la signature puis 466€/mois.",
        eyebrow="Application marketplace",
        h2="Vos membres publient,<br><span>vous prenez la commission.</span>",
        intro="Le principe des petites annonces entre particuliers : ce sont vos utilisateurs qui remplissent l'application. Vous fournissez la place de marché, la confiance et les outils — et vous vous rémunérez sur les options payantes ou sur la commission.",
        pour="Places de marché locales ou thématiques, réseaux professionnels, plateformes de location entre particuliers, bourses d'échange de clubs et de fédérations.",
        features=[
            ("Dépôt d'annonce avec photos", "Formulaire guidé, plusieurs photos, catégories et champs adaptés à votre univers."),
            ("Recherche filtrée et géolocalisée", "« Dans un rayon de 20 km, entre 50 et 200€, en bon état » — et le résultat tombe tout de suite."),
            ("Messagerie interne", "Acheteurs et vendeurs discutent dans l'application : personne ne donne son numéro, vous gardez la relation."),
            ("Modération et signalements", "File de modération, signalement en un geste, blocage d'un membre : vous tenez votre place de marché propre."),
            ("Commissions et options payantes", "Remontée d'annonce, mise en avant, abonnement vendeur pro, commission sur transaction."),
        ],
        mock=[("🏷️ App Marketplace", "iOS · Android"), ("Dépôt d'annonce", "✓ Inclus"),
              ("Recherche géolocalisée", "✓ Inclus"), ("Messagerie interne", "✓ Inclus"),
              ("Modération", "✓ Inclus"), ("Commissions", "✓ Inclus")],
        tech_angle="Une marketplace vit ou meurt sur sa recherche. Si un membre ne trouve pas en trois secondes ce qu'il cherche près de chez lui, il s'en va. Tout le choix technique part de là — et de la capacité à encaisser la croissance.",
        tech=[
            ("L'application", "Un code partagé iOS et Android, avec une attention particulière au formulaire de dépôt et à l'envoi des photos, qui doivent marcher même en 4G capricieuse.",
             ["Flutter", "React Native", "Swift (iOS)", "Kotlin (Android)"]),
            ("Le serveur", "Le langage se choisit sur la charge attendue. Pour quelques milliers d'annonces, un socle classique suffit largement. Au-delà, on découpe en services et on passe à un langage taillé pour le volume.",
             ["Node.js", "Go", "Java", "Python", "Stripe Connect"]),
            ("Les données et la recherche", "Une base relationnelle avec extension géographique pour le « près de chez moi », un moteur de recherche dédié pour les filtres, un cache pour les listes, et un stockage séparé pour les photos.",
             ["PostgreSQL + PostGIS", "Elasticsearch", "MeiliSearch", "Redis", "Stockage S3"]),
        ],
        faq=[
            ("Comment l'argent circule-t-il entre acheteur et vendeur ?",
             "Par un service de paiement fractionné : l'acheteur paie, la somme est conservée, votre commission est prélevée automatiquement et le reste est reversé au vendeur. Vous ne manipulez jamais l'argent des autres, ce qui vous évite de lourdes obligations réglementaires."),
            ("Que se passe-t-il si quelqu'un publie une annonce interdite ?",
             "Un filtrage automatique bloque les cas évidents à la publication, les membres peuvent signaler en un geste, et vous avez une file de modération pour trancher et bloquer un compte. C'est aussi une obligation légale pour une plateforme : on la câble dès le départ."),
            ("Mon application tiendra-t-elle si ça décolle ?",
             "C'est prévu dès la conception : recherche et stockage des photos sont séparés du reste, donc on peut renforcer une brique sans tout réécrire. C'est pour ça qu'on ne choisit pas la même technologie pour une marketplace que pour une application vitrine."),
        ],
    ),
    dict(
        slug='application-temps-reel', num=6, emo='📍', nom='App Temps réel',
        total='12 987€', acompte='3 897€', mens='758€', gestion='299€', cle='app-temps-reel',
        titre="Création d'application temps réel : transport, livraison, dépannage",
        desc="Deux applications mobiles iOS et Android, client et professionnel : suivi GPS en direct, calcul d'itinéraire et de prix, attribution de mission, paiement intégré. 12 987€ — 3 897€ à la signature puis 758€/mois.",
        eyebrow="Application temps réel",
        h2="Deux applications,<br><span>une carte qui bouge en direct.</span>",
        intro="C'est le projet le plus technique de la gamme, et le seul qui demande <strong>deux applications</strong> : une pour votre client qui commande et suit, une pour votre professionnel sur le terrain qui accepte et exécute. Entre les deux, une carte qui bouge à la seconde.",
        pour="Transport de personnes, livraison et coursiers, dépannage et interventions à domicile, flottes de techniciens, services de nettoyage à la demande.",
        features=[
            ("Deux applications distinctes", "L'application client pour commander et suivre, l'application professionnel pour recevoir et exécuter la mission."),
            ("Suivi GPS en direct", "La position du professionnel avance sur la carte du client, en continu, sans rafraîchir."),
            ("Calcul d'itinéraire et de prix", "Distance, durée, tarification par zone ou par kilomètre, majoration aux heures de pointe."),
            ("Attribution de mission", "La course part au professionnel le plus proche et disponible, avec un délai d'acceptation et un report automatique."),
            ("Back-office de supervision", "Toutes vos missions et tous vos professionnels sur une carte, en direct, avec reprise en main manuelle."),
        ],
        mock=[("📍 App Temps réel", "2 apps · iOS · Android"), ("Suivi GPS en direct", "✓ Inclus"),
              ("Itinéraire et prix", "✓ Inclus"), ("Attribution de mission", "✓ Inclus"),
              ("Paiement à la course", "✓ Inclus"), ("Supervision sur carte", "✓ Inclus")],
        tech_angle="Le temps réel ne pardonne rien : une position qui arrive avec dix secondes de retard, et le client croit que son chauffeur est perdu. Ici, chaque brique est choisie pour la latence et pour la batterie — rien d'autre ne compte.",
        tech=[
            ("Les deux applications", "Un code partagé reste possible, mais c'est le seul cas où l'on recommande parfois le natif : le GPS en arrière-plan et la consommation de batterie sur l'application professionnel sont trop sensibles pour être laissés au hasard.",
             ["Flutter", "React Native", "Swift (iOS)", "Kotlin (Android)"]),
            ("Le serveur", "Il faut une technologie taillée pour maintenir des milliers de connexions ouvertes en permanence, et une file d'attente pour distribuer les missions sans en perdre une seule.",
             ["Node.js", "Go", "WebSocket", "Redis", "RabbitMQ", "Kafka"]),
            ("Les données et la carte", "Base relationnelle avec extension géographique pour « qui est le plus proche », cache mémoire pour les positions qui changent chaque seconde, et base dédiée à l'historique des trajets.",
             ["PostgreSQL + PostGIS", "Redis", "TimescaleDB", "Google Maps", "Mapbox"]),
        ],
        faq=[
            ("Pourquoi deux applications et pas une seule ?",
             "Parce que les deux métiers n'ont rien à voir. Votre client veut commander en trois gestes et suivre une carte. Votre professionnel veut accepter une mission d'une main, en conduisant ou en portant un carton. Deux usages, deux applications, deux fiches sur les stores — c'est ce qui double le travail et explique le prix."),
            ("Le GPS va-t-il vider la batterie des professionnels ?",
             "C'est le premier sujet qu'on traite. La position n'est pas envoyée en continu mais à une cadence adaptée à la vitesse et au contexte, et le suivi s'arrête dès que la mission est terminée. Sans ce travail, une application de ce type vide un téléphone en trois heures."),
            ("Quelle carte utilisez-vous, et combien ça coûte ?",
             "Google Maps, Mapbox ou une solution libre selon votre volume : au-delà d'un certain nombre de calculs d'itinéraire par mois, ces services deviennent payants et la facture peut grimper. On compare les coûts réels sur votre volume prévu avant de choisir, et c'est inclus dans la gestion mensuelle."),
        ],
    ),
]

TECH_FAQ = [
    ("Avec quel langage mon application sera-t-elle développée ?",
     "Celui qui convient le mieux à votre projet. Nous travaillons avec tous les langages, tous les frameworks et toutes les bases de données du marché : Swift et Kotlin pour le natif, Flutter et React Native pour couvrir iPhone et Android avec un seul code, Node.js, PHP, Python, Java ou Go côté serveur, PostgreSQL, MySQL, MongoDB ou Firebase pour les données. On ne choisit jamais par habitude : on choisit ce qui rend votre application la plus rapide, la moins chère à faire tourner et la plus facile à faire évoluer."),
    ("Pourquoi ne pas m'annoncer la technologie tout de suite ?",
     "Parce que ce serait mettre la réponse avant la question. Le bon choix dépend de ce que votre application doit faire, du nombre d'utilisateurs attendu, de votre budget de fonctionnement et de ce que vous voudrez ajouter dans deux ans. On vous annonce la technologie retenue, et les raisons du choix en français, au moment du cadrage — avant que vous signiez quoi que ce soit."),
    ("Serai-je enfermé chez WebPrime ?",
     "Non. À la dernière des 12 mensualités, l'application est votre propriété : code source, fiche App Store et fiche Google Play vous sont transférés. Et comme on ne travaille qu'avec des technologies répandues et documentées, n'importe quel développeur sérieux peut reprendre le travail après nous. C'est aussi pour ça qu'on évite les solutions exotiques."),
]


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build(a):
    url = f"https://webprime.fr/{a['slug']}.html"
    faq = a['faq'] + TECH_FAQ

    ld_service = {
        "@context": "https://schema.org", "@type": "Service",
        "name": f"Création d'{a['nom'].lower().replace('app ', 'application ')} iOS et Android",
        "serviceType": a['eyebrow'], "url": url,
        "description": a['desc'],
        "provider": {"@type": "ProfessionalService", "name": "WebPrime",
                     "url": "https://webprime.fr", "email": "partenaire@webprime.fr"},
        "areaServed": {"@type": "Country", "name": "France"},
        "offers": {"@type": "Offer", "price": a['total'].replace('€', '').replace(' ', ''),
                   "priceCurrency": "EUR", "url": url,
                   "description": f"{a['acompte']} à la signature, puis {a['mens']} par mois sur 12 mois. Gestion mensuelle {a['gestion']} ensuite."},
    }
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in faq]}
    ld_bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://webprime.fr/"},
        {"@type": "ListItem", "position": 2, "name": "Nos applications", "item": "https://webprime.fr/#types"},
        {"@type": "ListItem", "position": 3, "name": a['nom'], "item": url}]}

    feats = "\n".join(
        f'                        <li><span class="fi">◆</span><div><b>{b}</b><span>{d}</span></div></li>'
        for b, d in a['features'])
    mock = "\n".join(
        f'                    <div class="ent-mock-row"><span class="k">{k}</span><span class="{"up" if v.startswith("✓") else "v"}">{v}</span></div>'
        for k, v in a['mock'])
    techs = "\n".join(
        f'''                <div class="ent-tech-card reveal">
                    <h3>{t}</h3>
                    <p>{d}</p>
                    <div class="ent-tech-tags">{"".join(f"<span>{x}</span>" for x in tags)}</div>
                </div>''' for t, d, tags in a['tech'])
    details = "\n".join(
        f'                <details class="reveal"><summary>{q}</summary><p>{r}</p></details>' for q, r in faq)

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{a['titre']} | WebPrime</title>
    <meta name="description" content="{a['desc']}">
    <link rel="canonical" href="{url}"/>
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{a['titre']} | WebPrime">
    <meta property="og:description" content="{a['desc']}">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" type="image/png" sizes="192x192" href="./logo/icon-192x192.png">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script type="application/ld+json">
{json.dumps(ld_service, ensure_ascii=False, indent=8)}
    </script>
    <script type="application/ld+json">
{json.dumps(ld_faq, ensure_ascii=False, indent=8)}
    </script>
    <script type="application/ld+json">
{json.dumps(ld_bc, ensure_ascii=False, indent=8)}
    </script>
</head>
<body>

{HEADER}

{DRAWER}

{BOTNAV}

    <section class="ent-hero">
        <div class="container">
            <p class="ent-breadcrumb"><a title="creation application mobile" href="https://webprime.fr/">Accueil</a> › <a title="types d'applications mobiles" href="https://webprime.fr/#types">Nos applications</a> › {a['nom']}</p>
            <h1 class="ent-eyebrow">{a['emo']} {a['titre']}</h1>
            <h2 class="ent-hero-title">{a['h2']}</h2>
            <p>{a['intro']}</p>
            <div class="ent-cta-row">
                <a title="devis {a['slug'].replace('-', ' ')}" href="https://webprime.fr/contact.html?projet={a['cle']}" class="btn btn-primary">Lancer mon app</a>
                <a title="prix {a['slug'].replace('-', ' ')}" href="#tarif" class="btn btn-ghost">Voir le tarif</a>
            </div>
            <div class="ent-trust">
                <span><b>iOS + Android</b> en un seul projet</span>
                <span><b>{a['acompte']}</b> à la signature</span>
                <span><b>{a['total']}</b> au total</span>
            </div>
        </div>
    </section>

    <section class="ent-section ent-white" id="detail">
        <div class="container">
            <div class="ent-split">
                <div>
                    <span class="ent-eyebrow reveal">{a['eyebrow']}</span>
                    <h2 class="reveal">Ce que votre <span>application fait</span></h2>
                    <p class="ent-lead reveal">{a['pour']}</p>
                    <ul class="ent-feature-list reveal">
{feats}
                    </ul>
                </div>
                <div class="ent-mock reveal">
                    <div class="ent-mock-bar"><i style="background:#ff5f56"></i><i style="background:#ffbd2e"></i><i style="background:#27c93f"></i></div>
{mock}
                </div>
            </div>
        </div>
    </section>

    <section class="ent-section" id="technologies">
        <div class="container ent-center">
            <span class="ent-eyebrow reveal">Les technologies</span>
            <h2 class="reveal">On choisit la technologie <span>pour votre projet</span></h2>
            <p class="ent-lead reveal">{TECH_INTRO}</p>
            <p class="ent-lead reveal">{a['tech_angle']}</p>
            <div class="ent-tech-grid">
{techs}
            </div>
            <p class="ent-note">Vous n'avez rien à décider : on vous annonce la technologie retenue et la raison du choix, en français, au moment du cadrage — avant la signature.</p>
        </div>
    </section>

    <section class="ent-section ent-white" id="tarif">
        <div class="container ent-center">
            <span class="ent-eyebrow reveal">Tarif</span>
            <h2 class="reveal">{a['nom']}, <span>{a['total']}</span></h2>
            <p class="ent-lead reveal">30% à la signature, le solde en 12 mensualités. À la dernière échéance, l'application est à vous.</p>
            <div class="ent-grid cols-3">
                <div></div>
                <div class="ent-card ent-offer featured reveal" id="offre">
                    <span class="tag">{a['eyebrow']}</span>
                    <h3>{a['num']} · {a['nom']}</h3>
                    <div class="ent-price"><b>{a['acompte']}</b> <span>à la signature, puis {a['mens']}/mois sur 12 mois</span></div>
                    <ul>
                        <li><b>{a['total']} au total</b></li>
                        <li>iPhone et Android</li>
                        <li>Design sur mesure à votre marque</li>
                        <li>Publication App Store + Google Play</li>
                        <li>Propriétaire à la 12<sup>e</sup> mensualité</li>
                        <li>Puis gestion <b>{a['gestion']}/mois</b></li>
                    </ul>
                    <a title="devis {a['slug'].replace('-', ' ')}" href="https://webprime.fr/contact.html?projet={a['cle']}" class="btn btn-primary">Lancer mon app</a>
                </div>
                <div></div>
            </div>
            <p class="ent-note">La gestion mensuelle comprend l'hébergement, le nom de domaine, la sécurité, les mises à jour iOS et Android, le maintien des fiches sur les stores et les modifications de contenu illimitées.<br><span style="color:var(--text-body);font-size:13px;"><a title="types d'applications mobiles" href="https://webprime.fr/#types">Comparer les 6 types d'applications →</a></span></p>
        </div>
    </section>

    <section class="ent-section" id="faq">
        <div class="container ent-center">
            <span class="ent-eyebrow reveal">Questions fréquentes</span>
            <h2 class="reveal">{a['nom']} : <span>ce qu'on nous demande</span></h2>
            <div class="ent-faq">
{details}
            </div>
        </div>
    </section>

    <section class="ent-cta">
        <div class="container">
            <h2 class="reveal">Un projet d'{a['eyebrow'].lower()} ?</h2>
            <p class="reveal">Parlez-nous de votre idée : on vous répond rapidement, et on vous dit franchement si une formule plus simple suffirait.</p>
            <div class="ent-cta-row reveal">
                <a title="devis {a['slug'].replace('-', ' ')}" href="https://webprime.fr/contact.html?projet={a['cle']}" class="btn btn-primary">Lancer mon projet</a>
                <a title="prix application mobile" href="https://webprime.fr/#offres" class="btn btn-ghost">Voir les 6 tarifs</a>
            </div>
            <div class="ent-guar reveal">
                <span>iPhone + Android</span>
                <span>Publication sur les stores</span>
                <span>Propriétaire au bout d'un an</span>
                <span>Interlocuteur unique</span>
                <span>Prix affichés</span>
            </div>
        </div>
    </section>

{FOOTER}

{SCRIPT}
    <script src="ui.js"></script>
</body>
</html>
'''


for a in APPS:
    path = f"{a['slug']}.html"
    open(path, 'w', encoding='utf-8').write(build(a))
    print(f"écrit  {path}")
