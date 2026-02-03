import pandas as pd


def analyze(df: pd.DataFrame) -> dict:
    """
    Analyzes numeric columns from a pandas DataFrame and returns
    basic descriptive statistics.

    :param df: pandas DataFrame loaded from an Excel file
    :return: Dictionary with statistics per numeric column
    """

    if df.empty:
        raise ValueError("No data available for analysis.")

    # Select only numeric columns
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        raise ValueError("No numeric columns found in the Excel file.")

    results = {}

    for column in numeric_df.columns:
        results[column] = {
            "min": numeric_df[column].min(),
            "max": numeric_df[column].max(),
            "mean": numeric_df[column].mean(),
            "median": numeric_df[column].median(),
            "std": numeric_df[column].std(),
        }

    return results
