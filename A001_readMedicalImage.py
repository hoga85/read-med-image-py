import os # change the working directory
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
import matplotlib.cm as cm
from medpy.io import load

os.chdir("G:/My Drive/15_KingsCollegeLondon/A007_Phantom_UG_project/Medical Images")
#print("Current Working Directory ", os.getcwd()) # Show the working directory.
filename ="18991230_000000VQuRyuRCSSSH-Z0xOH-Zl1559s008a1001.nii.gz"
image_data, image_header = load(filename)

fig = plt.figure()  # Create a blank figure
for i in np.array(range(26, 50, 1)): # After 26, no image is formed
    print(i)
    plt.close(fig)
    plt.imshow(image_data[:, :, i], interpolation='nearest')
    plt.show()
    plt.pause(0.1)

