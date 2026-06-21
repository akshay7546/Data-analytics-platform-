# Data Analytics Platform

## Overview

Data Analytics Platform is a web-based application built using Flask and Python that allows users to upload datasets, perform data cleaning, generate visualizations, preview data, filter records, and download processed datasets.

The platform helps users quickly analyze CSV and Excel files without writing code.

---

## Features

### Dataset Upload

* Upload CSV and Excel datasets
* Automatic file handling and storage

### Data Cleaning

* Handle missing values
* Remove unnecessary data issues
* Generate cleaned datasets

### Exploratory Data Analysis (EDA)

* Total rows and columns
* Data types information
* Missing value analysis
* Dataset insights

### Data Visualization

* Heatmap
* Histogram
* Bar Chart
* Pie Chart
* Line Chart

### Dataset Preview

* View first 10 rows of dataset
* Quick inspection of uploaded data

### Search & Filter

* Search records by column name
* Filter data dynamically

### Download Options

* Download cleaned CSV file
* Download Excel file

---

## Tech Stack

### Backend

* Python
* Flask

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Frontend

* HTML
* CSS

### Version Control

* Git
* GitHub

---

## Project Structure

data_analytics_platform/

├── app.py

├── services/

│   ├── analysis.py

│   ├── cleaning.py

│   ├── graph_generator.py

│   ├── upload.py

│   ├── filter_data.py

│   └── excel_export.py

├── templates/

│   ├── index.html

│   └── dashboard.html

├── static/

│   ├── css/

│   └── graphs/

├── uploads/

├── exports/

├── database/

└── requirements.txt

---

## Installation

### Clone Repository

```bash
git clone https://github.com/akshay7546/Data-analytics-platform-.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Future Enhancements

* User Authentication
* SQLite Database Integration
* PDF Analytics Reports
* AI-Based Insights
* Dashboard Export
* Cloud Deployment

---

## Author

Akshay Kumar

B.Tech Data Science

CGC University

GitHub: https://github.com/akshay7546
