## Large-scale Face Retrieval System based on Locality-Sensitive Hashing
### Abstract
Face retrieval is one of the prime issues in big data analysis and machine learning. With the availability of powerful parallel ma- chines and massive increase in training data, deep convolutional neural networks (CNNs) achieve great progress on face recognition. However, the progress of for face retrieval for large-scale datasets is still a challenging problem due to the huge number of face im- ages. In this project, we proposed a novel system based on deep learning and LSH to achieve large-scale face retrieval.After prepro- cessing image to extract feature, we took a in-depth research into the state-of-arts LSH frameworks for different similarity metrics and chose the best method to tackle our practical problem.Finally, we implemented a website to give a intuitive interpretation of our results.

For more details, please refers to our [Project Report](static/images/report.pdf)
![](static/images/WechatIMG287.jpeg)

### Structure
![](static/images/example-1.jpg)

### Redis

* redis service start: `brew services start redis` or `redis-server /usr/local/etc/redis.conf`
* redis service detect: `redis-cli ping`
* redis shutdown: `redis-cli shutdown`
* redis get all keys: `redis-cli keys "*"`
* redis delete all data: `redis-cli FLUSHALL`

### Unix

* find file path under directory: `find ./ -name "xxx"`
* find files count under directory: `find DIRNAME -type f | wc -l`

### Output

#### Hash Test Output

```
The sample hash: ['0011100010', '0101101100', '1010101110', '0101011111', '1101000101']

Sample query_sample_02_944600.jpg hash in directory:['0011000010', '0101101101', '1010101110', '0100111111', '1101000100']
Sample query_image_04_944600.jpg hash in directory:['0011100010', '0101101100', '1010101110', '0101011111', '1101000101']
Sample sample.jpg hash in directory:['0011100010', '0101101100', '1010101110', '0101011111', '1101000101']
Sample query_sample_01_944600.jpg hash in directory:['0011100010', '0101101100', '1010101110', '0100011111', '1101000100']
```

#### Query Output

```
Start extract face image and query:query_sample_02_944600.jpg
Top #1 similar image:34475481_1994-01-19_2014.jpg.txt, The distance is:0.516188
Top #2 similar image:32473067_1990-11-10_2013.jpg.txt, The distance is:0.544584
Top #3 similar image:24242071_1987-06-11_2012.jpg.txt, The distance is:0.545507
Top #4 similar image:7816311_1986-02-11_2015.jpg.txt, The distance is:0.558843
Top #5 similar image:12259352_1987-02-23_2013.jpg.txt, The distance is:0.562442
Time cost:0.62685084343

Start extract face image and query:query_image_04_944600.jpg
Top #1 similar image:944600_1968-02-05_2006.jpg.txt, The distance is:0.000004
Top #2 similar image:22998644_1982-06-06_2014.jpg.txt, The distance is:0.529140
Top #3 similar image:18678530_1955-11-30_2012.jpg.txt, The distance is:0.530373
Top #4 similar image:7218144_1940-11-30_1964.jpg.txt, The distance is:0.540707
Top #5 similar image:19229774_1973-11-19_2009.jpg.txt, The distance is:0.557928
Time cost:0.521167993546

Start extract face image and query:sample.jpg
Top #1 similar image:944600_1968-02-05_2006.jpg.txt, The distance is:0.000004
Top #2 similar image:22998644_1982-06-06_2014.jpg.txt, The distance is:0.529140
Top #3 similar image:18678530_1955-11-30_2012.jpg.txt, The distance is:0.530373
Top #4 similar image:7218144_1940-11-30_1964.jpg.txt, The distance is:0.540707
Top #5 similar image:19229774_1973-11-19_2009.jpg.txt, The distance is:0.557928
Time cost:0.494425058365

Start extract face image and query:query_sample_01_944600.jpg
Top #1 similar image:944600_1968-02-05_2006.jpg.txt, The distance is:0.364206
Top #2 similar image:3594289_1979-06-07_2009.jpg.txt, The distance is:0.527838
Top #3 similar image:24242071_1987-06-11_2012.jpg.txt, The distance is:0.534310
Top #4 similar image:3934694_1969-11-19_2014.jpg.txt, The distance is:0.535654
Top #5 similar image:617029_1917-04-16_1962.jpg.txt, The distance is:0.535810
Time cost:0.46483206749
```

## Dataset
IMDB-WIKI – 500k+ face images with age and gender labels[website](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)
