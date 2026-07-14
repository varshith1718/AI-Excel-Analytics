import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from src.data_loader import DataLoader
from src.analyzer import Analyzer
from src.chart_generator import ChartGenerator
from src.ai_summary import AISummary
from src.report_generator import ReportGenerator
from src.ppt_generator import PPTGenerator


def main():

    print("=" * 70)
    print("AI EXCEL ANALYTICS & REPORT GENERATOR")
    print("=" * 70)

    # Hide tkinter window
    Tk().withdraw()

    # Select any Excel file
    file_path = askopenfilename(
        title="Select Excel File",
        filetypes=[
            ("Excel Files", "*.xlsx *.xls")
        ]
    )

    if not file_path:
        print("No file selected.")
        return

    # Load workbook
    loader = DataLoader(file_path)

    sheets = loader.load_all_sheets()

    sheet_names = list(sheets.keys())

    print("\nAvailable Sheets\n")

    for i, sheet in enumerate(sheet_names, start=1):
        print(f"{i}. {sheet}")

    try:
        choice = int(input("\nSelect Sheet Number : "))
        sheet_name = sheet_names[choice - 1]
    except Exception:
        print("Invalid selection.")
        return

    df = sheets[sheet_name]

    print("\nAnalyzing dataset...\n")

    # Dataset Analysis
    analyzer = Analyzer()

    dataset_info = analyzer.analyze_dataset(df)

    # AI Summary
    ai = AISummary()

    insights = ai.generate_summary(df)

    risks = ai.risk_analysis(df)

    recommendations = ai.recommendations(df)

    score = ai.overall_score(df)

    # Charts
    chart_generator = ChartGenerator()

    chart_files = chart_generator.generate_all(df)

    # Report
    report_generator = ReportGenerator()

    report_file = report_generator.generate_report(
        dataset_info,
        ai.executive_summary(df),
        risks,
        recommendations,
        score
    )

    # PowerPoint
    ppt_generator = PPTGenerator()

    ppt_file = ppt_generator.generate_presentation(
        dataset_info,
        chart_files,
        insights,
        risks,
        recommendations,
        score
    )

    # Delete temporary chart images
    for image in chart_files.values():

        if image and os.path.exists(image):

            os.remove(image)

    print("=" * 70)
    print("DATASET INFORMATION")
    print("=" * 70)

    for key, value in dataset_info.items():
        print(f"{key:25}: {value}")

    print("\nAI INSIGHTS")
    print("-" * 70)

    for item in insights:
        print("•", item)

    print("\nRISKS")
    print("-" * 70)

    for risk in risks:
        print("⚠", risk)

    print("\nRECOMMENDATIONS")
    print("-" * 70)

    for rec in recommendations:
        print("✓", rec)

    print("\nDataset Score :", score)

    print("\nReport Saved :", report_file)

    print("Presentation Saved :", ppt_file)

    print("\n" + "=" * 70)
    print("PROCESS COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()