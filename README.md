# AI-Powered Online Class Quality Checker

An automated, multimodal AI application designed to evaluate online class recordings for children. Built for the **Humaniti AI - Build Challenge 2**, this system processes video and audio signals across **Verbal & Pedagogy**, **Audio Dynamics**, and **Visual Engagement** to provide structured, objective quality classifications along with specific, timestamped observational feedback.

---

##  Key Features

* **Multimodal Evaluation Engine:** Leverages Gemini 3.5 Flash to simultaneously analyze video streams, teacher speech, slide movements, and non-verbal interactions without complex multi-step transcription setups.
* **Acoustic Signal Analytics:** Uses `librosa` and `moviepy` to extract objective audio metrics, including silence ratios (dead air/pauses > 2.5s) and vocal energy variability (RMS standard deviation for enthusiasm vs. monotony).
* **Structured Assessment Output:** Generates overall quality tiers (`Poor`, `Average`, `Good`, `Excellent`), numerical sub-scores (0–10) across key pedagogical dimensions, and timestamped actionable observations.
* **Interactive Web Interface:** Single-page Streamlit dashboard featuring video upload/preview, sub-score bar charts, executive badges, and timestamped feedback logs.

---

##  Tech Stack

* **Framework & UI:** Streamlit, Python 3.10+
* **Multimodal LLM Engine:** Google Gemini 2.5 Flash API (`google-genai` SDK)
* **Audio & Signal Processing:** `librosa`, `soundfile`, `moviepy`
* **Data Visualization:** Plotly Express, Pandas

---

##  Repository Structure

```text
├── app.py                          # Streamlit web application & UI layout
├── evaluator.py                    # Gemini Multimodal API integration & JSON payload handler
├── audio_processor.py              # Acoustic dynamics extractor (librosa + moviepy)
├── requirements.txt                # Python dependencies
├── .env                            # Sample environment file template
└── README.md                       # Project documentation