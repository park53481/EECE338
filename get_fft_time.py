import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse
 
import time

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

time_1= time()

print("drawing plot for", args.filename)

time_2= time()

samplerate, data = sio.wavfile.read(args.filename)
fftsize = len(data)
data_fft = fftpack.fft(data, fftsize)

print('fft_time= ', time_2-time_1)
