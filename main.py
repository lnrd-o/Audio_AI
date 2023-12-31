# -*- coding: utf-8 -*-
"""Sistema Experto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fw7O3fU0PbKB83rB2BtxyrRlxJnPvA7d
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

import cv2
import imutils

from glob import glob

import librosa
import librosa.display
import IPython.display as ipd

from itertools import cycle

sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])

audio_files = glob('./cancion1.wav')

ipd.Audio(audio_files[0])

y, sr = librosa.load(audio_files[0])
print(f'y: {y[:16]}')
print(f'shape y: {y.shape}')
print(f'sr: {sr}')

pd.Series(y).plot(figsize=(20, 5),
                  lw=1,
                  title='Muestra completa del Audio',
                 color=color_pal[0])
plt.show()

D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
S_db.shape

fig, ax = plt.subplots(figsize=(15, 10))
img = librosa.display.specshow(S_db,
                               cmap='mako',
                              x_axis='time',
                              y_axis='log',
                              ax=ax)
#ax.set_title('Espectrograma', fontsize=20)
#fig.colorbar(img, ax=ax, format=f'-%0.1fdB')
ax.set_axis_off()
plt.savefig('1.png', bbox_inches='tight',transparent=True, pad_inches=0.0 )
plt.show()

"""<h1>Analisis de Canción 2</h1>"""

audio_files = glob('./cancion2.wav')

ipd.Audio(audio_files[0])

y, sr = librosa.load(audio_files[0])
print(f'y: {y[:16]}')
print(f'shape y: {y.shape}')
print(f'sr: {sr}')

pd.Series(y).plot(figsize=(20, 5),
                  lw=1,
                  title='Muestra completa del Audio',
                 color=color_pal[0])
plt.show()

D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
S_db.shape

fig, ax = plt.subplots(figsize=(15, 10))
img = librosa.display.specshow(S_db,
                               cmap='mako',
                              x_axis='time',
                              y_axis='log',
                              ax=ax)
#ax.set_title('Espectrograma', fontsize=20)
#fig.colorbar(img, ax=ax, format=f'-%0.1fdB')
ax.set_axis_off()
plt.savefig('2.png', bbox_inches='tight',transparent=True, pad_inches=0.0 )
plt.show()

"""<h1>Analisis Comparativo</h1>"""

from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def ecm(cancionA, cancionB):
    err = np.sum((cancionA.astype("float") - cancionB.astype("float")) ** 2)
    err /= float(cancionA.shape[0] * cancionA.shape[1])
    return err

def comparar(cancionA, cancionB):
    m = ecm(cancionA, cancionB)
    s = ssim(cancionA, cancionB)
    fig = plt.figure("")
    s = s*1000
    plt.suptitle("ECM: %.3f | Similitud Estructural: %.2f" % (m,s))
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(cancionA, cmap = plt.cm.gray)
    plt.axis("off")
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(cancionB, cmap = plt.cm.gray)
    plt.axis("off")
    plt.show()


original = cv2.imread("1.png")
contrast = cv2.imread("2.png")

original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)


comparar(original, contrast)
