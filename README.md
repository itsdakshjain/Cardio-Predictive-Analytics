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


Cardio-Predictive-Analytics
A practise project with eda, preprocessing , scaling, model building, streamlit app
