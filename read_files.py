import numpy as np
import os

def read_files(filename):
    df = np.loadtxt(filename, delimiter=' ', dtype=float)

    n, w = int(df[0][0]), float(df[0][1])

    values = df.T[0][1:]
    weights = df.T[1][1:]

    float_values = []
    float_weights = []

    for v in values:
        float_values.append(float(v))
        
    for w1 in weights:
        float_weights.append(float(w1))

    return n, w, float_weights, float_values

def get_test_files():
    return os.listdir('tests')