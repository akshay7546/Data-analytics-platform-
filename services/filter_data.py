import pandas as pd

def filter_dataset(file_path, column_name, value):

    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)

    else:
        df = pd.read_excel(file_path)

    if column_name not in df.columns:
        return None

    filtered_df = df[
        df[column_name]
        .astype(str)
        .str.contains(
            str(value),
            case=False,
            na=False
        )
    ]

    return {
        "columns": list(filtered_df.columns),
        "data": filtered_df.head(50).fillna("").to_dict(
            orient="records"
        )
    }