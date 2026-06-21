import os
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns


def generate_heatmap(df):

    graph_folder = "static/graphs"
    os.makedirs(graph_folder, exist_ok=True)

    numeric_df = df.select_dtypes(include=['number'])

    if len(numeric_df.columns) < 2:
        return None

    plt.figure(figsize=(6, 4))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    path = os.path.join(
        graph_folder,
        "heatmap.png"
    )

    plt.savefig(path, bbox_inches="tight")
    plt.close()

    return "graphs/heatmap.png"


def generate_histogram(df):

    graph_folder = "static/graphs"
    os.makedirs(graph_folder, exist_ok=True)

    numeric_cols = df.select_dtypes(
        include=['number']
    ).columns

    if len(numeric_cols) == 0:
        return None

    column = numeric_cols[0]

    plt.figure(figsize=(6, 4))

    plt.hist(df[column], bins=20)

    plt.title(f"Histogram - {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    path = os.path.join(
        graph_folder,
        "histogram.png"
    )

    plt.savefig(path, bbox_inches="tight")
    plt.close()

    return "graphs/histogram.png"


def generate_bar_chart(df):

    graph_folder = "static/graphs"
    os.makedirs(graph_folder, exist_ok=True)

    cat_cols = df.select_dtypes(
        include=['object']
    ).columns

    if len(cat_cols) == 0:
        return None

    column = cat_cols[0]

    plt.figure(figsize=(6, 4))

    df[column].value_counts().head(10).plot(
        kind='bar'
    )

    plt.title(f"Bar Chart - {column}")
    plt.xlabel(column)
    plt.ylabel("Count")

    path = os.path.join(
        graph_folder,
        "bar_chart.png"
    )

    plt.savefig(path, bbox_inches="tight")
    plt.close()

    return "graphs/bar_chart.png"


def generate_pie_chart(df):

    graph_folder = "static/graphs"
    os.makedirs(graph_folder, exist_ok=True)

    cat_cols = df.select_dtypes(
        include=['object']
    ).columns

    if len(cat_cols) == 0:
        return None

    column = cat_cols[0]

    plt.figure(figsize=(4, 4))

    df[column].value_counts().head(5).plot(
        kind='pie',
        autopct='%1.1f%%'
    )

    plt.ylabel("")
    plt.title(f"Pie Chart - {column}")

    path = os.path.join(
        graph_folder,
        "pie_chart.png"
    )

    plt.savefig(path, bbox_inches="tight")
    plt.close()

    return "graphs/pie_chart.png"


def generate_line_chart(df):

    graph_folder = "static/graphs"
    os.makedirs(graph_folder, exist_ok=True)

    numeric_cols = df.select_dtypes(
        include=['number']
    ).columns

    if len(numeric_cols) < 2:
        return None

    x_col = numeric_cols[0]
    y_col = numeric_cols[1]

    plt.figure(figsize=(6, 3))

    plt.plot(
        df[x_col],
        df[y_col],
        marker='o'
    )

    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.title(
        f"Line Chart: {y_col} vs {x_col}"
    )

    path = os.path.join(
        graph_folder,
        "line_chart.png"
    )

    plt.savefig(
        path,
        bbox_inches="tight"
    )

    plt.close()

    return "graphs/line_chart.png"