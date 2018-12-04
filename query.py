import numpy as np
from lshash.lshash import LSHash
import json

feature_dir = "./data/feature/"
sample = np.loadtxt(feature_dir + "1028975_1983-07-06_2012.jpg.txt")
lsh = LSHash(16, 128, storage_config={"redis": {"host": 'localhost', "port": 6379, "db": 0}},
             matrices_filename="./matrices.npz")
result = lsh.query(sample, num_results=10)

# Print Top Similar Images
for rank, item in enumerate(result, start=1):
    img_path = json.loads(item[0])[1]
    distance = item[1]
    print("Top #%d similar image:%s, The distance is:%f" % (rank, img_path, distance))
