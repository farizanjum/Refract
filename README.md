# Refract - AI Video Editor for Instagram Reels/Shorts

An advanced AI-powered video editing system that automatically transforms widescreen videos (podcasts, YouTube videos, interviews, etc.) into engaging vertical format content optimized for TikTok, Instagram Reels, and other social media platforms.

## What It Does

This system intelligently:
- **Analyzes speakers** and tracks who is speaking throughout the video
- **Detects faces** and matches them to speakers for smooth camera tracking
- **Creates smooth cuts** that follow the active speaker
- **Generates subtitles** automatically from speech
- **Produces Blender projects** with all edits pre-configured
- **Exports ready-to-use videos** with 9:16 aspect ratio

## Core Technologies

### Speaker Diarization
- **Resemblyzer**: Voice embedding and speaker identification
- **Agglomerative Clustering**: Groups similar voice segments
- **Audio Processing**: Extracts speaker segments with timestamps

### Face Recognition & Tracking
- **FaceNet**: Deep learning face embeddings for identity matching
- **MTCNN**: Multi-task Cascaded Convolutional Networks for face detection
- **Cosine Similarity**: Measures face similarity for speaker-face matching

### Video Processing
- **OpenCV**: Computer vision for frame analysis and cropping
- **FFmpeg**: Audio/video processing and format conversion
- **Shot Change Detection**: Structural Similarity Index (SSIM) for scene transitions

### Speech-to-Text & Subtitles
- **OpenAI Whisper**: State-of-the-art speech recognition
- **Sentence/Word-level Subtitling**: Flexible subtitle generation
- **Multi-language Support**: Including Indian languages via transliteration

## Quick Start

### 1. Installation

#### Option A: Using pip (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# For GPU support (optional but recommended)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Option B: Using Conda
```bash
# Create conda environment
conda env create -f environment.yml
conda activate ai-video-editor
```

### 2. Basic Usage

```bash
# Quick start using the launcher
python run.py --video-path your_video.mp4 --n-speakers 2 --add-subtitles

# Advanced usage with custom settings
python run.py \
  --video-path your_video.mp4 \
  --n-speakers 3 \
  --threshold 0.4 \
  --add-subtitles \
  --word-timestamps
```

### 3. Create Blender Project

1. Open Blender in Video Editing workspace
2. Load the `src/blender.py` script in the Text Editor
3. Run the script to import your processed video
4. Continue editing or export directly

## Command Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--video-path VIDEO_PATH` | str | **required** | Path to input video file |
| `--n-speakers` | int | 2 | Number of speakers in the video |
| `--threshold` | float | 0.4 | Face embedding similarity threshold |
| `--add-subtitles` | flag | - | Generate subtitle file |
| `--word-timestamps` | flag | - | Create word-level subtitles (vs sentence-level) |
| `--redo-faces` | flag | - | Re-match faces to speakers |
| `--edit` | flag | - | Edit video without Blender export |
| `--delete-cache` | flag | - | Clear cache and start fresh |

## 📂 Project Structure

```
refract/
├── src/                    # Python source code
│   ├── main.py            # Main application entry point
│   ├── editor.py          # Core video editing logic
│   ├── diarize.py         # Speaker diarization
│   ├── faces.py           # Face detection and recognition
│   ├── subtitles.py       # Subtitle generation and processing
│   ├── gui.py             # User interface for face matching
│   ├── framediff.py       # Shot change detection
│   └── blender.py         # Blender integration script
├── data/                   # Input files (videos, etc.)
├── output/                 # Generated output files
├── cache/                  # Temporary processing files
├── BL_proxy/              # Blender proxy files
├── requirements.txt       # Python dependencies
├── run.py                 # Application launcher
└── README.md             # This documentation
```

## Advanced Configuration

### GPU Acceleration
The system automatically detects and uses CUDA if available. For optimal performance:
- Install CUDA 11.8+ compatible PyTorch
- Ensure NVIDIA drivers are up to date
- Monitor GPU memory usage for long videos

### Speaker Diarization Tuning
- **n-speakers**: Start with an estimate, the system can handle variations
- **Audio Quality**: Better audio = better speaker separation
- **Background Noise**: Clean audio improves diarization accuracy

### Face Recognition Tuning
- **threshold**: Lower values (0.3-0.4) for stricter matching
- **Face Quality**: Clear, well-lit faces work best
- **Multiple Angles**: System handles face variations automatically

## Troubleshooting

### Common Issues

**Low GPU Memory**: Process shorter video segments or reduce resolution
**Poor Speaker Separation**: Adjust `--n-speakers` or improve audio quality
**Face Detection Issues**: Ensure good lighting and clear faces
**Blender Import Errors**: Check that Blender is in Video Editing workspace

### Performance Tips
- Process videos in 10-30 minute segments for best results
- Use high-quality source videos (1080p+ recommended)
- Clean audio with minimal background noise
- Close other GPU-intensive applications

## Contributing

This project uses several cutting-edge AI technologies:
- **FaceNet** for face recognition
- **OpenAI Whisper** for speech recognition
- **Resemblyzer** for speaker diarization
- **PyTorch** for deep learning inference

## 📄 License

This project combines multiple open-source technologies for video processing and AI analysis.

