import pandas as pd
import os

def export_to_excel(csv_file_path):

    df = pd.read_csv(csv_file_path)

    export_folder = "exports/excel"
    os.makedirs(export_folder, exist_ok=True)

    excel_file_path = os.path.join(
        export_folder,
        "cleaned_dataset.xlsx"
    )

    df.to_excel(
        excel_file_path,
        index=False
    )

    return excel_file_path