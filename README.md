# 🎉 PartyLens

**Predict student event turnout using social media and weather data.**

PartyLens is a machine learning-powered dashboard designed to help event organizers make informed decisions by predicting student turnout at campus events. It combines social media engagement signals and weather data to forecast attendance in real time.

---

## 🚀 Features

- 📊 **Turnout Prediction** using Random Forest, Decision Tree, and Logistic Regression models  
- 🧠 **Custom Feature Engineering** based on Instagram buzz (likes, hashtags, post count) and weather conditions  
- 💻 **Interactive Streamlit Interface** where users can input event details and receive predictions  
- 📈 **Data Analysis Notebooks** for exploratory data analysis and model training

---

## 🛠️ Tech Stack

- **Languages**: Python  
- **Libraries**: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `streamlit`  
- **Tools**: Jupyter Notebook, Git/GitHub  

---

### 📂 Project Structure

```
PartyLens/
├── app.py                        # Streamlit app code
├── data/
│   ├── party_data.csv            # Raw event data
│   └── party_data_cleaned.csv    # Cleaned dataset
├── notebooks/
│   ├── 01_data_prep.ipynb        # Data cleaning and preparation
│   ├── 02_eda.ipynb              # Exploratory data analysis
│   └── 03_modeling.ipynb         # Model training and evaluation
├── Party_Lens_Final_Report.ipynb # Final summary report
├── .streamlit/                   # Streamlit configuration files
│   └── config.toml
├── README.md                     # Project documentation
└── LICENSE                       # Open-source license file
```




---

## 📈 Example

Try predicting turnout for a hypothetical event:
- 💬 12 Instagram posts  
- ❤️ 200 total likes  
- ☀️ Sunny  
- Day of the week: Saturday

→ The model returns a high turnout prediction!

---

## 👩‍💻 Authors

- Alina Miret Shah [@amshah1022](https://github.com/amshah1022)
  
---

## 📄 License

This project is open source under the [MIT License](LICENSE).

