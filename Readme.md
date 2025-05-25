# Indian Elections 2019: Exploratory Data Analysis and Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Plotly](https://img.shields.io/badge/Plotly-4.0%2B-orange) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0%2B-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## Project Overview

This project conducts an in-depth analysis of the 2019 Indian General Elections, a pivotal event in the world's largest democracy, through **Exploratory Data Analysis (EDA)** and **predictive modeling**. Utilizing two Kaggle datasets, the project employs Plotly for interactive visualizations to explore constituency distributions, party performance, candidate demographics, and criminal cases. A RandomForestClassifier model predicts election outcomes with **90.51% accuracy**, providing a data-driven tool for political forecasting. The analysis offers valuable insights for researchers, analysts, and policymakers, enhancing transparency and understanding of electoral dynamics.

## Objectives

- **Exploratory Data Analysis**:

  - Visualize constituency distributions across Indian states using geospatial and interactive plots.
  - Analyze party performance (win counts, win-loss ratios), gender ratios, educational qualifications, and criminal cases.
  - Create engaging, dark-themed Plotly visualizations for accessibility.

- **Predictive Modeling**:
  - Build a RandomForestClassifier to predict candidate success based on features like party, education, gender, votes, and financial status.
  - Achieve high accuracy (90.51%) with robust metrics (precision, recall, F1-score) and a confusion matrix.
  - Demonstrate practical applicability with sample predictions.

## Datasets

The project uses two publicly available datasets from Kaggle:

1. **Indian Candidates for General Election 2019** (`LS_2.0.csv`):

   - Source: [Kaggle](https://www.kaggle.com/datasets/prakrutchauhan/indian-candidates-for-general-election-2019)
   - Description: Details candidate attributes (e.g., `PARTY`, `EDUCATION`, `GENDER`, `CRIMINAL CASES`, `AGE`, `ASSETS`, `LIABILITIES`, `TOTAL VOTES`, `WINNER`) for ~2,000 candidates across 543 constituencies.
   - Size: ~2,000 rows.

2. **India States** (`Indian_States.shp`):
   - Source: [Kaggle](https://www.kaggle.com/datasets/somacodes/india-states)
   - Description: Geospatial shapefile with state boundaries (`st_nm`) for visualizing constituency distributions.

## Key Findings

- **Geopolitical Trends**: Uttar Pradesh and Maharashtra lead in constituency counts, reflecting large voter bases (visualized via choropleth and sunburst charts).
- **Party Performance**: Bharatiya Janata Party (BJP) secured ~300 constituencies with a high win ratio, followed by Indian National Congress (INC) with ~50 wins.
- **Demographics**: Over 85% of winners are male, indicating gender imbalance. Over 50% of winners are graduates/post-graduates.
- **Criminal Cases**: Major parties (BJP, INC) have candidates with significant criminal records, visualized via Sankey diagram.
- **Predictive Model**:
  - **Accuracy**: 90.51% on test set.
  - **Classification Report**:
    ```
              precision    recall  f1-score   support
           0       0.92      0.95      0.94       331
           1       0.86      0.77      0.81       122
    accuracy                           0.91       453
    ```
  - Confusion matrix (heatmap) confirms strong performance with minimal false predictions.
    ![alt text](confusion_matrix.png)

## Methodology

### 1. Data Preprocessing

- Cleaned column names (e.g., `CRIMINAL\nCASES` to `CRIMINAL CASES`).
- Handled missing values: `CRIMINAL CASES` filled with 0, `AGE` with median, categorical columns with 'Unknown'.
- Converted `ASSETS` and `LIABILITIES` to numeric by removing 'Rs' and commas.
- Ensured proper data types (e.g., `CRIMINAL CASES` to int64, `WINNER` to int).

### 2. Exploratory Data Analysis (EDA)

- **Tools**: Plotly (interactive visualizations), Matplotlib (geospatial plots).
- **Analyses**:
  - State-wise constituency distribution (choropleth map, sunburst chart).
  - Party win counts and win-loss ratios (bar and stacked bar charts).
  - Gender ratios and educational qualifications (bar and pie charts).
  - Criminal cases by party (Sankey diagram).

### 3. Predictive Modeling

- **Features**: `PARTY`, `EDUCATION`, `GENDER`, `CATEGORY`, `CRIMINAL CASES`, `AGE`, `TOTAL VOTES`, `TOTAL ELECTORS`, `ASSETS`, `LIABILITIES`.
- **Model**: RandomForestClassifier in a Pipeline with StandardScaler (numerical features) and OneHotEncoder (categorical features).
- **Evaluation**: 90.51% accuracy, detailed classification report, and confusion matrix.
- **Deployment**: Saved model as `rf_politician_model_pipeline.pkl`.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lokesha01hp/Lok_Sabha_2019_EDA_and_Prediction.git
   cd Lok_Sabha_2019_EDA_and_Prediction
   ```

### 1. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Download & Place Datasets

Place LS_2.0.csv in:

```bash
datasets/Indian Candidates for General Election 2019/
Place Indian_States.shp (and related .shx, .dbf, etc.) in datasets/India states/Igismap/:
```

### Run the Jupyter Notebook

```bash
jupyter notebook main.ipynb
```

---

### Inside the notebook:

Perform EDA on candidate demographics, votes, and electoral patterns.

Generate visualizations:

-Choropleth Map

-Sunburst Chart

-Bar & Pie Charts

-Sankey Diagram

-Confusion Matrix

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Datasets by:
--Prakrut Chauhan
--Somacodes (Kaggle)
