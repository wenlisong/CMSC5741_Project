import time
from lsh.lshash import *
from constants import *
import numpy as np
import os

lsh = LSHash(HASH_SIZE, INPUT_DIMS, num_hashtables=NUMS_TABLE, storage_config=STORAGE_CONFIG,
             matrices_filename=MATRICES_NAME)
feature_dir = "./data/feature/"
counter = 0
start = time.time()
for file in os.listdir(feature_dir):
    feature = np.loadtxt(feature_dir + file)
    lsh.index(feature, file)

    counter += 1
    if counter % 1000 == 0:
        print("processed " + str(counter) + " features")

print("index time cost:" + str(time.time() - start))
