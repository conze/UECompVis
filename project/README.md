# Optical Flow–Based Video Editing

This repository contains a Python implementation of an **optical flow–based video editing pipeline**.
The objective is to propagate a **manual edit applied to a reference frame** across a video sequence
using dense and long-term motion estimation.

---

## Context

This project was developed in the context of the **UE Computer Vision** course.  
It is intended as an **educational baseline**, not as a production-ready system.

---

## Objectives

The goals of this project are to:

- Estimate **dense optical flow** between consecutive video frames
- Integrate motion over time to obtain **long-term correspondences**
- Propagate a **manual image edit** consistently across a video sequence
- Analyze typical limitations such as drift, occlusions, and temporal artifacts

---

## Pipeline Overview

1. Load a sequence of input frames  
2. Estimate dense optical flow between frames  
3. Accumulate motion to obtain long-term displacement fields  
4. Warp the edited reference frame through time  
5. Generate an edited output video  

---

## Project Structure

```text
project/
|-- README.md
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
|   |-- config.py                  (paths and global parameters)
|   |
|   |-- motion/
|   |   |-- optical_flow.py         (dense optical flow estimation)
|   |   |-- long_term_flow.py       (temporal integration)
|   |   `-- visualization.py
|   |
|   |-- editing/
|   |   |-- warping.py              (image warping)
|   |   |-- propagation.py          (edit propagation logic)
|   |   `-- occlusion.py            (optional occlusion handling)
|   |
|   |-- evaluation/
|   |   |-- temporal_metrics.py
|   |   `-- qualitative.py
|   |
|   |-- utils/
|   |   |-- io.py                   (frame I/O utilities)
|   |   |-- video.py                (frame <-> video conversion)
|   |   `-- logging.py
|   |
|   `-- main.py                    (end-to-end pipeline)
|
`-- slides/
    `-- presentation.pdf
