"""
main.py

Entry point for the Optical Flow–Based Video Editing project.

Pipeline:
1. Load video frames
2. Estimate dense optical flow
3. Visualize motion fields
4. Propagate a manual edit through the sequence
5. Save results (frames + video)

Author: Computer Vision course
"""

import os
import cv2

from motion.optical_flow import compute_dense_flows
from motion.visualization import save_flow_visualization
from editing.propagation import propagate_edit
from utils.io import load_frames, save_frames
from utils.video import frames_to_video


# ==========================
# Configuration
# ==========================

INPUT_FRAMES_DIR = "data/input_frames"
EDITED_FRAME_PATH = "edit/edited_frame.png"

FLOW_METHOD = "farneback"      # baseline method
VISUALIZE_FLOW = True

FLOW_VIS_DIR = "output/flow_visualization"
PROPAGATED_DIR = "output/propagated_frames"
OUTPUT_VIDEO_PATH = "output/final_video.mp4"

FPS = 25


# ==========================
# Main pipeline
# ==========================

def main():
    print("=== Optical Flow–Based Video Editing ===")

    # 1. Load input frames
    print("[1] Loading input frames...")
    frames = load_frames(INPUT_FRAMES_DIR)
    assert len(frames) >= 2, "At least two frames are required."
    print(f"    Loaded {len(frames)} frames")

    # 2. Compute dense optical flow
    print("[2] Computing dense optical flow...")
    flows = compute_dense_flows(
        frames,
        method=FLOW_METHOD,
        verbose=True
    )

    # 3. Visualize optical flow (optional)
    if VISUALIZE_FLOW:
        print("[3] Saving flow visualizations...")
        for t, flow in enumerate(flows):
            save_flow_visualization(
                flow=flow,
                frame=frames[t],
                output_dir=FLOW_VIS_DIR,
                index=t
            )

    # 4. Load edited reference frame
    print("[4] Loading edited reference frame...")
    edited_frame = cv2.imread(EDITED_FRAME_PATH)
    assert edited_frame is not None, "Edited frame could not be loaded."

    # 5. Propagate editing through the video
    print("[5] Propagating editing through the sequence...")
    propagated_frames = propagate_edit(
        edited_img=edited_frame,
        flows=flows
    )

    # 6. Save propagated frames
    print("[6] Saving propagated frames...")
    save_frames(propagated_frames, PROPAGATED_DIR)

    # 7. Export final video
    print("[7] Exporting final video...")
    frames_to_video(
        PROPAGATED_DIR,
        OUTPUT_VIDEO_PATH,
        fps=FPS
    )

    print("=== Done ===")
    print(f"Results saved in: {os.path.abspath('output/')}")


if __name__ == "__main__":
    main()
