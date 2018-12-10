import os
import time
import face_recognition

try:
    from package.lsh.lshash import *
    from package.lsh.constants import *
except:
    from lshash import *
    from constants import *

"""
The test image dataset capacity is 62329
The face features in the dataset is 39173
"""


def train(lsh):
    feature_dir = "../../data/tmp/"
    counter = 0
    start = time.time()
    for file in os.listdir(feature_dir):
        feature = np.loadtxt(feature_dir + file)
        lsh.index(feature, file)

        counter += 1
        if counter % 1000 == 0:
            print("processed " + str(counter) + " features")

    cost = time.time() - start
    print("index time cost:" + str(cost))
    return cost


def query(lsh, image_path):
    start = time.time()
    face_image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(face_image)
    result = []
    if len(encodings):
        # Extract face feature
        face_feature = encodings[0]
        # Query similar images from redis
        result = lsh.query(face_feature, num_results=5, distance_func="norm")
    return result, (time.time() - start)


def testcase(lsh):
    train_cost = train(lsh)
    train_time.append(train_cost)

    test_dir = "../../data/tmp/"
    total_count = 0
    correct_count = 0
    query_cost = 0
    for file in os.listdir(test_dir):
        start = time.time()
        feature = np.loadtxt(test_dir + file)
        result = lsh.query(feature, num_results=5, distance_func="norm")
        cost = time.time() - start

        total_count += 1
        query_cost += cost
        if result:
            for item in result:
                img_info = json.loads(item[0])
                img_path = img_info[1]
                if file in img_path:
                    correct_count += 1
                    break
        if total_count % 100 == 0:
            print("query total_count=%d, correct_count=%d" % (total_count, correct_count))
    query_time.append(query_cost)
    accuracy.append(float(correct_count) / float(total_count))


def writerecords(records, file_path):
    with open(file_path, 'w') as f:
        for item in records:
            f.write("%s\n" % str(item))


output_dir = "../../data/output/"
query_time = []
train_time = []
accuracy = []
hashtables = []
# hashtable test
for num_hashtables in range(2, 11):
    hashtables.append(num_hashtables)
    print("Start test with num_hashtables=%d" % num_hashtables)
    # clear redis train records
    os.system("redis-cli FLUSHALL")
    lsh = LSHash(16, INPUT_DIMS, num_hashtables=num_hashtables, storage_config=STORAGE_CONFIG,
                 matrices_filename=MATRICES_NAME, overwrite=True)
    testcase(lsh)

writerecords(query_time, os.path.join(output_dir, "hashtable_query_time"))
writerecords(train_time, os.path.join(output_dir, "hashtable_train_time"))
writerecords(accuracy, os.path.join(output_dir, "hashtable_accuracy"))
writerecords(hashtables, os.path.join(output_dir, "hashtable_hashtables"))
print("HashTables Test Done!")

# hashsize test
query_time = []
train_time = []
accuracy = []
hashsizes = []
for hashsize in range(10, 19):
    hashsizes.append(hashsize)
    print("Start test with hashsize=%d" % hashsize)
    # clear redis train records
    os.system("redis-cli FLUSHALL")
    lsh = LSHash(hashsize, INPUT_DIMS, num_hashtables=NUMS_TABLE, storage_config=STORAGE_CONFIG,
                 matrices_filename=MATRICES_NAME, overwrite=True)
    testcase(lsh)

writerecords(query_time, os.path.join(output_dir, "hashsize_query_time"))
writerecords(train_time, os.path.join(output_dir, "hashsize_train_time"))
writerecords(accuracy, os.path.join(output_dir, "hashsize_accuracy"))
writerecords(hashsizes, os.path.join(output_dir, "hashsize_hashtables"))
print("HashSizes Test Done!")