import pandas as pd


class Analyzer:

    def analyze_dataset(self, df):

        analysis = {}

        analysis["Rows"] = df.shape[0]
        analysis["Columns"] = df.shape[1]

        analysis["Missing Values"] = int(df.isnull().sum().sum())

        analysis["Duplicate Rows"] = int(df.duplicated().sum())

        analysis["Column Names"] = list(df.columns)

        analysis["Numeric Columns"] = list(
            df.select_dtypes(include="number").columns
        )

        analysis["Categorical Columns"] = list(
            df.select_dtypes(exclude="number").columns
        )

        return analysis

    def missing_value_report(self, df):

        report = (
            df.isnull()
            .sum()
            .sort_values(ascending=False)
        )

        return report

    def duplicate_report(self, df):

        return int(df.duplicated().sum())

    def numeric_summary(self, df):

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return None

        return numeric.describe()

    def categorical_summary(self, df):

        result = {}

        categorical = df.select_dtypes(exclude="number")

        for col in categorical.columns:

            result[col] = (
                categorical[col]
                .value_counts()
                .head(10)
            )

        return result

    def correlation_matrix(self, df):

        numeric = df.select_dtypes(include="number")

        if numeric.shape[1] < 2:
            return None

        return numeric.corr()

    def top_numeric_columns(self, df):

        numeric = df.select_dtypes(include="number")

        return list(numeric.columns)

    def top_categorical_columns(self, df):

        categorical = df.select_dtypes(exclude="number")

        return list(categorical.columns)

    def executive_summary(self, df):

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

        summary = f"""
Dataset Overview

• Total Rows : {rows}

• Total Columns : {cols}

• Numeric Columns : {numeric}

• Categorical Columns : {categorical}

• Missing Values : {missing}

• Duplicate Rows : {duplicate}
"""

        return summary

    def recommendations(self, df):

        recommendations = []

        if df.isnull().sum().sum() > 0:

            recommendations.append(
                "Fill missing values before analysis."
            )

        if df.duplicated().sum() > 0:

            recommendations.append(
                "Remove duplicate records."
            )

        if len(df.select_dtypes(include="number").columns) == 0:

            recommendations.append(
                "Dataset has no numeric columns for statistical analysis."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Dataset quality looks good."
            )

        return recommendations