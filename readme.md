# Processus de Recrutement BIGmama
​
​
Votre candidature a été retenue pour le processus de recrutement de
BIGmama qui est le suivant:
​
- Entretien téléphonique (optionnel):
  - L'objet de cet échange est de donner un aperçu des principales
    étapes du processus de recrutement.
​
- Test pratique:
  - Un dépôt privé sur GitLab est partagé avec vous pour héberger les résultats du test expliqué ci-dessous.
  - Développer la solution en utilisant Git et GitLab pour versionner le projet
  - Envoyer un mail signifiant que vous avez terminé le développement. (délai de 15 jours)
  - Nous allons ensuite évaluer votre solution.
​
## Entretien technique:
​
Un entretien est programmé dans les locaux de BIGmama. Le but de cet
entretien est de donner l'opportunité au candidat d'exposer le spèctre
de ses compétences. Ramener son ordinateur personnel est vivement encouragé.
​
## Entretien relationnel (optionnel):
​
Un second entretien sera planifié dans la mesure du possible. Suite à l'entretien,
vous receverez une réponse.
​
Il arrive qu'un candidat nous intéresse mais que nous ne puissions pas l'embaucher
immédiatement. Nous gardons soigneusement ce candidat dans une liste à part et nous
le contacterons dès que nous avons une opportunité de recruter.
​
​
## Foire aux Questions:
​
### Pour quel poste et quel salaire?
​
Le poste est celui de "Software Developer" basé à Alger avec un salaire mensuel entre 45,000 DZD et 100,000 DZD.
​
​
### Je ne suis pas en mesure de me présenter pour un entretien?
​
Répondre à la chaine mail pour informer de votre indisponibilité au
minimum 24h avant la date prévue de l'entretien, ou appeler la personne
qui vous a contacté par téléphone.
​
### Où en est ma candidature?
​
Nous envoyons des réponses à tous les candidats ayant répondu au test.
Cela peut parfois prendre du temps, mais nous tenons à donner un retour.
Nous allons vous contacter quelle que soit la décision prise.
​
### Je ne peux pas répondre au test présentement (cas de force majeure)
​
Envoyer un mail qui explique la situation.
​
### Quel langage dois-je utiliser?
​
Python est l'un des langages les plus utilisés dans ce domaine, mais
vous pouvez utiliser le langage dans lequel vous êtes le plus à l'aise.
​
Traîter ce dépôt comme un réel projet. Un modèle et une application qui servira
le modèle aux utilisateurs.
​
​
### J'ai des problèmes avec la donnée:
​
Faire au mieux. La réalité est loin des compétitions Kaggle où la donnée est propre, annotée, expliquée.
​
​
## Test
​
Le test implique d'entraîner un modèle et de créer une application qui utilisera ce modèle pour servir
 des utilisateurs non-techniques.
​
Merci d'utiliser Git pour versionner le développement. Un dépôt privé sera partagé avec vous sur GitLab.
​
​
Cette étape consiste à travailler sur un test pratique, qui nous
permettra d’apprécier vos capacités d’apprentissage et de résolution de
problèmes.
​
Une fois que vous aurez finalisé le modèle, créez une application web Flask pour pouvoir 
l'utiliser. L'application acceptera un fichier CSV avec le même schéma que le dataset de test,
 et rendra un tableau de résultats d'inférence du modèle.
​
**Important:** Vous devez produire un document qui explique votre compréhension du problème,
la recherche effectuée sur le sujet (état de l'art) ainsi que la justification de vos choix
 techniques (modèles, métriques, librairies ...) dans la réponse que vous
fournirez.
​
## Dataset
​
Le fichier comporte une base de `train` et de `test`. Elles comportent
l'historique de pubs (ad_id, format) affichées sur des applications
mobiles (support_type, support_id) à un utilisateur (user_id, device_id,
device_model, device_type, device_os, device_language).
​
La boite de pub obtient ces emplacements par un système d'enchère (de
type Vickrey auction), nommé RTB.
​
Voici une petite explication de la signification de certaines variables:
​
  - `bid_floor`: mise minimum
​
  - `won_price`: prix à laquelle l'enchère est remportée
​
  - `bid_price`: prix à laquelle on mise, format 10^11 coût pour mille
     impressions.
​
  - `cpc_price`: indique le cout par clic (format 10^8), c'est à dire à
    quel prix est vendu le clic à l'annonceur .
​
  - `verticals_X`: sont des colonnes qui réfèrent au "classement" de
     l'app, vous pouvez trouver des infos sur le site développer de
     google (recherche google:verticals apps)
​
  - `support_category`: est un classement également des support (site où
    les pubs sont affichées).
​
  - `viewability`: pourcentage de visibilité (-1 si inconnu)
​
  - `position`: position de l'ad sur la page
​
L'objectif est de trouver les probabilités pour la colonne `clicked`,
omise à dessein. La réponse au test est le code que vous avez écrit pour
trouver ces probabilités.
​
Le dataset est localisé à l’emplacement suivant:
​
https://www.dropbox.com/s/9jmpk7jtvnqzcto/data.tar.gz?dl=1