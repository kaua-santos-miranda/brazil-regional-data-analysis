import os
from datetime import datetime


def generate_report(results: dict, output_path: str) -> None:
    """
    Generates a .txt report with the analysis results.

    :param results: Dictionary containing statistics per column
    :param output_path: Path where the report will be saved
    """

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_path, mode="w", encoding="utf-8") as file:
        file.write("Excel Data Analysis Report\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated at: {timestamp}\n")

        for column, stats in results.items():
            file.write("\n")
            file.write(f"Column: {column}\n")
            file.write("-" * 40 + "\n")

            for key, value in stats.items():
                file.write(f"{key.capitalize():<10}: {value:.2f}\n")
