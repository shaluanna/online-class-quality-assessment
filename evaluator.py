# evaluator.py
import json
import os
import time
from google import genai
from google.genai import types
from audio_processor import analyze_audio_dynamics

import os
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

def evaluate_class_recording(video_path):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is missing or empty. Please check your .env file.")
        
    client = genai.Client(api_key=api_key)
    
    # Extract signal metrics
    audio_stats = analyze_audio_dynamics(video_path)
    
    # Upload video to Gemini Files API
    video_file = client.files.upload(file=video_path)
    
    # Wait for file processing if needed
    while video_file.state.name == "PROCESSING":
        time.sleep(2)
        video_file = client.files.get(name=video_file.name)

    prompt = f"""
    You are an expert pedagogical evaluator for 8x8 online classes for children.
    Evaluate this class recording along with these computed signal features:
    - Total Duration: {audio_stats['duration_seconds']}s
    - Silence/Pause Ratio: {audio_stats['silence_ratio']*100:.1f}%
    - Vocal Energy Variability: {audio_stats['energy_variability']}

    Analyze across 3 dimensions:
    1. Verbal & Pedagogy: Clarity, active student participation, encouragement, age-appropriate explanations.
    2. Audio Dynamics: Teacher enthusiasm, monotony, dead air/unexplained pauses.
    3. Visual Engagement: Screen shares, slide movement, teacher camera presence, visual aids.

    Return ONLY a JSON object matching this strict schema:
    {{
      "overall_quality": "Poor" | "Average" | "Good" | "Excellent",
      "overall_score": <number 0-100>,
      "category_scores": {{
         "pedagogy": <number 0-10>,
         "audio_enthusiasm": <number 0-10>,
         "visual_interactivity": <number 0-10>
      }},
      "summary_justification": "<2-3 sentence overview>",
      "key_observations": [
         {{"timestamp": "MM:SS", "type": "Positive" | "Needs Improvement", "observation": "<specific detail>"}}
      ]
    }}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[video_file, prompt],
        config=types.GenerateContentConfig(response_mime_type="application/json")
    )
    
    # Clean up file after evaluation
    client.files.delete(name=video_file.name)
    
    return json.loads(response.text)