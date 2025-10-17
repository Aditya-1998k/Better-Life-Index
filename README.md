# Better Life Index Prediction

A Machine Learning project to predict **Life Satisfaction** of countries based on economic and social indicators, using **Linear Regression** and **k-Nearest Neighbors (k-NN) Regression**.

---

## 📖 Project Overview

The **Better Life Index** project aims to analyze how factors like **GDP per capita** influence the life satisfaction of a country. Using the Life Satisfaction dataset (`lifesat.csv`) from [Aurélien Géron’s data repository](https://github.com/ageron/data), we explore:

- The relationship between GDP per capita and life satisfaction.
- How Linear Regression can model the global trend.
- How k-Nearest Neighbors (k-NN) Regression can predict values based on nearest countries.

---

## 🗂 Dataset

- **Source:** [https://github.com/ageron/data](https://github.com/ageron/data)  
- **File:** `lifesat/lifesat.csv`  
- **Features include:**
  - `Country`
  - `GDP per capita (USD)`
  - `Life satisfaction`

---

## 🧠 Approach

### 1. Data Exploration
- Checked data types, missing values, and duplicates.
- Visualized distributions using **boxplots** and **scatter plots**.
- Observed a roughly linear relationship between **GDP per capita** and **Life Satisfaction**.

### 2. Linear Regression
- Trained a **Linear Regression** model using `GDP per capita` as the independent variable.
- Predicted **Life Satisfaction** for a given country (e.g., Cyprus ≈ 6.3).
- Pros: Easy to interpret, captures global trend.  

### 3. k-Nearest Neighbors Regression
- Used **k = 3** to predict Cyprus’ life satisfaction based on nearest GDP countries:
  - **Israel** → 7.2  
  - **Lithuania** → 5.9  
  - **Slovenia** → 5.9  
- Average = 6.33, close to Linear Regression prediction.
- Pros: Captures local patterns, non-linear relationships.

---
