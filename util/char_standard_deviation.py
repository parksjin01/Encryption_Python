import string
import numpy as np

def check_dev(file):
    times = word_frequency(file).values()
    return np.std(times)
