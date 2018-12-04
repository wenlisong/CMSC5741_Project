import numpy as np
from lshash import LSHash

feature_dir = "./feature/"
sample = np.loadtxt(feature_dir + "1028975_1983-07-06_2012.jpg.txt")
lsh = LSHash(16, 128, storage_config={"redis": {"host": 'localhost', "port": 6379, "db": 0}},
             matrices_filename="./matrices.npz")
result = lsh.query(sample, 5)
print(result)