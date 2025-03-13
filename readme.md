# Investigating the Relationship between Demographic Factors and Heart Disease Mortality

# Goal of the project

This analysis investigates the relationship between demographic characteristics—specifically income, ethnicity, and gender to predict heart disease mortality rates at the county level. Understanding these relationships can guide targeted public health interventions aimed at reducing heart disease-related mortality.

## Sources of the data

### Primary Data Sources:
- **U.S. Census Bureau**
  - Link: [census.gov](https://www.census.gov/)
  - Provides detailed demographic data (income, ethnicity, gender) by county.

- **Heart Motality Data**
  - Link: [U.S. Department of Health & Human Services-Heart Disease Mortality](https://catalog.data.gov/dataset/heart-disease-mortality-data-among-us-adults-35-by-state-territory-and-county-2019-2021)
  - Provides age-adjusted heart disease mortality rates at the county level.


### Data Collection Methods:
- Demographic data sourced from the U.S. Census Bureau, primarily using decennial census data supplemented by the American Community Survey (ACS).
- Heart disease mortality data sourced from U.S. Deapartment of Health & Human Services-Heart Disease Motality.

### Relevant Features:
- **Income:** catergorial household income at the county level.
- **Ethnicity:** Proportions of different ethnic groups within each county.
- **Gender:** Gender composition, specifically the ratio of male to female residents in each county.
- **Heart Disease Mortality Rate:** Age-adjusted heart disease mortality per 100,000 population.

### Data Limitations:
- Data aggregation at the county level obscures finer-scale (e.g., neighborhood-level) variations.
- Census data relies on self-reporting, potentially introducing reporting biases.
- Income data does not account for income inequality or detailed economic disparities within counties.
- Missing mortality data in sparsely populated counties due to confidentiality restrictions.

## Data Reproduction:
- install additional package: pip install -r requirements.txt
- run preprocess.ipynb file for all pre-processing data.
- run pred.ipynb file for all prediction results.

## Modeling Approaches

### Data Preprocessing
- Extracted only the necessary columns from the dataset and removed rows with missing values.
- Merged the dataset with regional income distribution data to complete the dataset.
- Applied one-hot encoding to categorical variables.
- Scaled the remaining numerical features using a standard scaler for normalization.

### Models Explored
- **Linear Regression:** Serves as a baseline, assuming a linear relationship between features and the target variable.  
- **Decision Tree Regression:** Captures non-linear patterns by recursively splitting the data based on feature values.  
- **Random Forest Regression:** Enhances robustness by averaging multiple decision trees, reducing overfitting and capturing complex feature interactions.  
- **Stochastic Gradient Descent (SGD):** Efficiently optimizes models for large datasets (20,000+ rows) by updating weights incrementally.  
- **Support Vector Regression (SVR):** Leverages kernel tricks to model non-linear relationships while remaining resilient to outliers, making it effective for limited data scenarios.  
- **Neural Network (MLP):** Learns complex, high-dimensional patterns using multiple layers and activation functions, making it suitable for deep feature extraction.  

### Evaluation Metrics:
- Root Mean Squared Error (RMSE)
- R-squared (R²)


## Results

| Model                      | RMSE (lower is better) | R² (higher is better) |
|-----------------------------|-------------------------|-------------------------------|
| Linear Regression             | 95.99        | 0.6330 |
| Decision Tree Regression     | 116.89      | 0.4558           |
| Random Forest                | 101.57         | 0.5891               |
| SGD Regression               | 95.89                | 0.6338                       |
| SVR                          | 123.27            | 0.3948           |
| Neural Network (MLP)         | **84.81**    | **0.7135**           |

### Interpretation
The neural network (MLP) produced the most accurate predictions, followed by SGD and Linear Regression. This suggests that the strong performance of linear models indicates a direct correlation between income and mortality, reinforcing income as a key predictor of heart disease mortality rates.

## Futher Research

### Recommended Model:
- **Neural Network** is recommended due to the best overall balance between predictive accuracy (lowest RMSE and high R² score) and interpretability, making it suitable for practical application in public health policy formulation.

### Recommendations for Future Analysis:
- Integrate additional demographic and socioeconomic data (e.g., education levels, employment status, healthcare access).
- Perform analysis at finer resolutions (e.g., zip code level) to refine public health targeting and interventions.


