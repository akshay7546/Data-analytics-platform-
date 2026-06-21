import pandas as pd
import os

def clean_data(file_path):

    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)

    else:
        df = pd.read_excel(file_path)

    # Remove Duplicates
    df.drop_duplicates(inplace=True)

    # Fill Missing Values
    for col in df.columns:

        if df[col].dtype == 'object':

            if not df[col].mode().empty:
                df[col] = df[col].fillna(df[col].mode()[0])

        else:

            df[col] = df[col].fillna(df[col].mean())

    cleaned_folder = "uploads/cleaned_data"

    if not os.path.exists(cleaned_folder):
        os.makedirs(cleaned_folder)

    # Same filename as uploaded file
    filename = os.path.basename(file_path)

    cleaned_path = os.path.join(
        cleaned_folder,
        f"cleaned_{filename}"
    )

    df.to_csv(cleaned_path, index=False)

    return cleaned_path




# import pandas as pd
# import os

# def clean_data(file_path):

#     if file_path.endswith('.csv'):
#         df = pd.read_csv(file_path)

#     else:
#         df = pd.read_excel(file_path)

#     # Remove Duplicates
#     df.drop_duplicates(inplace=True)

#     # Fill Missing Values
#     for col in df.columns:

#         if df[col].dtype == 'object':

#             if not df[col].mode().empty:
#                 df[col] = df[col].fillna(df[col].mode()[0])

#         else:

#             df[col] = df[col].fillna(df[col].mean())

#     cleaned_folder = "uploads/cleaned_data"

#     if not os.path.exists(cleaned_folder):
#         os.makedirs(cleaned_folder)

#     cleaned_path = os.path.join(
#         cleaned_folder,
#         "cleaned_dataset.csv"
#     )

#     df.to_csv(cleaned_path, index=False)

#     return cleaned_path