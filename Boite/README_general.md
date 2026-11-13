# Boîte étanche MOLONARI

Ce dossier regroupe tout ce qui concerne la **boîte du capteur MOLONARI** : sa conception, sa fabrication et son installation sur le terrain.

La boîte est imprimée en 3D. Elle protège l'électronique du capteur lorsqu'il est immergé dans la rivière, laisse passer les sondes de température et met le transducteur de pression au contact de l'eau.

📷 *[À COMPLÉTER : photo de la boîte assemblée]*

---

## Comment ce dossier est organisé

Le dossier est découpé selon **les deux moments de la vie de la boîte** : on la fabrique d'abord, puis on la déploie sur le terrain. Chaque sous-dossier est autonome et a son propre README.

```
boite/
├── README.md          ← vous êtes ici : présentation générale
├── fabrication/       ← comment FABRIQUER la boîte
├── tests/             ← prototypes et pieces d'essais
└── deploiement/       ← comment INSTALLER la boîte sur le terrain

```

### 📁 `fabrication/` : construire la boîte

Pour ceux qui doivent **produire une boîte**, à partir de zéro ou pour en refaire une. Ce dossier contient :

- les **fichiers de conception** (lien Onshape, fichiers STEP modifiables, fichiers STL prêts à imprimer) ;
- les **paramètres d'impression** des pièces et des moules ;
- la **fabrication des joints** en silicone coulé (moules, mélange, coulage, démoulage) ;
- l'**assemblage** de la boîte, étape par étape ;
- les **protocoles de test** d'étanchéité ;
- les **retours d'expérience** : ce que nous avons essayé, ce qui n'a pas marché et pourquoi.

➡️ [Aller à la fabrication](fabrication/README.md)

### 📁 `deploiement/` : installer la boîte sur le terrain

Pour ceux qui ont **une boîte prête**, dans sa mallette, et doivent l'installer dans la rivière. Ce dossier contient :

- le **contenu de la mallette** et la préparation avant de partir ;
- l'**installation pas à pas** (tige, lest, immersion) et les vérifications finales ;
- la **récupération** de la boîte et le **dépannage** ;
- une **fiche de déploiement** à imprimer.

➡️ [Aller au déploiement](deploiement/README.md)

---

### 📁 `tests/` : nos prototypes et pièces d'essai

Pour **comprendre comment nous en sommes arrivés à la boîte actuelle**, ou pour **retester une solution** avant de modifier la boîte. Ce dossier contient :

- l'**ancienne version de la boîte** (v1), avec les modèles Onshape de toutes ses pièces : boîte complète, moules des joints, bouchons d'étalonnage, raccord cannelé ;
- les **pièces de test** : des pièces miniatures imprimées pour valider une solution (joint de fermeture, joint des capteurs…) avant d'imprimer la boîte complète.

> ⚠️ Ces pièces ne sont **pas à imprimer pour fabriquer la boîte**. Pour cela, allez dans [`fabrication/`](fabrication/README.md).

➡️ [Aller aux tests](tests/README.md)

---

## Par où commencer ?

| Vous voulez… | Allez à |
|---|---|
| Voir les anciennes versions ou refaire un test | [`tests/`](tests/README.md) |
| Comprendre comment la boîte est conçue | [Vue d'ensemble](#vue-densemble-de-la-boîte), juste en dessous |
| Fabriquer une nouvelle boîte | [`fabrication/`](fabrication/README.md) |
| Modifier la boîte (autre capteur, autre carte…) | [`fabrication/`](fabrication/README.md), partie CAO |
| Installer une boîte déjà prête | [`deploiement/`](deploiement/README.md) |
| Savoir pourquoi un choix a été fait | [`fabrication/`](fabrication/README.md), retours d'expérience |

---

## Vue d'ensemble de la boîte

La boîte est composée de **trois parties** :

| Partie | Rôle | Fermeture |
|---|---|---|
| **Partie haute : électronique** | Contient la carte, le bloc de 6 piles et les composants de transmission. Les sondes de température y entrent par des passages étanches. | Couvercle vissé (vis M5 et écrous) avec joint silicone |
| **Partie basse : capteur** | Contient le transducteur de pression et la cavité où arrive l'eau. Elle est coupée selon l'axe y pour permettre un joint continu et bien serré. | Vis M5 et écrous avec joint silicone |
| **Support des poids** | Boîte ouverte qui reçoit le lest, en quantité adaptée au site. | Fermoirs grenouilles |

La boîte s'utilise avec une **tige**, enfoncée dans le lit de la rivière, qui porte les sondes de température.

### Les grands principes de conception

- **Une boîte en plusieurs parties**, pour garder des pièces simples à imprimer. Les passages des sondes sont formés de deux demi-trous, un sur chaque partie, qui se referment autour du câble.
- **Des joints en silicone coulé** dans des moules imprimés, dont la dureté est réglée en mélangeant deux silicones.
- **Un serrage métal sur métal** : les écrous M5 sont logés dans la boîte et serrés à la visseuse. C'est le serrage, autant que le joint, qui garantit l'étanchéité.
- **Un modèle paramétré** sur Onshape : les dimensions principales sont des variables, ce qui permet d'adapter la boîte sans tout redessiner.

---

## Version actuelle

| Version | Description | Statut |
|---|---|---|
| v1 | Boîte en deux parties coupée selon x | Abandonnée |
| **v2** | Partie basse capteur coupée selon y, partie haute électronique, support des poids séparé | **Version actuelle** |

Le détail des versions et des tests se trouve dans [`fabrication/`](fabrication/README.md).

---

## Contributeurs

Projet MOLONARI : [À COMPLÉTER : école, année, noms de l'équipe]