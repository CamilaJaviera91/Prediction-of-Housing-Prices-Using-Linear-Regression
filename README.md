# Kaggle Dataset Fetcher and Predictor

This project provides tools to search for datasets on Kaggle, download and preprocess them, and perform predictions using a Linear Regression model. It includes interactive text-based user interfaces built with `curses`.

## Features

- Search for datasets on Kaggle interactively.
- Download datasets and automatically extract files.
- Load datasets into a pandas DataFrame and preprocess them.
- Train a Linear Regression model and evaluate it using RMSE and MAE.
- Visualize results with scatter plots.

---

## Prerequisites

1. **Python**: Python 3.7 or higher.
2. **Install Required Libraries**:
<br>
   
   ```bash
   pip install pandas numpy matplotlib scikit-learn kaggle
   ```

## Set Up Kaggle API:

- Go to Kaggle Account.
- Download the kaggle.json API token.
- Place it in ~/.kaggle/ (Linux/Mac) or %USERPROFILE%\.kaggle\ (Windows).

## File Structure
```bash
.
├── kaggle_connect.py  # Handles dataset search and download via Kaggle API.
├── prediction.py      # Performs data preprocessing, model training, and visualization.
└── README.md          # Documentation for the project.
```