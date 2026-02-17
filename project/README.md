# Optical Flow–Based Video Editing

This repository provides a Python framework for dense and long-term motion estimation
applied to video editing.

## Context
Project of UE Computer Vision.

## Objectives
- Estimate dense optical flow in video sequences
- Integrate motion over time (long-term)
- Propagate a manual edit across a video using motion fields

## Structure
See `src/` for the main pipeline.

## Requirements
- Python 3.9+
- OpenCV
- NumPy

## Disclaimer
This code is provided as a baseline for educational purposes.
Students are expected to analyze its limitations and propose improvements.

## Code architecture

project/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── input_frames/
│   │   ├── frame_000.png
│   │   ├── frame_001.png
│   │   └── ...
│   └── masks/                     # optional (manual or automatic)
│
├── edit/
│   ├── reference_frame.png
│   └── edited_frame.png            # edited with GIMP
│
├── output/
│   ├── flow_visualization/
│   ├── propagated_frames/
│   └── final_video.mp4
│
├── src/
│   ├── __init__.py
│   │
│   ├── config.py                   # paths and parameters
│   │
│   ├── motion/
│   │   ├── __init__.py
│   │   ├── optical_flow.py          # dense flow estimation
│   │   ├── long_term_flow.py        # temporal integration
│   │   └── visualization.py
│   │
│   ├── editing/
│   │   ├── __init__.py
│   │   ├── warping.py               # image warping
│   │   ├── propagation.py           # edit propagation logic
│   │   └── occlusion.py             # optional occlusion handling
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── temporal_metrics.py
│   │   └── qualitative.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── io.py                    # load/save frames
│   │   ├── video.py                 # frame ↔ video
│   │   └── logging.py
│   │
│   └── main.py                      # end-to-end pipeline
│
└── slides/
    └── presentation.pdf

