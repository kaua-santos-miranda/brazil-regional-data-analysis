import pandas as pd


def load_excel(file_path: str) -> pd.DataFrame:
    """
    Loads an Excel (.xlsx) file and returns a pandas DataFrame.
    """

    try:
        df = pd.read_excel(file_path, engine="openpyxl")

        if df.empty:
            raise ValueError("The Excel file is empty.")

        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    except ValueError:
        raise

    except Exception as error:
        raise RuntimeError(f"Error reading the Excel file: {error}")
