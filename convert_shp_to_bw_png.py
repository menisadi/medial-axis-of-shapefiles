import sys

import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image


def convert_shp_to_bw_png(path_to_shapefile, resulting_name, chosen_dpi=1000):
    """
    This function converts a shapefile to a black and white png image.
    :param path_to_shapefile: path to the shapefile
    :param resulting_name: name of the resulting image
    :return: None
    """
    # Read shapefile
    gdf = gpd.read_file(path_to_shapefile)

    # Create png image
    fig, ax = plt.subplots()
    gdf.plot(ax=ax)

    ax.axis("off")

    plt.savefig(
        resulting_name + ".png",
        dpi=chosen_dpi,
        bbox_inches="tight",
        pad_inches=0,
    )

    # convert the image to black and white
    img = Image.open(resulting_name + ".png")
    gray = img.convert("L")
    bw = gray.point(lambda x: 0 if x < 128 else 255, "1")
    bw.save(resulting_name + "_bw.png")


if __name__ == "__main__":
    args = sys.argv[1:]
    chosen_dpi = 1000
    if len(args) == 3:
        chosen_dpi = int(args[2])
    convert_shp_to_bw_png(args[0], args[1], chosen_dpi)
