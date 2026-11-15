"""Small helper shared by all scripts: save the figure as PNG, then show it."""
import sys
from pathlib import Path

import matplotlib.pyplot as plt

IMAGES = Path(__file__).parent / "images"


def save_and_show(filename):
    IMAGES.mkdir(exist_ok=True)
    plt.savefig(IMAGES / filename, dpi=120, bbox_inches="tight")
    print("saved ->", IMAGES / filename)
    if "--no-show" not in sys.argv:      # run with --no-show to only save images
        plt.show()
    plt.close()
