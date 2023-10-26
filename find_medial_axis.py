import sys

import matplotlib.pyplot as plt
import skimage
from skimage.morphology import medial_axis


def find_ma(path_to_bw_image, result_dpi=1000):
    bw_mesh = skimage.io.imread(path_to_bw_image)
    medial_axis_mesh = medial_axis(skimage.util.invert(bw_mesh))

    combined_mesh = bw_mesh | medial_axis_mesh

    plt.imshow(combined_mesh, cmap=plt.cm.gray)
    plt.axis("off")
    plt.savefig("medial_axis.png", bbox_inches="tight", dpi=result_dpi)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2:
        find_ma(args[0], int(args[1]))
    else:
        find_ma(args[0])
