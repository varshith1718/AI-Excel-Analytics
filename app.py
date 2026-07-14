import streamlit as st
import tempfile
import os

from src.data_loader import DataLoader
from src.analyzer import Analyzer
from src.chart_generator import ChartGenerator
from src.ai_summary import AISummary
from src.report_generator import ReportGenerator
from src.ppt_generator import PPTGenerator


st.set_page_config(
    page_title="AI Excel Analytics & Report Generator",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Excel Analytics & Report Generator")

st.write(
    "Upload any Excel (.xlsx) file to automatically generate analytics, charts, AI insights, reports and PowerPoint."
)

uploaded_file = st.file_uploader(
    "Choose Excel File",
    type=["xlsx"]
)

if uploaded_file is not None:

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".xlsx"
    )

    temp.write(uploaded_file.read())

    temp.close()

    loader = DataLoader(temp.name)

    sheets = loader.load_all_sheets()

    sheet_names = list(sheets.keys())

    sheet = st.selectbox(
        "Select Sheet",
        sheet_names
    )

    df = sheets[sheet]

    st.success("Excel uploaded successfully.")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    if st.button("Generate AI Report"):

        analyzer = Analyzer()

        dataset_info = analyzer.analyze_dataset(df)

        summary = AISummary()

        insights = summary.generate_summary(df)

        risks = summary.risk_analysis(df)

        recommendations = summary.recommendations(df)

        score = summary.overall_score(df)

        chart = ChartGenerator()

        charts = chart.generate_all(df)

        report = ReportGenerator()

        report_file = report.generate_report(
            dataset_info,
            summary.executive_summary(df),
            risks,
            recommendations,
            score
        )

        ppt = PPTGenerator()

        ppt_file = ppt.generate_presentation(
            dataset_info,
            charts,
            insights,
            risks,
            recommendations,
            score
        )

        st.success("Analysis Completed Successfully")

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows",
            dataset_info["Rows"]
        )

        col2.metric(
            "Columns",
            dataset_info["Columns"]
        )

        col3.metric(
            "Score",
            f"{score}/100"
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Missing Values",
            dataset_info["Missing Values"]
        )

        col2.metric(
            "Duplicate Rows",
            dataset_info["Duplicate Rows"]
        )

        st.subheader("AI Insights")

        for item in insights:

            st.write("✅", item)

        st.subheader("Risk Analysis")

        for risk in risks:

            st.warning(risk)

        st.subheader("Recommendations")

        for rec in recommendations:

            st.success(rec)

        st.subheader("Charts")

        if charts["Bar"]:

            st.image(charts["Bar"])

        if charts["Histogram"]:

            st.image(charts["Histogram"])

        if charts["Pie"]:

            st.image(charts["Pie"])

        if charts["Line"]:

            st.image(charts["Line"])


        st.download_button(
            "📄 Download Report",
            open(report_file, "rb"),
            file_name="Excel_Analytics_Report.txt"
        )

        st.download_button(
            "📊 Download Presentation",
            open(ppt_file, "rb"),
            file_name="Excel_Analytics_Report.pptx"
        )

    os.unlink(temp.name)