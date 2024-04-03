import numpy as np

from matplotlib.figure import Figure
import io


def fig_to_array(fig: Figure) -> np.ndarray:
    """Convert a matplotlib figure to a numpy array."""
    # fig.tight_layout(pad=0)
    # fig.canvas.draw()
    # data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    # return data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    fig.canvas.draw()
    buf = fig.canvas.buffer_rgba()
    w, h = fig.canvas.get_width_height()
    arr = np.frombuffer(buf, np.uint8).reshape(h, w, -1)[:,:,:3]  # Extract RGB channels

    return arr