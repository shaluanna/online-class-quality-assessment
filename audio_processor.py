# audio_processor.py
import os
import tempfile
import librosa
import numpy as np
from moviepy.editor import VideoFileClip

def analyze_audio_dynamics(video_path):
    """
    Extracts audio from video clip, converts to temporary WAV, 
    and computes acoustic dynamics.
    """
    temp_wav = None
    try:
        # 1. Extract audio from .mp4 to a temporary .wav file
        video_clip = VideoFileClip(video_path)
        temp_wav = os.path.join(tempfile.gettempdir(), "temp_extracted_audio.wav")
        video_clip.audio.write_audiofile(temp_wav, logger=None)
        video_clip.close()

        # 2. Load the extracted .wav file with librosa
        y, sr = librosa.load(temp_wav, sr=None)

        # 3. Compute RMS Energy (Vocal Variation)
        rms = librosa.feature.rms(y=y)[0]
        energy_std = np.std(rms)
        energy_mean = np.mean(rms)

        # 4. Compute Silence / Dead-Air Ratio (pauses > 2.5s)
        non_silent_intervals = librosa.effects.split(y, top_db=30)
        total_non_silent = sum([(end - start) for start, end in non_silent_intervals]) / sr
        total_duration = len(y) / sr
        silence_ratio = max(0.0, 1.0 - (total_non_silent / total_duration))

        return {
            "duration_seconds": round(total_duration, 2),
            "silence_ratio": round(silence_ratio, 4),
            "energy_variability": round(float(energy_std), 4),
            "mean_energy": round(float(energy_mean), 4)
        }

    finally:
        # Clean up temporary extracted WAV file
        if temp_wav and os.path.exists(temp_wav):
            try:
                os.remove(temp_wav)
            except Exception:
                pass