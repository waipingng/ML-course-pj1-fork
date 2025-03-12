# Investigating the Relationship between Demographic Factors and Heart Disease Mortality

## Goal of the project

This analysis investigates the relationship between demographic characteristics—specifically median income, ethnicity, and gender distributions—and heart disease mortality rates at the county level. Understanding these relationships can guide targeted public health interventions aimed at reducing heart disease-related mortality.

## Sources of the data

### Primary Data Sources:
- **U.S. Census Bureau**
  - Link: [census.gov](https://www.census.gov/)
  - Provides detailed demographic income data by county.

- **Heart Motality Data**
  - Link: [wXXX](XXX)
  - Provides age-adjusted heart disease mortality rates at the county level.


### Data Collection Methods:
- Demographic data sourced from the U.S. Census Bureau, primarily using decennial census data supplemented by the American Community Survey (ACS).
- Heart disease mortality data sourced from XXX.

### Relevant Features:
- **Median Income:** Median household income at the county level.
- **Ethnicity Distribution:** Proportions of different ethnic groups within each county.
- **Gender Ratio:** Gender composition, specifically the ratio of male to female residents.
- **Heart Disease Mortality Rate:** Age-adjusted heart disease mortality per 100,000 population.

### Data Limitations:
- Data aggregation at the county level obscures finer-scale (e.g., neighborhood-level) variations.
- Census data relies on self-reporting, potentially introducing reporting biases.
- Income data does not account for income inequality or detailed economic disparities within counties.
- Missing mortality data in sparsely populated counties due to confidentiality restrictions.

### Data Reproduction:
- install additional package: pip install requirements.txt
- run data cleaning and combine the income data from census to heart motality data: python code/data_comb.py, result is saved as merged_data.csv in cleaned_data folder
- combine additional demographic data from census, such as gender and ethnicity to the abovementioned data: python code/data_comb_census.py, result is saved as merged_data_add in cleaned_data folder
- run OLS model: python code/ols.py
- run KNN model: python code/knn.py
- run randomforest model: python code/randomforest_bestparameters.py
- run other models and compare the predictions: python code/pred.py

## Modeling Approaches

### Models Explored:
- **Linear Regression:** A baseline approach assuming linear relationships.
- **Random Forest Regression:** Robust to non-linearities and interactions between demographic features.
- **Stochastic Gradient Descent (SGD):** Efficiently optimizes models on large datasets by updating weights incrementally (more than 20,000 rows.
- **Support Vector Regression (SVR):** Effectively captures nonlinear relationships using kernel tricks while being robust to outliers. Its ability to generalize well with limited data makes it a strong choice for complex regression tasks.
- **Neural Network (MLP):** it can model complex nonlinear relationships using multiple layers and activation functions, making it effective for high-dimensional feature learning.

### Evaluation Metrics:
- Root Mean Squared Error (RMSE)
- R-squared (R²)


### Evaluation Results

| Model                      | RMSE (lower is better) | R² (higher is better) |
|-----------------------------|-------------------------|-------------------------------|
| Linear Regression             | High (~100)           | ~0.55 |
| Decision Tree Regression     | Moderate RMSE, ~80       | Moderate R², ~0.6            |
| Random Forest                | 99.66         | 0.6017               |
| SGD Regression               | 93.15                | 0.6626                       |
| SVR                          | 125.73            | 0.3852           |
| Neural Network (MLP)         | **81.12**    | **0.7441**           |

## 3.1 Limitations of Modeling

- Linear models failed to capture complex non-linear relationships.
- Tree-based models, while performing well, may present interpretability challenges.
- The neural network's complexity and potential overfitting were concerns given limited interpretability.

## Futher Research

### Recommended Model:
- **Neural Network** is recommended due to the best overall balance between predictive accuracy (lowest RMSE and high R² score) and interpretability, making it suitable for practical application in public health policy formulation.

### Recommendations for Future Analysis:
- Integrate additional demographic and socioeconomic data (e.g., education levels, employment status, healthcare access).
- Perform analysis at finer resolutions (e.g., zip code level) to refine public health targeting and interventions.


