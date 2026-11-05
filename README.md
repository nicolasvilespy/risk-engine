# Risk Engine

## Objectif
Produire un rapport quotidien de risque de marché pour un portefeuille multi-actifs :
mesurer les pertes potentielles, surveiller les limites et expliquer les variations de risque d'un jour à l'autre.

## Périmètre
Inclus progressivement :
1. Actions, indices, FX et matières premières
2. Options vanilles, valorisées par modèle
3. Une option exotique à barrière ou un produit structuré simple

Exclus pour l'instant : risque de crédit, liquidité et risque intraday.

## Mesures
- Volatilité, VaR historique et Expected Shortfall, à 99 % sur 1 jour
- Pour les options : delta, gamma, vega et theta
- Stress tests sur les prix et la volatilité

## Devise de référence
USD.

## Validation
Comparer chaque VaR aux pertes réelles du lendemain.
Sur 250 jours, on attend environ 2 à 3 dépassements à 99 %.
Pour les options, vérifier les prix du modèle avec des cas simples et des résultats de référence.

## Portefeuille fictif
Valeur : 1 000 000 USD.

| Actif | Ticker | Poids |
|---|---|---|
| S&P 500 | SPY | 25 % |
| TSMC | TSM | 15 % |
| BNP Paribas | BNP.PA | 15 % |
| Or | GLD | 15 % |
| Tencent | 0700.HK | 10 % |
| Exxon | XOM | 10 % |
| Nestlé | NESN.SW | 10 % |

Couverture de change : vente de 150 000 USD d'équivalent EUR contre USD (EURUSD=X),
hors carry dans la V1.

## Données et hypothèses
- Source : Yahoo Finance, prix de clôture ajustés.
- Les prix sont convertis en USD avant le calcul des rendements.
- Seules les dates où tous les marchés ont un prix sont conservées.
- Limite : un rendement peut donc couvrir plusieurs jours de marché.
- Limite : les clôtures ont lieu à des heures différentes selon les marchés.

### Expected Shortfall
ES historique sur 1 jour, sur environ 10 ans de données, avec la convention <= pour la queue :
- 95 % : 22 171 USD
- 97,5 % : 27 939 USD
- 99 % : 38 115 USD

12 des 26 journées sous la VaR à 99 % ont eu lieu en 2020 : les pertes extrêmes sont regroupées dans le temps.