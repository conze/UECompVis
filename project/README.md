Optical Flow–Based Video Editing
===============================

This repository provides a Python framework for dense and long-term optical flow
estimation applied to video editing.
The goal is to propagate a user-defined manual edit consistently across a video
sequence using motion information.

Context
-------
This project was developed as part of the UE Computer Vision course.

Objectives
----------
The main objectives of this project are:
- Estimate dense optical flow between consecutive video frames
- Integrate motion over time to obtain long-term correspondences
- Propagate a manual edit throughout a video using estimated motion fields

Project Structure
-----------------
The core implementation is located in the src/ directory and follows a modular
pipeline.

Requirements
------------
- Python 3.9 or later
- OpenCV
- NumPy

All dependencies are listed in requirements.txt.

Disclaimer
----------
This code is provided for educational purposes only.
It serves as a baseline implementation: students are expected to analyze its
limitations (e.g. drift, occlusions, temporal inconsistencies) and propose
improvements.

Code Architecture
-----------------

project/
|
|-- README.txt
|-- requirements.txt
|
|-- data/
|   |-- input_frames/
|   |   |-- frame_000.png
|   |   |-- frame_001.png
|   |   `-- ...
|   `-- masks/                     (optional: manual or automatic)
|
|-- edit/
|   |-- reference_frame.png
|   `-- edited_frame.png           (edited externally, e.g. with GIMP)
|
|-- output/
|   |-- flow_visualization/
|   |-- propagated_frames/
|   `-- final_video.mp4
|
|-- src/
|   |-- __init__.py
|   |
|   |-- config.py                  (paths and global parameters)
|   |
|   |-- motion/
|   |   |-- __init__.py
|   |   |-- optical_flow.py         (dense optical flow estimation)
|   |   |-- long_term_flow.py       (temporal motion integration)
|   |   `-- visualization.py
|   |
|   |-- editing/
|   |   |-- __init__.py
|   |   |-- warping.py              (image warping)
|   |   |-- propagation.py          (edit propagation logic)
|   |   `-- occlusion.py            (optional occlusion handling)
|   |
|   |-- evaluation/
|   |   |-- __init__.py
|   |   |-- temporal_metrics.py
|   |   `-- qualitative.py
|   |
|   |-- utils/
|   |   |-- __init__.py
|   |   |-- io.py                   (frame I/O utilities)
|   |   |-- video.py                (frame <-> video conversion)
|   |   `-- logging.py
|   |
|   `-- main.py                    (end-to-end pipeline)
|
`-- slides/
    `-- presentation.pdf
