# Vie privée et RGPD

## Principe absolu : tout en local

Mémoire, historique, réglages, données personnelles : **tout vit sur l'appareil et n'en sort jamais**.

C'est à la fois :
- la meilleure protection RGPD (pas de données collectées, pas de traitement sur un serveur) ;
- la garantie d'un coût de fonctionnement nul (pas de serveur à payer).

## Les trois briques vocales sont locales

| Brique | Rôle | Exigence |
|---|---|---|
| Écoute | La parole devient du texte | Locale |
| Cerveau | Comprendre et décider | Local |
| Voix | Le texte devient du son | Locale |

Si une seule brique envoyait ses données au cloud, la promesse tomberait.

## Les images

- Captures d'écran : analysées **en mémoire vive** puis **détruites immédiatement**, jamais écrites sur le disque, jamais envoyées.
- Modèle de vision : **exécuté sur le téléphone**.
- Pas de reconnaissance faciale ni vocale des tiers (infirmières, visiteurs). L'identification se fait par la conversation (voir [MEMOIRE.md](MEMOIRE.md)).

## Les données d'une seule personne

Bob est mono-utilisateur : il ne contient les données que d'une seule personne.

## Le consentement

### Mention claire dès l'accueil

En langage simple, sans jargon juridique. Exemple :
> « Bob fonctionne entièrement sur votre téléphone. Vos données ne sont jamais envoyées ailleurs, ni conservées par qui que ce soit d'autre que vous. »

### Consentement vocal en deux validations

1. Bob lit les conditions.
2. La personne dit : « J'accepte. »
3. Bob reformule : « Tu es d'accord pour que je t'aide sur ton téléphone, en gardant tout ici, chez toi ? Tu confirmes ? »
4. La personne valide une seconde fois.

### Trace du consentement

À concevoir : garder une **note datée** (« conditions acceptées le … »), sans enregistrement de la voix.

## Exception : les API Google

L'accès à Gmail, Agenda, Contacts ou Drive passe par les serveurs de Google, où ces données se trouvent déjà. Bob ne les envoie nulle part ailleurs. Le point exact de ce qui transite reste à examiner en phase technique (voir [QUESTIONS_OUVERTES.md](QUESTIONS_OUVERTES.md)).
