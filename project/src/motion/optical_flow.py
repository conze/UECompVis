"""
optical_flow.py

Dense optical flow estimation module.

This file provides baseline implementations for dense motion estimation
between video frames. It is designed to be easily extensible to learning-based
methods (e.g., FlowNet, RAFT).

Author: Computer Vision course
"""

from typing import List
import cv2
import numpy as np


def compute_optical_flow_pair(
    frame_t: np.ndarray,
    frame_t1: np.ndarray,
    method: str = "farneback"
) -> np.ndarray:
    """
    Compute dense optical flow between two consecutive frames.

    Args:
        frame_t: frame at time t (H, W, 3), uint8
        frame_t1: frame at time t+1 (H, W, 3), uint8
        method: optical flow method ("farneback", "custom")

    Returns:
        flow: dense optical flow (H, W, 2), float32
              flow[..., 0] = horizontal displacement
              flow[..., 1] = vertical displacement
    """
    gray_t = cv2.cvtColor(frame_t, cv2.COLOR_BGR2GRAY)
    gray_t1 = cv2.cvtColor(frame_t1, cv2.COLOR_BGR2GRAY)

    if method == "farneback":
        flow = cv2.calcOpticalFlowFarneback(
            gray_t,
            gray_t1,
            None,
            pyr_scale=0.5,
            levels=4,
            winsize=15,
            iterations=5,
            poly_n=7,
            poly_sigma=1.5,
            flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN
        )

    elif method == "custom":
        raise NotImplementedError(
            "Custom optical flow method not implemented. "
            "Students are expected to implement their own method here."
        )

    else:
        raise ValueError(f"Unknown optical flow method: {method}")

    return flow.astype(np.float32)


def compute_dense_flows(
    frames: List[np.ndarray],
    method: str = "farneback",
    verbose: bool = True
) -> List[np.ndarray]:
    """
    Compute dense optical flow for an entire video sequence.

    Args:
        frames: list of video frames [frame_0, frame_1, ..., frame_T]
        method: optical flow method
        verbose: display progress

    Returns:
        flows: list of optical flows
               flows[t] maps frame t -> frame t+1
    """
    assert len(frames) >= 2, "At least two frames are required."

    flows = []

    for t in range(len(frames) - 1):
        if verbose:
            print(f"[OpticalFlow] Computing flow {t} -> {t+1}")

        flow = compute_optical_flow_pair(
            frames[t],
            frames[t + 1],
            method=method
        )
        flows.append(flow)

    return flows


def backward_flow(flow: np.ndarray) -> np.ndarray:
    """
    Approximate backward optical flow from forward flow.

    This is a naive approximation and is intentionally left simple.
    Students are encouraged to improve this using forward-backward consistency.

    Args:
        flow: forward flow (H, W, 2)

    Returns:
        backward flow (H, W, 2)
    """
    return -flow


def flow_magnitude(flow: np.ndarray) -> np.ndarray:
    """
    Compute magnitude of optical flow vectors.

    Args:
        flow: optical flow (H, W, 2)

    Returns:
        magnitude map (H, W)
    """
    return np.linalg.norm(flow, axis=2)


def flow_statistics(flow: np.ndarray) -> dict:
    """
    Compute simple statistics on an optical flow field.

    Args:
        flow: optical flow (H, W, 2)

    Returns:
        dictionary with basic statistics
    """
    mag = flow_magnitude(flow)

    return {
        "min_magnitude": float(np.min(mag)),
        "max_magnitude": float(np.max(mag)),
        "mean_magnitude": float(np.mean(mag)),
        "std_magnitude": float(np.std(mag))
    }
