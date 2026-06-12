# 🔥 Fire Weather Index (FWI) Predictor

This project predicts the **Fire Weather Index (FWI)** — a key indicator of wildfire risk — using multiple **machine learning regression models**.  
The notebook explores environmental data, preprocesses it, trains multiple models, and evaluates their performance to identify the best predictor.

---

## 📘 Project Overview

Wildfires are one of the most severe natural hazards, influenced by weather conditions such as temperature, humidity, and wind.  
This project aims to build a machine learning model that predicts the **FWI** to help monitor and manage fire-prone areas.

---

## 🧠 Models Used

The notebook experiments with the following regression models:

- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**
- **ElasticNet Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
The final deployed model uses **Ridge Regression**, chosen for its robustness against multicollinearity in weather data.

---

---

## 📊 Evaluation Metrics

The following metrics were used to assess model performance:

- Root Mean Squared Error (RMSE)  
- Mean Squared Error (MSE)  
- R² Score (Coefficient of Determination)  
- Accuracy (for comparison)

Among these, **Ridge Regression** and **Random Forest** provided the most accurate predictions based on RMSE and R² scores.

---

## ⚙️ Project Workflow

### ** Data Collection**
- Collected structured FWI dataset with features: *Temperature, RH, Wind Speed, Rain, FFMC, DMC, ISI, and Region*.
- Ensured data consistency and formatting before loading into Pandas.

### ** Data Exploration & Preprocessing**
- Checked for missing values and outliers using boxplots and statistics.
- Visualized feature distributions and correlations.
- Encoded categorical variables (e.g., Region).
- Cleaned dataset stored for modeling.

### ** Feature Engineering & Scaling**
- Selected top correlated features with FWI.
- Normalized features using **StandardScaler**.
- Split data into training and test sets.
- Saved the scaler as `scaler.pkl` for deployment.

### ** Model Training**
- Trained multiple regression models including **Ridge Regression**.
- Tuned hyperparameters (e.g., alpha for Ridge).
- Saved the best-performing model as `ridge.pkl`.

### ** Evaluation & Optimization**
- Used metrics: **MAE**, **RMSE**, and **R² Score**.
- Visualized predicted vs. actual values.
- Optimized model hyperparameters to minimize RMSE.

### ** Deployment via Flask**
- Built a **Flask web app** for user interaction.
- Developed `index.html` for input form and `home.html` for results display.
- Integrated the trained model and scaler for real-time predictions.
- Output: FWI prediction displayed instantly upon form submission.
---

## 🧩 Technologies and Libraries

- **Python 3**
- **NumPy, Pandas** – for data manipulation  
- **Matplotlib, Seaborn** – for visualization  
- **Scikit-learn** – for ML models and metrics  
- **Jupyter Notebook** – for development and experimentation  

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Pavani-Cheviti/FWI_PREDICTION.git
   cd FWI_PREDICTION
   ```

2. Open the notebook:
   ```bash
   jupyter notebook "Pavani Cheviti_FWI Predictor3.ipynb"
   ```


3. Run all cells to reproduce the results.


4. Run the Flask App:
 ```bash
  python app.py
 ```
5. Open in Browser:

```bash 
Go to → http://127.0.0.1:5000/
```

Enter the input values and get your FWI prediction instantly.

---

## 📈 Future Improvements

- Try **XGBoost** or **LightGBM** for improved performance.  
- Deploy as a **Streamlit web app** for interactive FWI prediction.  
- Integrate with real-time weather APIs for live fire risk monitoring.  

---

## 👩‍💻 Author

**Pavani Cheviti**  
Project: *Fire Weather Index (FWI) Predictor*  
GitHub: [Pavani-Cheviti](https://github.com/Pavani-Cheviti)

---

## 🪶 License

This project is open-source under the [MIT License](LICENSE).
