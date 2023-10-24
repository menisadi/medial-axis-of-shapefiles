import sys

import geopandas as gpd
import matplotlib.pyplot as plt


def convert_shp_to_bw_png(path_to_shapefile, resulting_name):
    """
    This function converts a shapefile to a black and white png image.
    :param path_to_shapefile: path to the shapefile
    :param resulting_name: name of the resulting image
    :return: None
    """
    # Read shapefile
    gdf = gpd.read_file(path_to_shapefile)

    # Create png image
    fig, ax = plt.subplots(figsize=(4, 4))
    gdf.plot(ax=ax)

    ax.axis("off")

    plt.savefig(
        resulting_name + ".png", dpi=300, bbox_inches="tight", pad_inches=0
    )

    # convert the image to black and white
    from PIL import Image

    img = Image.open(resulting_name + ".png")
    gray = img.convert("L")
    bw = gray.point(lambda x: 0 if x < 128 else 255, "1")
    bw.save(resulting_name + "_bw.png")


if __name__ == "__main__":
    args = sys.argv[1:]
    convert_shp_to_bw_png(args[0], args[1])
