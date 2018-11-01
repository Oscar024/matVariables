import scipy.io as sio
import numpy as np

mat_contents = sio.loadmat('trimvec2.mat')

print(mat_contents["x1"])