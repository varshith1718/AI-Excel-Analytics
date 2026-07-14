import os
from datetime import datetime


class ReportGenerator:

    def __init__(self):

        self.output_folder = "output"

        os.makedirs(self.output_folder, exist_ok=True)

    def generate_report(
        self,
        dataset_info,
        ai_summary,
        risks,
        recommendations,
        score
    ):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = os.path.join(
            self.output_folder,
            f"Excel_Analytics_Report_{timestamp}.txt"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("=" * 70 + "\n")
            file.write("AI EXCEL ANALYTICS REPORT\n")
            file.write("=" * 70 + "\n\n")

            file.write("GENERATED ON\n")
            file.write("-" * 70 + "\n")
            file.write(
                datetime.now().strftime(
                    "%d %B %Y %I:%M %p"
                )
            )

            file.write("\n\n")

            file.write("DATASET INFORMATION\n")
            file.write("-" * 70 + "\n")

            for key, value in dataset_info.items():

                file.write(
                    f"{key:<25}: {value}\n"
                )

            file.write("\n")

            file.write("EXECUTIVE SUMMARY\n")
            file.write("-" * 70 + "\n")

            file.write(ai_summary)

            file.write("\n\n")

            file.write("RISK ANALYSIS\n")
            file.write("-" * 70 + "\n")

            for risk in risks:

                file.write(
                    f"• {risk}\n"
                )

            file.write("\n")

            file.write("RECOMMENDATIONS\n")
            file.write("-" * 70 + "\n")

            for rec in recommendations:

                file.write(
                    f"✓ {rec}\n"
                )

            file.write("\n")

            file.write("OVERALL DATASET SCORE\n")
            file.write("-" * 70 + "\n")

            file.write(
                f"{score}/100\n"
            )

            file.write("\n")

            file.write("=" * 70 + "\n")
            file.write("END OF REPORT\n")
            file.write("=" * 70 + "\n")

        return filename