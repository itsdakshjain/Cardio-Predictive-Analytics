# 🫀 Cardio Predictive Analytics Dashboard
A clinical decision support tool built with Scikit-Learn and Streamlit to predict cardiovascular risk based on patient biomarkers.

### 🚀 [Live App Link](https://itsdakshjain-cardio-analytics.streamlit.app/)

## 🧪 Model Selection
I evaluated 5 different classification algorithms using an initial 80/20 train-test split. While **KNN** initially showed the highest accuracy on a single split, I moved to **5-Fold Cross-Validation** to ensure model stability across the entire dataset.

### Initial Performance (Test Set):
| Model | Accuracy | F1 Score |
| :--- | :--- | :--- |
| **KNN** | **88.59%** | 0.8986 |
| Logistic Regression | 87.50% | 0.8878 |
| Naive Bayes | 86.96% | 0.8788 |
| SVM (RBF Kernel) | 86.41% | 0.8804 |
| Decision Tree | 76.63% | 0.7817 |

### 🛡️ Final Validation (5-Fold Cross-Validation)
I performed Cross-Validation on the top-performing models to check for variance and generalization:

| Model | CV Mean Accuracy | Std Deviation (σ) |
| :--- | :--- | :--- |
| **Logistic Regression** | **84.74%** | **0.0264** |
| KNN | 84.60% | 0.0302 |
| Naive Bayes | 83.92% | 0.0207 |

**Decision:** I selected **Logistic Regression** for deployment. Even though KNN was close, Logistic Regression provided a higher mean CV accuracy and a lower standard deviation, making it the more "reliable" and "stable" choice for a clinical application.

## 🛠️ Tech Stack & Pipeline
- **Data Manipulation:** `Pandas` and `NumPy` for efficient data cleaning and transformation.
- **Visualization:** `Seaborn` and `Matplotlib` for Exploratory Data Analysis (EDA).
- **Preprocessing:** `Scikit-Learn`'s `StandardScaler` for numerical normalization.
- **Validation:** 5-Fold Stratified Cross-Validation to ensure model stability.
- **Deployment:** `Streamlit Cloud` for a high-performance web interface.
- **Serialization:** `joblib` for model and scaler persistence.

## ⚙️ Data Engineering Process
To prepare the clinical data for the Logistic Regression model, I implemented the following:
* **One-Hot Encoding:** Converted categorical clinical markers (like Chest Pain Type and ST Slope) into binary vectors to allow the model to interpret non-ordinal data.
* **Feature Scaling:** Applied Z-score normalization to numerical features (Age, Cholesterol, BP) to ensure all features contribute equally to the model's decision boundary.
* **Input Alignment:** Exported feature column names to a `.pkl` file to ensure the web app perfectly matches the model's expected input structure.


Cardio-Predictive-Analytics
A practise project .
