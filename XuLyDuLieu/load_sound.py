import os.path
import librosa

import load
import librosa
from glob import glob
import librosa.display
import matplotlib.pyplot as plt
import random
import tensorflow as tf
import tensorflow_io as tfio
from keras import datasets, layers, models

if __name__ == "__main__":

    # p = "D:/MyProject/_python/VOiCES_devkit/VOiCES_devkit/distant-16k/speech/train/rm1/babb/sp0032/Lab41-SRI-VOiCES-rm1-babb-sp0032-ch004137-sg0007-mc01-stu-clo-dg150.wav"
    p = os.path.abspath(os.path.join(load.VOiCES_devkit, "distant-16k/speech/train/rm1/babb/sp0032/Lab41-SRI-VOiCES-rm1-babb-sp0032-ch004137-sg0007-mc01-stu-clo-dg150.wav"))
    x, sr = librosa.load(p)



    # Tạo tensor từ tệp âm thanh
    audio_tensor = tf.convert_to_tensor(x, dtype=tf.float32)
    # print(audio_tensor)
    # Chuyển đổi âm thanh thành dạng spectrogram
    spectrogram = tfio.audio.spectrogram(audio_tensor, nfft=2048, window=2048, stride=512)
    # print(spectrogram)
    # sp_ft = librosa.stft(x)
    # sp_db = librosa.amplitude_to_db(abs(sp_ft))
    #
    # plt.figure(figsize=(14, 5))
    # plt.title('Noisy Speech')
    # img = librosa.display.specshow(sp_db, sr=sr, x_axis='time', y_axis='hz')
    #
    #
    # plt.figure(figsize=(10, 5))
    # librosa.display.waveshow(x, color='blue', alpha=0.6, label='Noisry Speech')
    # plt.legend()
    # plt.show()

