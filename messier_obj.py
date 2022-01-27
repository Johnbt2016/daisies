"""
Query ALMA archive for M83 pointings and plotting them on a 2MASS image
"""

import numpy as np
from astroquery.skyview import SkyView
import pylab as pl
import aplpy
import pyregion
import base64
import os

def get_image(messier_image):

    home = os.getenv("HOME")

    m_images = SkyView.get_images(position=str(messier_image), survey=['2MASS-K'],
                                    pixels=1500)
    print(m_images)

    fig = aplpy.FITSFigure(m_images[0])

    fig.show_grayscale()

    fig.savefig(home + '/fig.png', transparent=True)

    with open(home + '/fig.png', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    return [{"type": "image", "data": {"alt": "Messier object image from Skyview", "src": "data:image/png;base64, " + encoded_string.decode('ascii')}}]



if __name__ == "__main__":
    a = get_image('M4')
    print(a)
