# Data Analytics Platform

## Overview
A Flask-based Data Analytics Platform for uploading, cleaning, analyzing, and visualizing datasets.

## Features
- Dataset Upload
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Dataset Preview
- Graph Generation
  - Heatmap
  - Histogram
  - Bar Chart
  - Pie Chart
  - Line Chart
- Search & Filter Data
- Download Cleaned Dataset (CSV)
- Download Dataset (Excel)

## Tech Stack
- Python
- Flask
- Pandas
- Matplotlib
- Seaborn
- HTML
- CSS

## Project Structure

```text
data_analytics_platform/
│
├── app.py
├── requirements.txt
│
├── services/
│   ├── analysis.py
│   ├── cleaning.py
│   ├── upload.py
│   ├── graph_generator.py
│   ├── filter_data.py
│   └── excel_export.py
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   └── graphs/
│
└── uploads/
```

## Installation

```bash
git clone <repository-url>
cd data_analytics_platform

pip install -r requirements.txt

python app.py
```

## Future Improvements

- SQLite Database Integration
- User Authentication
- PDF Report Generation
- AI-Powered Insights
- Dashboard Analytics

## Author

Akshay Kumar
B.Tech Data Science
CGC University