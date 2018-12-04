import os
import face_recognition
import numpy as np
count = 0
file_path = "/research/pheng5/jzwang/big_data/project/imdb_crop/00"
#extract features from file_path
for photo in os.listdir(file_path):
    path = os.path.join(file_path, photo)
    picture_of_me = face_recognition.load_image_file(path)
    if len(face_recognition.face_encodings(picture_of_me)):
         my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
         np.savetxt(file_path % photo, my_face_encoding, fmt='%f')
    print(count)
    count = count + 1
