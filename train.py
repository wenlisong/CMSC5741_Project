import time
from lsh.lshash import *
from constants import *
import numpy as np
import os

# A sample could be 1028975_1983-07-06_2012.jpg.txt

lsh = LSHash(HASH_SIZE, INPUT_DIMS, storage_config=STORAGE_CONFIG, matrices_filename=MATRICES_NAME)
feature_dir = "./data/feature/"
counter = 0
start = time.time()
for file in os.listdir(feature_dir):
    feature = np.loadtxt(feature_dir + file)
    lsh.index(feature, file)

    counter += 1
    if counter % 500 == 0:
        print("processed " + str(counter) + " features")

print("index time cost:" + str(time.time() - start))
