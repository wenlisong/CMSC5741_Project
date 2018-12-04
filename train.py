import time
from lshash import *
import numpy as np
import os

# A sample could be 1028975_1983-07-06_2012.jpg.txt

lsh = LSHash(16, 128, storage_config={"redis": {"host": 'localhost', "port": 6379, "db": 0}},
             matrices_filename="./matrices.npz")
feature_dir = ".data/feature/"
counter = 0
start = time.time()
for file in os.listdir(feature_dir):
    feature = np.loadtxt(feature_dir + file)
    lsh.index(feature, file)

    counter += 1
    if counter % 100 == 0:
        print("processed " + str(counter) + " features")

print("index time cost:" + str(time.time() - start))
