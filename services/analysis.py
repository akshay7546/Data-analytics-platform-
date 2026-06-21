import matplotlib
matplotlib.use('Agg')

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


def perform_eda(file_path):

    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)

    else:
        df = pd.read_excel(file_path)

    # Create graph folder
    graph_folder = "static/graphs"
    os.makedirs(graph_folder, exist_ok=True)

    # Select numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    # Generate Default Heatmap
    if len(numeric_df.columns) > 1:

        plt.figure(figsize=(10, 6))
        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="coolwarm"
        )
        plt.title("Correlation Heatmap")
        heatmap_path = os.path.join(
            graph_folder,
            "heatmap.png"
        )
        plt.savefig(
            heatmap_path,
            bbox_inches="tight"
        )
        plt.close()

        report = {

    "Rows": df.shape[0],

    "Columns": df.shape[1],

    "Column Names": list(df.columns),

    "Missing Values":
        df.isnull().sum().to_dict(),

    "Data Types":
        df.dtypes.astype(str).to_dict(),

    "Duplicate Rows":
        int(df.duplicated().sum()),

    "Total Missing":
        int(df.isnull().sum().sum()),

    "Heatmap":
        "graphs/heatmap.png",

    "Preview Columns":
        list(df.columns),

    "Preview Data":
        df.head(10).fillna("").to_dict(
            orient="records"
        ),

    # this is for Auto Insights
    "Numeric Columns":
        len(
            df.select_dtypes(
                include=['number']
            ).columns
        ),
    "Categorical Columns":
        len(
            df.select_dtypes(
                include=['object']
            ).columns
        ),
    "Total Missing":
        int(
            df.isnull().sum().sum()
        ),
    "Most Missing Column":
        df.isnull().sum().idxmax(),
    "Recommended Graph":
        "Heatmap"
        if len(
            df.select_dtypes(
                include=['number']
            ).columns
        ) > 1
        else "Bar Chart"
}
        return report


    # report = {

    #     "Rows": df.shape[0],

    #     "Columns": df.shape[1],

    #     "Column Names": list(df.columns),

    #     "Missing Values":
    #         df.isnull().sum().to_dict(),

    #     "Data Types":
    #         df.dtypes.astype(str).to_dict(),

    #     "Heatmap":
    #         "graphs/heatmap.png",

    #     # Dataset Preview
    #     "Preview Columns":
    #         list(df.columns),

    #     "Preview Data":
    #         df.head(10).fillna("").to_dict(
    #             orient="records"
    #         )
    # }
    # return report



