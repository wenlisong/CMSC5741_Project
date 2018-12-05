import time

from lshash.lshash import LSHash
import json
import os
import face_recognition

lsh = LSHash(16, 128, storage_config={"redis": {"host": 'localhost', "port": 6379, "db": 0}},
             matrices_filename="./matrices.npz")

sample_dir = "./data/sample/"
for file in os.listdir(sample_dir):
    start = time.time()
    face_image = face_recognition.load_image_file(os.path.join(sample_dir, file))
    encodings = face_recognition.face_encodings(face_image)
    if len(encodings):
        print("Start extract face image and query:%s" % file)
        # Extract face feature
        face_feature = encodings[0]
        # Query similar images from redis
        result = lsh.query(face_feature, num_results=5)

        # Print top similar images
        for rank, item in enumerate(result, start=1):
            img_path = json.loads(item[0])[1]
            distance = item[1]
            print("Top #%d similar image:%s, The distance is:%f" % (rank, img_path, distance))
        print("Time cost:%s\n" % str(time.time() - start))
