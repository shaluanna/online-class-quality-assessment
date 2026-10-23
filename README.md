# AI-Powered Online Class Quality Checker

An AI-powered application developed for the **Humaniti AI – Build Challenge** to assess recorded online classes for children. It aims to evaluate teaching quality using speech content and audio dynamics, with an overall classification of **Poor, Average, Good, or Excellent**.

## Key Features

- **AI-Based Evaluation:** Uses the Google Gemini API to assess class recordings and generate structured feedback.
- **Audio Analytics:** Uses Librosa and MoviePy to process audio and calculate acoustic indicators, such as silence duration and vocal energy variation.
- **Quality Classification:** Produces an overall quality rating and, where implemented, category-wise scores and timestamped observations.
- **Interactive Dashboard:** Provides a Streamlit interface for uploading recordings and viewing assessment results and visualizations.

## Tech Stack

- **Framework:** Python 3.10+, Streamlit
- **AI Integration:** Google Gemini API (`google-genai`)
- **Audio Processing:** Librosa, SoundFile, MoviePy, FFmpeg
- **Visualization and Data:** Plotly Express, Pandas

## Repository Structure

```text
├── app.py                 # Streamlit application
├── evaluator.py           # Gemini API integration
├── audio_processor.py     # Audio extraction and analysis
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment configuration
└── README.md              # Project documentation
```

## Setup and Run

1. Clone the repository and navigate to its folder.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and configure your Gemini API key using the environment variable expected by the application. Never commit the actual API key.
5. Start the application:

   ```bash
   streamlit run app.py
   ```

6. Upload a supported class recording and review the assessment.

## Limitations

Results depend on recording quality, file size, API availability, and AI-generated judgments. Audio metrics are indicators, not definitive measures of teaching effectiveness. Visual engagement and student learning outcomes should not be claimed unless they are explicitly analyzed by the implementation. The generated ratings should support, not replace, human evaluation.
