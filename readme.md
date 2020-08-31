# Ads-Click-Through-Rate-CTR-Prediction

## Project Intro/Objective
In this project, I worked on the analysis of the data about the affected cases by Coronavirus. The datasets are provided by Johns Hopkins Github repository and they are updated daily. 
The Data Science skills shown are: 
* Wrangling, transforming and cleaning time-series, Data Visualization. 
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

### Methods Used
* Data Wrangling 
* Timeseries cleaning and merging 
* Data Visualization

### Technologies
* Python
* Pandas, jupyter

## Needs of this project

- data exploration/descriptive statistics
- data processing/cleaning

## Getting Started

1. Clone this repo to your computer (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](https://github.com/DzAnalytics/Ads-Click-Through-Rate-CTR-Prediction/tree/master/data) within this repo.


### Install the requirements
1. Make sure you use Python 3 and Jupyter Notebook.
2. Install the requirements using pip install -r requirements.txt.

### Usage
Open Ads-Click-Through-Rate-CTR-Prediction.ipynb using Jupyter Notebook and Run the notebook.
Or, If you want just show our project without installation. a web page is provided [here](https://ads-ctr-prediction.herokuapp.com/) 

## The Developer


|Name     |  Slack Handle   | 
|---------|-----------------|
|[Mohamed Merabet](https://github.com/DzAnalytics)| @DzAnalytics       |


* Feel free to contact the Developer with any questions or if you are interested in contributing!
