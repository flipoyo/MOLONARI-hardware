# MOLONARI – Boîte étanche du capteur

Boîte imprimée en 3D qui protège l'électronique d'un capteur MOLONARI immergé, tout en laissant passer les sondes de température et en exposant le transducteur de pression à l'eau.

Ce dépôt contient tous les fichiers de conception (Onshape, STEP, STL) et les instructions pour **fabriquer, assembler et tester** la boîte de A à Z.

---

## Sommaire

1. [Liste du matériel](#liste-du-matériel)
2. [Fabrication pas à pas](#fabrication-pas-à-pas)
3. [Modifier la boîte](#modifier-la-boîte)
4. [Historique des versions](#historique-des-versions)



## Liste du matériel

### Impression
| Élément | Détail |
|---|---|
| Imprimante 3D | 
| Filament boîte | PLA et TPU |

### Quincaillerie
| Élément | Quantité | Remarque |
|---|---|---|
| Vis M5 | 6 | Inox recommandé (milieu humide) |
| Écrous M5 | 6 | Insérés dans les logements imprimés |
| Poids de 2kg | 2 | Placé dans le support des poids |

### Joints
| Élément | Remarque |
|---|---|
| Silicone  BLUESIL RTV 147A | 50% |
| Silicone  BLUESIL RTV 148A| 50% |
| Activateur / catalyseur  BLUESIL RTV 147B| 10% |
| Balance de précision, gobelets, bâtonnets, seringue ou pipette | Pour doser et couler |

### Outillage
- Visseuse (indispensable pour un serrage suffisant)
- Clé Allen / embout adapté aux vis
- Barre à mine et masse (pose de la tige sur le terrain)

---

## Fabrication pas à pas

| Étape | Guide | Durée indicative |
|---|---|---|
|1. Récupérer les documents sur Onshape. Si vous le souhaitez, vous pouvez modifié les mesures dans le tableau de données pour mettre la boite aux mesures que vous préferez. | lien | 1h
| 2. Imprimer les pièces de la boîte, la sonde et les moules, telecharger au format STL et mettez les sur l'appli de votre imprimante (bambulab, Ultimaker Cura...). Verifier qu'il s'agit des bonnes dimensions, mettez les trous plutot vers le ciel, verifiez que c'est bien en PLA et slicer puis imprimer. | docx au fomat STL | ~2-3 jours d'impression |
| 2. Couler les joints en silicone | [`docs/02_joints.md`](docs/02_joints.md) | 24 h de séchage |
| 3. Assembler la boîte avec les vis, utilisez une visseuse.| [`docs/03_assemblage.md`](docs/03_assemblage.md) | 10min|
| 4. Tester l'étanchéité avant déploiement | [`docs/04_tests.md`](docs/04_tests.md) | 6 h minimum |

> 💡 Lancez le coulage des joints **pendant** l'impression de la boîte pour gagner une journée.

---

## Modifier la boîte

Le modèle Onshape est paramétré : on modifie les **variables** (dimensions extérieures, épaisseur des parois, entraxe des vis, position des sondes…), et toutes les pièces se mettent à jour en restant compatibles entre elles.

Tout est expliqué dans [`cao/README.md`](cao/README.md).

**Règles à respecter :**
- ne jamais saisir une dimension partagée « en dur » : utiliser les variables ;
- si vous modifiez une gorge de joint, **modifiez aussi le moule correspondant** ;
- exportez à nouveau les fichiers STEP et STL, puis créez une version dans Onshape à chaque étape validée par un test.

---

## Historique des versions

| Version | Description | Statut |
|---|---|---|
| v1 | Boîte en deux parties coupée selon x, raccord cannelé coupé en deux | Abandonnée : logements de joints mal imprimés, étanchéité non testable. Fichier dans `cao/archives/v1/` |
| v2 | Nouvelle architecture : partie basse capteur coupée selon y, partie haute électronique, support des poids séparé | **Version actuelle** |

