import pandas as pd


class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_all_sheets(self):
        """
        Load all sheets from an Excel workbook.

        Returns:
            dict : {sheet_name: dataframe}
        """

        excel = pd.ExcelFile(self.file_path)

        sheets = {}

        for sheet in excel.sheet_names:
            sheets[sheet] = pd.read_excel(
                self.file_path,
                sheet_name=sheet
            )

        return sheets

    def get_sheet_names(self):
        """
        Return all sheet names.
        """

        excel = pd.ExcelFile(self.file_path)

        return excel.sheet_names

    def load_sheet(self, sheet_name):
        """
        Load a single sheet.
        """

        return pd.read_excel(
            self.file_path,
            sheet_name=sheet_name
        )

    def dataset_information(self, dataframe):
        """
        Basic dataset information.
        """

        info = {

            "Rows": dataframe.shape[0],

            "Columns": dataframe.shape[1],

            "Column Names": list(dataframe.columns),

            "Missing Values": int(
                dataframe.isnull().sum().sum()
            ),

            "Duplicate Rows": int(
                dataframe.duplicated().sum()
            ),

            "Numeric Columns": list(
                dataframe.select_dtypes(
                    include="number"
                ).columns
            ),

            "Categorical Columns": list(
                dataframe.select_dtypes(
                    exclude="number"
                ).columns
            )

        }

        return info

    def summary_statistics(self, dataframe):
        """
        Generate summary statistics.
        """

        try:
            return dataframe.describe(include="all")
        except Exception:
            return None