import pandas as pd

from services.graph_generator import (
    generate_heatmap,
    generate_histogram,
    generate_bar_chart,
    generate_pie_chart,
    generate_line_chart
)

from flask import Flask, render_template, request, send_file
import os

from services.upload import save_uploaded_file
from services.cleaning import clean_data
from services.analysis import perform_eda
from services.excel_export import export_to_excel
from services.filter_data import filter_dataset

app = Flask(__name__)
latest_cleaned_file = None


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global latest_cleaned_file

    # Uploaded file
    file = request.files['dataset']

    # Save Raw Dataset
    raw_file = save_uploaded_file(file)

    # Clean Dataset
    cleaned_file = clean_data(raw_file)
    latest_cleaned_file = cleaned_file

    # Perform EDA
    report = perform_eda(cleaned_file)

    # Calculate Missing Values
    total_missing = sum(
        report["Missing Values"].values()
    )

    # Data Quality Score
    quality_score = 100

    if total_missing > 0:
        quality_score -= 10

    return render_template(
        "dashboard.html",
        report=report,
        total_missing=total_missing,
        quality_score=quality_score
    )

#  for graph generator

@app.route('/generate-graph', methods=['POST'])
def generate_graph():

    global latest_cleaned_file

    if latest_cleaned_file is None:
        return "Please upload a dataset first."

    graph_type = request.form['graph_type']

    df = pd.read_csv(latest_cleaned_file)

    graph_path = None

    if graph_type == "heatmap":
        graph_path = generate_heatmap(df)

    elif graph_type == "histogram":
        graph_path = generate_histogram(df)

    elif graph_type == "bar":
        graph_path = generate_bar_chart(df)

    elif graph_type == "pie":
        graph_path = generate_pie_chart(df)

    elif graph_type == "line":
        graph_path = generate_line_chart(df)

    report = perform_eda(latest_cleaned_file)

    total_missing = sum(
        report["Missing Values"].values()
    )

    quality_score = 100

    if total_missing > 0:
        quality_score -= 10

    report["Selected Graph"] = graph_path

    return render_template(
        "dashboard.html",
        report=report,
        total_missing=total_missing,
        quality_score=quality_score
    )

 # Search data filter 
@app.route('/search-data', methods=['POST'])
def search_data():

    global latest_cleaned_file

    if latest_cleaned_file is None:
        return "Please upload dataset first."

    column_name = request.form['column_name']
    value = request.form['search_value']

    filtered_result = filter_dataset(
        latest_cleaned_file,
        column_name,
        value
    )

    report = perform_eda(
        latest_cleaned_file
    )

    total_missing = sum(
        report["Missing Values"].values()
    )

    quality_score = 100

    if total_missing > 0:
        quality_score -= 10

    report["Filtered Result"] = filtered_result

    return render_template(
        "dashboard.html",
        report=report,
        total_missing=total_missing,
        quality_score=quality_score
    )


# Download Latest Cleaned Dataset
@app.route('/download-cleaned')
def download_cleaned():

    cleaned_folder = "uploads/cleaned_data"

    files = os.listdir(cleaned_folder)

    if not files:
        return "No cleaned dataset found."

    latest_file = max(
        [os.path.join(cleaned_folder, f) for f in files],
        key=os.path.getctime
    )

    return send_file(
        latest_file,
        as_attachment=True
    )

@app.route('/download-excel')
def download_excel():

    cleaned_folder = "uploads/cleaned_data"

    files = os.listdir(cleaned_folder)

    if not files:
        return "No cleaned dataset found."

    latest_file = max(
        [os.path.join(cleaned_folder, f) for f in files],
        key=os.path.getctime
    )

    excel_file = export_to_excel(
        latest_file
    )

    return send_file(
        excel_file,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask, render_template, request, send_file

# from services.upload import save_uploaded_file
# from services.cleaning import clean_data
# from services.analysis import perform_eda

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():

#     # Uploaded file
#     file = request.files['dataset']

#     # Save Raw Dataset
#     raw_file = save_uploaded_file(file)

#     # Clean Dataset
#     cleaned_file = clean_data(raw_file)

#     # Perform EDA
#     report = perform_eda(cleaned_file)

#     # Calculate Missing Values
#     total_missing = sum(
#         report["Missing Values"].values()
#     )

#     # Data Quality Score
#     quality_score = 100

#     if total_missing > 0:
#         quality_score -= 10

#     return render_template(
#         "dashboard.html",
#         report=report,
#         total_missing=total_missing,
#         quality_score=quality_score
#     )

# # Download Cleaned Dataset
# @app.route('/download-cleaned')
# def download_cleaned():

#     return send_file(
#         'uploads/cleaned_data/cleaned_dataset.csv',
#         as_attachment=True
#     )

# if __name__ == '__main__':
#     app.run(debug=True)