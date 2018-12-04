import time
from lshash import LSHash
import numpy as np
import os
import redis

# A sample could be 1028975_1983-07-06_2012.jpg.txt

lsh = LSHash(16, 128)
feature_dir = "./feature/"
counter = 0
sample = np.loadtxt(feature_dir + "1028975_1983-07-06_2012.jpg.txt")

start = time.time()
for file in os.listdir(feature_dir):
    feature = np.loadtxt(feature_dir + file)
    lsh.index(feature, file)

    counter += 1
    # if counter % 100 == 0:
    #     print("processed " + str(counter) + " features")

    if counter >= 1000:
        break

print("index time cost:" + str(time.time() - start))
result = lsh.query(sample, 5)
print(result)

