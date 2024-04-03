# POC Protein Feature Extraction

This repository contains the code for the prediction of `Kcat`. This project is a Proof of Concept for my thesis. The main goal is to use different regression models on the dataset created by the Fondant pipeline. The feature that has been predicted is the `Kcat` feature.

## Dataset

The Fondant pipeline was created during my internship for ML6. This pipeline contains multiple components that generate features based on the protein sequence. There are 100+ features generated and the dataset contains 2000+ proteins.

## Models

The models that have been used are:

- Polynomial Regression
- Random Forest
- KNN
- Gradient Boosting
- XGB (Extreme Gradient Boosting)

## Results

The results can be found in the [prediction notebook](./prediction.ipynb) in the `1.7 Conclusion` section. The results are also visualized here:

Model|Train|Validation
 --- | --- | ---
PolynomialRegressor|63.6%|0.0%
KNearestNeighbor|88.8%|76.0%
RandomForestRegressor|93.7%|80.3%
GradientBoostingRegressor|96.3%|79.5%
XGradientBoostingRegressor|100.0%|74.9%

The model used for the prediction the test set is the `GradientBoostingRegressor` model. The model has a `R2` score of `77%` on the test set.
