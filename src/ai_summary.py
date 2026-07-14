import pandas as pd


class AISummary:

    def generate_summary(self, df):

        rows = df.shape[0]
        cols = df.shape[1]

        missing = int(df.isnull().sum().sum())
        duplicate = int(df.duplicated().sum())

        numeric = len(
            df.select_dtypes(include="number").columns
        )

        categorical = len(
            df.select_dtypes(exclude="number").columns
        )

        insights = []

        insights.append(
            f"The dataset contains {rows} records."
        )

        insights.append(
            f"A total of {cols} columns were detected."
        )

        insights.append(
            f"There are {numeric} numeric columns."
        )

        insights.append(
            f"There are {categorical} categorical columns."
        )

        if missing == 0:
            insights.append(
                "No missing values were detected."
            )
        else:
            insights.append(
                f"{missing} missing values were found."
            )

        if duplicate == 0:
            insights.append(
                "No duplicate records were detected."
            )
        else:
            insights.append(
                f"{duplicate} duplicate records were detected."
            )

        return insights

    def risk_analysis(self, df):

        risk = []

        missing = int(df.isnull().sum().sum())

        duplicate = int(df.duplicated().sum())

        if missing > 0:

            risk.append(
                "Dataset contains missing values."
            )

        if duplicate > 0:

            risk.append(
                "Duplicate records exist."
            )

        numeric = len(
            df.select_dtypes(include="number").columns
        )

        if numeric == 0:

            risk.append(
                "No numeric columns available."
            )

        if len(risk) == 0:

            risk.append(
                "No major risks detected."
            )

        return risk

    def recommendations(self, df):

        recommendations = []

        missing = int(df.isnull().sum().sum())

        duplicate = int(df.duplicated().sum())

        if missing > 0:

            recommendations.append(
                "Fill missing values before performing analysis."
            )

        if duplicate > 0:

            recommendations.append(
                "Remove duplicate rows."
            )

        numeric = len(
            df.select_dtypes(include="number").columns
        )

        if numeric == 0:

            recommendations.append(
                "Include numeric columns for better analytics."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Dataset quality is good."
            )

        return recommendations

    def executive_summary(self, df):

        rows = df.shape[0]

        cols = df.shape[1]

        missing = int(df.isnull().sum().sum())

        duplicate = int(df.duplicated().sum())

        summary = f"""

EXECUTIVE SUMMARY

Dataset Size

• Rows : {rows}

• Columns : {cols}

Data Quality

• Missing Values : {missing}

• Duplicate Rows : {duplicate}

Overall Assessment

The uploaded Excel file has been analyzed successfully.
The dataset quality has been evaluated based on
missing values, duplicate records and available columns.
"""

        return summary

    def overall_score(self, df):

        score = 100

        score -= int(df.isnull().sum().sum()) * 0.5

        score -= int(df.duplicated().sum()) * 2

        if score < 0:
            score = 0

        return round(score, 2)