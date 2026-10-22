# app.py
import sys
import asyncio

# Fix Windows ProactorEventLoop connection closed warning
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import streamlit as st
import tempfile
import os
import plotly.express as px
import pandas as pd
from evaluator import evaluate_class_recording

st.set_page_config(page_title="Online Class Quality Evaluator", layout="wide")

st.title("Online Class Quality Checker")
st.write("Upload a class recording to receive an automated multimodal quality assessment.")

uploaded_file = st.file_uploader("Choose a video file (.mp4, .mkv, .webm)", type=["mp4", "mkv", "webm"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.video(tmp_path)

    if st.button("🚀 Run Quality Assessment"):
        with st.spinner("Analyzing audio dynamics, visuals, and pedagogical engagement..."):
            results = evaluate_class_recording(tmp_path)
            
            # Top Level Metric Display
            col1, col2 = st.columns(2)
            quality = results["overall_quality"]
            score = results["overall_score"]
            
            color_map = {"Poor": "🔴", "Average": "🟡", "Good": "🔵", "Excellent": "🟢"}
            col1.metric("Classification", f"{color_map.get(quality, '⚪')} {quality}")
            col2.metric("Overall Score", f"{score}/100")
            
            st.subheader("Assessment Summary")
            st.write(results["summary_justification"])

            # Sub-score Radar/Bar Breakdown
            st.subheader("Category Breakdown")
            df = pd.DataFrame(list(results["category_scores"].items()), columns=["Category", "Score"])
            fig = px.bar(df, x="Category", y="Score", range_y=[0,10], color="Score", color_continuous_scale="Viridis")
            st.plotly_chart(fig, use_container_width=True)

            # Specific Timestamped Feedback
            st.subheader("Specific Observations")
            for obs in results["key_observations"]:
                icon = "✅" if obs["type"] == "Positive" else "⚠️"
                st.markdown(f"**[{obs['timestamp']}]** {icon} **{obs['type']}:** {obs['observation']}")

    # Cleanup temporary file
    os.remove(tmp_path)