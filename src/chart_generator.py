import os
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self):

        self.output_folder = "output"
        os.makedirs(self.output_folder, exist_ok=True)

    def bar_chart(self, df):

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return None

        means = numeric.mean().sort_values(ascending=False).head(10)

        plt.figure(figsize=(10, 5))

        plt.bar(
            means.index.astype(str),
            means.values,
            color="royalblue"
        )

        plt.title("Average Value by Numeric Column")

        plt.xticks(rotation=45)

        plt.tight_layout()

        path = os.path.join(
            self.output_folder,
            "bar_chart.png"
        )

        plt.savefig(path)

        plt.close()

        return path

    def histogram(self, df):

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return None

        column = numeric.columns[0]

        plt.figure(figsize=(8, 5))

        plt.hist(
            numeric[column],
            bins=20,
            color="green",
            edgecolor="black"
        )

        plt.title(f"Histogram - {column}")

        plt.tight_layout()

        path = os.path.join(
            self.output_folder,
            "histogram.png"
        )

        plt.savefig(path)

        plt.close()

        return path

    def pie_chart(self, df):

        categorical = df.select_dtypes(exclude="number")

        if categorical.empty:
            return None

        column = categorical.columns[0]

        values = (
            categorical[column]
            .value_counts()
            .head(8)
        )

        plt.figure(figsize=(7, 7))

        plt.pie(
            values.values,
            labels=values.index.astype(str),
            autopct="%1.1f%%"
        )

        plt.title(column)

        path = os.path.join(
            self.output_folder,
            "pie_chart.png"
        )

        plt.savefig(path)

        plt.close()

        return path

    def line_chart(self, df):

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return None

        column = numeric.columns[0]

        plt.figure(figsize=(10, 5))

        plt.plot(
            numeric[column].values,
            linewidth=2
        )

        plt.title(column)

        plt.grid(True)

        plt.tight_layout()

        path = os.path.join(
            self.output_folder,
            "line_chart.png"
        )

        plt.savefig(path)

        plt.close()

        return path

    def box_plot(self, df):

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return None

        plt.figure(figsize=(10, 5))

        numeric.boxplot()

        plt.xticks(rotation=45)

        plt.tight_layout()

        path = os.path.join(
            self.output_folder,
            "box_plot.png"
        )

        plt.savefig(path)

        plt.close()

        return path

    def generate_all(self, df):

        charts = {}

        charts["Bar"] = self.bar_chart(df)

        charts["Histogram"] = self.histogram(df)

        charts["Pie"] = self.pie_chart(df)

        charts["Line"] = self.line_chart(df)

        charts["Box"] = self.box_plot(df)

        return charts