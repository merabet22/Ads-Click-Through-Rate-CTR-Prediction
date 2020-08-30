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
  - `verticals_X`: sont des colonnes qui réfèrent au "classement" de
     l'app, vous pouvez trouver des infos sur le site développer de
     google (recherche google:verticals apps)
​
  - `support_category`: est un classement également des support (site où
    les pubs sont affichées).
​
  - L'objectif est de trouver les probabilités pour la colonne `clicked`,
omise à dessein. La réponse au test est le code que vous avez écrit pour
trouver ces probabilités.

Try the application here
