"""
warping.py

Image and mask warping utilities using dense optical flow.

Optical flow convention (IMPORTANT):
-----------------------------------
Given a source image I_src and a destination image I_dst, the optical flow F
is defined such that:

    I_src(x) corresponds to I_dst(x + F(x))

In the reference-based setting used in this project:
- the flow maps pixels from the CURRENT frame to the REFERENCE frame
- edited content (logo, mask) is defined in the reference frame
- warping is used to pull this content into the current frame

This convention must be respected everywhere in the pipeline.
"""

import cv2
import numpy as np


def warp_image(
    image: np.ndarray,
    flow: np.ndarray,
    interpolation: int = cv2.INTER_LINEAR,
    border_mode: int = cv2.BORDER_REFLECT
) -> np.ndarray:
    """
    Warp an image using a dense optical flow field.

    Args:
        image: image to warp
               - RGB image: (H, W, 3)
               - grayscale or mask: (H, W) or (H, W, 1)
        flow: optical flow (H, W, 2)
              mapping pixels from the current frame to the reference frame
        interpolation: OpenCV interpolation method
        border_mode: OpenCV border handling

    Returns:
        warped image with the same shape as input
    """
    h, w = flow.shape[:2]

    # Base pixel grid
    grid_x, grid_y = np.meshgrid(
        np.arange(w),
        np.arange(h)
    )

    # Apply displacement field
    map_x = (grid_x + flow[..., 0]).astype(np.float32)
    map_y = (grid_y + flow[..., 1]).astype(np.float32)

    # Case 1: single-channel image (H, W)
    if image.ndim == 2:
        return cv2.remap(
            image,
            map_x,
            map_y,
            interpolation=interpolation,
            borderMode=border_mode
        )

    # Case 2: single-channel image with explicit channel (H, W, 1)
    if image.ndim == 3 and image.shape[2] == 1:
        warped = cv2.remap(
            image[..., 0],
            map_x,
            map_y,
            interpolation=interpolation,
            borderMode=border_mode
        )
        return warped[..., None]

    # Case 3: RGB image (H, W, 3)
    return cv2.remap(
        image,
        map_x,
        map_y,
        interpolation=interpolation,
        borderMode=border_mode
    )


def warp_mask(
    mask: np.ndarray,
    flow: np.ndarray,
    threshold: float = 0.5
) -> np.ndarray:
    """
    Warp a binary or soft mask using optical flow.

    Args:
        mask: mask image
              - shape (H, W) or (H, W, 1)
              - values in [0, 1]
        flow: optical flow (H, W, 2)
        threshold: binarization threshold after warping

    Returns:
        warped binary mask of shape (H, W, 1), values in {0, 1}
    """
    warped = warp_image(
        mask,
        flow,
        interpolation=cv2.INTER_LINEAR,
        border_mode=cv2.BORDER_CONSTANT
    )

    # Ensure shape (H, W, 1)
    if warped.ndim == 2:
        warped = warped[..., None]

    # Re-binarize to avoid mask diffusion
    warped = (warped > threshold).astype(np.float32)

    return warped
