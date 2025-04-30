# 🏍️ Used Bike Price Prediction

This project involves end-to-end data analysis and machine learning modeling on a dataset of used bikes to predict their selling price based on features like brand, age, kms driven, and city.

## 🔧 Tools & Technologies
- **Python**, **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Scikit-learn**: for ML modeling (Linear Regression, Random Forest, etc.)
- **Preprocessing Pipelines**
- **Visualization**: Histogram, Correlation Matrix, Scatter plots

## 📊 Problem Statement
Build a predictive model to estimate the selling price of a used bike based on its features.

## 🧹 Data Cleaning
- Removed noisy bike names and version labels.
- Handled duplicates (30K).
- EDA
- Normalized and visualized distributions (price, kms, etc.)

## 🚀 ML Modeling
- Built a preprocessing + modeling pipeline using `ColumnTransformer` and `Pipeline`
- Trained a **Random Forest Regressor** achieving:
  - **MAE**: ~3,123
  - **RMSE**: ~23,845
  - **R² Score**: ~0.93

## 🔮 Prediction Function
Includes a custom function to input new bike details and get price predictions using the trained pipeline.

## 📈 Future Scope
- Outlier detection and treatment

## Deployment
- Used pkl to save the model
- Used streamlit to create a interface to get user input and predict accordingly

## 📁 Dataset
Dataset sourced from a public used bike sales repository.
