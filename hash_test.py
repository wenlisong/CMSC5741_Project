import face_recognition
from lsh.lshash import *
from constants import *

lsh = LSHash(HASH_SIZE, INPUT_DIMS, num_hashtables=NUMS_TABLE, storage_config=STORAGE_CONFIG,
             matrices_filename=MATRICES_NAME)
sample_dir = "./data/sample/"

sample_image = face_recognition.load_image_file(os.path.join(sample_dir, "sample.jpg"))
sample_feature = face_recognition.face_encodings(sample_image)[0]
print("The sample hash: %s\n" % lsh.hash(sample_feature))

for file in os.listdir(sample_dir):
    face_image = face_recognition.load_image_file(os.path.join(sample_dir, file))
    encodings = face_recognition.face_encodings(face_image)
    if len(encodings):
        face_feature = encodings[0]
        face_hash = lsh.hash(face_feature)
        print("Sample %s hash in directory:%s" % (file, face_hash))