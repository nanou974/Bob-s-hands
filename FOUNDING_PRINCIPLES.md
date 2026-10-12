# Principes fondateurs de Bob's Hands

Ces principes sont la colonne vertébrale du projet. Toute décision technique ou fonctionnelle doit les respecter. Si une idée en contredit un, c'est l'idée qui change, pas le principe.

---

## 1. La voix suffit à tout

Aucune fonction, aucun réglage, aucun paramètre ne peut dépendre d'un geste de la main.
Si une chose existe dans Bob, elle est pilotable à la voix. Sans exception.

*Pourquoi : le public premier ne peut pas toucher l'écran. Une seule fonction tactile obligatoire suffit à l'exclure.*

## 2. Rien ne sort du téléphone

Tout fonctionne **en local** : la mémoire, l'historique, les réglages, les données personnelles.
Et cela vaut pour **les trois briques de la chaîne vocale** :

1. **L'écoute** (reconnaissance de la parole)
2. **Le cerveau** (le modèle de langage qui comprend et décide)
3. **La voix** (la synthèse vocale)

Si une seule de ces briques envoyait des données dans le cloud, la promesse tomberait. Les captures d'écran analysées par Bob sont traitées en mémoire vive puis détruites, jamais écrites sur le disque, jamais envoyées.

*Promesse faite à l'utilisateur : « Rien de ce que vous dites, rien de votre écran n'a jamais quitté votre téléphone. »*

## 3. Gratuit, complet, pour tout le monde

L'application est et restera **entièrement gratuite**. Les personnes en situation de handicap ont souvent peu de moyens : l'accessibilité ne doit pas être un privilège payant.

- Pas d'abonnement, pas de « Bob premium ».
- Le don est possible, mais **totalement décorrélé des fonctions** : aucun avantage réservé aux donateurs.
- Le coût de fonctionnement doit rester **proche de zéro** : IA gratuites et locales, pas de serveur à payer.

## 4. Bob ne touche jamais à l'argent

Les **applications et comptes bancaires sont une zone interdite par conception**. Non négociable.

*Pourquoi : le risque est maximal et irréversible, et c'est la première porte d'entrée des arnaques visant un public vulnérable.*

## 5. Rien d'irréversible sans double confirmation

Toute action sensible (envoyer, supprimer, publier, acheter) demande une **confirmation en deux temps**, formulée **deux fois différemment** pour éviter le « oui, oui » machinal.
Le mot **« stop »** ou **« annule »** arrête Bob net, à tout moment.

*Pourquoi : la personne ne peut pas rattraper une erreur d'un geste.*

## 6. Un appareil, une personne, un Bob

Pas de multi-utilisateur. Bob connaît une seule personne et ne garde que ses données.
Les proches, aidants et soignants utilisent le téléphone normalement grâce à l'accès classique conservé (un glissement vers le haut ouvre le tiroir d'applications Android).

## 7. Bob est une couche, pas un remplaçant

Bob s'ajoute par-dessus le téléphone sans jamais en couper les fonctions vitales. Exemple : quand Bob est en silence total, **la sonnerie des appels continue de fonctionner**. Le silence de Bob ne met jamais la personne en danger.

## 8. Bob apprend et devient

Bob n'a pas une personnalité figée. Il se modèle au fil du temps sur la personne avec qui il vit : son rythme, son vocabulaire, son humour. **Chaque Bob finit unique.**
Son principe directeur est le **mimétisme** : comme un humain, il se synchronise sur son interlocuteur.

## 9. Jamais la faute de la personne

Une incompréhension, un échec, une erreur : Bob reste doux, patient, honnête. Il ne donne **jamais** l'impression que c'est la faute de la personne. Il ne s'agace jamais de répéter.

## 10. Le lien avec le monde avant tout

Bob n'est pas un assistant domotique. Il sert à écrire à ses proches, lire ses mails, écouter de la musique, s'informer, et tout simplement avoir de la compagnie.

## 11. Proposer, ne pas imposer

Bob demande plutôt qu'il ne présume : la liste des personnages à la voix ou à l'écran ? Le mode silence essentiel ou total ? La caméra avant ou arrière ? Il peut suggérer, la personne a toujours le dernier mot.

## 12. Accessible au plus grand nombre

Le public visé a souvent des téléphones anciens. Bob doit viser **la plus large compatibilité possible**, sans renier le principe n° 2. L'arbitrage exact reste à faire (voir [docs/QUESTIONS_OUVERTES.md](docs/QUESTIONS_OUVERTES.md)).
