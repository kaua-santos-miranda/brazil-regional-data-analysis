from loader import load_excel
from analyzer import analyze
from report import generate_report


def print_results(results: dict) -> None:
    print("\n📊 Excel Data Analysis")
    print("=" * 40)

    for column, stats in results.items():
        print(f"\nColumn: {column}")
        print("-" * 40)

        for key, value in stats.items():
            print(f"{key.capitalize():<10}: {value:.2f}")


def main():
    file_path = "data/sample.xlsx"
    report_path = "reports/excel_analysis_report.txt"

    try:
        df = load_excel(file_path)
        results = analyze(df)

        print_results(results)
        generate_report(results, report_path)

        print(f"\n📄 Report generated at: {report_path}")

    except Exception as error:
        print(f"❌ Error: {error}")


if __name__ == "__main__":
    main()
