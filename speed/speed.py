import PIL.Image
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np

index = 1

px_val = []

while True:
    # Load images until file error
    try:
        im = PIL.Image.open("seq/out_" + str(index) + ".png").convert("L")
        index = index + 1
    except IOError:
        # Sample frequency of 25 fps
        fs = 25.0

        # Do spectrogram
        f, t, Sxx = signal.spectrogram(np.array(px_val), fs, nperseg=32, nfft=128)

        # Plot everything
        plt.pcolormesh(t, f, Sxx)
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()
        
        exit()

    # Get pixel value
    img = im.crop((400, 100, 1000, 400))
    px_val.append(np.mean(img))


