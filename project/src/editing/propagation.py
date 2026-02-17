import numpy as np
from editing.warping import warp_image

def propagate_logo(
    frames,
    edited_frame,
    logo_mask,
    flows,
    start_index
):
    """
    Propagate a logo through a video using optical flow and a binary mask.

    Args:
        frames: original video frames
        edited_frame: frame with inserted logo (H, W, 3)
        logo_mask: binary mask (H, W), values in [0, 1]
        flows: list of optical flows (t -> t+1)
        start_index: index of edited frame

    Returns:
        list of propagated frames
    """
    H, W = logo_mask.shape
    logo_mask = logo_mask[..., None]  # (H, W, 1)

    # Extract logo content
    logo = edited_frame * logo_mask

    results = frames.copy()

    current_logo = logo
    current_mask = logo_mask

    for t in range(start_index, len(flows)):
        flow = flows[t]

        # Warp logo and mask
        current_logo = warp_image(current_logo, flow)
        current_mask = warp_image(current_mask, flow)

        # Recompose frame
        results[t + 1] = (
            current_mask * current_logo +
            (1 - current_mask) * frames[t + 1]
        ).astype(np.uint8)

    return results