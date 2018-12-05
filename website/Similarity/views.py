from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import os
import face_recognition
import numpy as np
from lshash.lshash import LSHash
import pdb

def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method=="GET":
        return  render(request,'index.html')
    elif request.method == "POST":
        res = {"status":"success","code":999}
        img_obj = request.FILES.get('img')
        with open(os.path.join('static/images', img_obj.name), 'wb') as f:
            for chunk in img_obj.chunks(chunk_size=1024):
                f.write(chunk)
        feature_path = extract(img_obj.name)
        if feature_path:
            query(feature_path)
            res['upload_img'] = os.path.join('/static/images', img_obj.name)
            return JsonResponse(res)
def query(feature_path):
    sample = np.loadtxt(feature_path)
    lsh = LSHash(16, 128, storage_config={"redis": {"host": 'localhost', "port": 8080, "db": 0}},
             matrices_filename="./matrices.npz")
    result = lsh.query(sample, num_results=10)
    # Print Top Similar Images
    for rank, item in enumerate(result, start=1):
        img_path = json.loads(item[0])[1]
        distance = item[1]
        print("Top #%d similar image:%s, The distance is:%f" % (rank, img_path, distance))

def extract(image_name):
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "static/images")
    #extract features from file_path
    image_path = os.path.join(file_path, image_name)
    picture_of_me = face_recognition.load_image_file(image_path)
    if len(face_recognition.face_encodings(picture_of_me)):
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        feature_path = cwd+'/static/feature/{0}.txt'.format(image_name)
        np.savetxt(feature_path, my_face_encoding, fmt='%f')
        return feature_path
    else:
        return False
