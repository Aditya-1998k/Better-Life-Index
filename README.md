# Better Life Index Predictor API

A **FastAPI-based REST API** that predicts the Better Life Index (BLI) for a country based on its GDP per capita. The API returns the predicted BLI along with a comparison to the average.

---

## Project Structure
```text
Better-Life-Index/
│
├── backend/
│ ├── app.py 
│ ├── utilities/
│ │ ├── init.py
│ │ ├── logging_config.py
│ │ └── model_loader.py
| |
│ ├── var/log/ # Logs for predictions
| |
| ├── models/
|    ├── better_life_model.pkl # Trained Linear Regression model
|    └── Better_Life_Index.ipynb# Notebook for model training
│
├── requirements.txt
└── .gitignore
```
---

## Features

- Predict Better Life Index using GDP per capita.
- Returns whether the country's BLI is "better than average" or "worse than average".
- Logs all predictions and validation errors to `var/log/backend.log`.
- Swagger UI available at `/docs` for easy testing.
- Clean separation of concerns: model loading, logging, and API logic.

---

## Requirements

- Python 3.10+
- FastAPI
- scikit-learn
- pandas
- numpy
- joblib
- uvicorn

## Project Setup
1. create a virtual Environment: `python -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Install the dependency
```bash
pip install -r backend/requirements.txt
```

## Run the API
1. `cd backend`
2. run the command : `uvicorn app:app --reload`
3. Access Swagger UI: http://127.0.0.1:8000/docs
<img width="1326" height="676" alt="image" src="https://github.com/user-attachments/assets/b2261661-c308-4fce-ab65-4890e673cf6f" />
4. PostMan
<img width="940" height="491" alt="image" src="https://github.com/user-attachments/assets/67ecc21f-1028-4e97-918c-0be7f2d18662" />


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
