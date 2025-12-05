# 🌦️ Streamlit Rainfall Prediction WebApp

🔗 **Live Demo**: [Click here to try the deployed app](https://rainfall-predictor-webapp.streamlit.app/)

---

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b.svg)](https://streamlit.io/)

[![Model](https://img.shields.io/badge/Model-Logistic%20Regression-brightgreen.svg)](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)  

[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

This project is an interactive **rainfall prediction tool** built with **Streamlit** and powered by a trained **Logistic Regression** model. Users can input real-time weather parameters and obtain predictions for **rainfall occurrence**.

The model was trained on the `Rainfall.csv` dataset and tested with multiple classifiers in the notebooks. **Logistic Regression achieved the best performance** for this dataset.

> ⚠️ **Disclaimer**: This application is for **educational and research purposes only**. It is **not a substitute for official weather forecasts**. For real weather information, consult accredited meteorological sources.

---

## 📁 Project Structure

```bash
Rainfall-Predictor/
│
├── app/
│   └── main.py
├── dataset/
│   └── Rainfall.csv
├── notebook/
│   ├── main.ipynb
│   └── research.ipynb
├── models/
│   ├── logreg_rainfall_model.pkl
│   └── rainfall_model.sav
├── requirements.txt
├── README.md
└── LICENSE
```
---

## 🚀 Features

- 🎚️ **Interactive Inputs** for key weather parameters:
  - Pressure (hPa)
  - Temperature (°C)
  - Humidity (%)
  - Cloud Cover (%)
  - Sunshine (hours)
  - Wind Direction (°)
  - Wind Speed (m/s)
- 🔍 **Real-Time Predictions** using a trained Logistic Regression model
- 📊 **Optional Probability Scores** per class (Rain / No Rain)
- ⚠️ **Educational Disclaimer** for responsible usage

---
## ⚙️ Installation

### 🔐 Prerequisites
- Python ≥ 3.10
- Conda (recommended)
- Git

### 📦 Setup Guide
1. Clone this repository:
```bash
git clone https://github.com/yourusername/rainfall_predictor.git
cd rainfall_predictor
```

2. Create a new Conda environment:
```bash
conda create -n rainfall-predictor python=3.12
```

3. Activate the Environment
```bash
conda activate rainfall-predictor
```

4. Install Dependencies
```bash
pip install -r requirements.txt
```

5. Run the Streamlit Application
```bash
cd app
streamlit run main.py
```

---

## 🙋‍♂️ Questions or Feedback?

Feel free to open an issue or reach out if you have suggestions, questions, or ideas to improve this project.
---

### Built by [@kamijoseph](https://github.com/kamijoseph) using [Streamlit](https://streamlit.io/)
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dxqvqgszvwaiu889yccfmv.streamlit.app/)
