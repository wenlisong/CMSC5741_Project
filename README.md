# CMSC5741_Project

## Redis

* redis service start: `brew services start redis` or `redis-server /usr/local/etc/redis.conf`
* redis service detect: `redis-cli ping`
* redis shutdown: `redis-cli shutdown`
* redis get all keys: `redis-cli keys "*"`
* redis delete all data: `redis-cli FLUSHALL`

## Unix

* find file path under directory: `find ./ -name "xxx"`

## Hash Test Output

The sample hash: ['0011100010', '0101101100', '1010101110', '0101011111', '1101000101']

Sample query_sample_02_944600.jpg hash in directory:['0011000010', '0101101101', '1010101110', '0100111111', '1101000100']
Sample query_image_04_944600.jpg hash in directory:['0011100010', '0101101100', '1010101110', '0101011111', '1101000101']
Sample sample.jpg hash in directory:['0011100010', '0101101100', '1010101110', '0101011111', '1101000101']
Sample query_sample_01_944600.jpg hash in directory:['0011100010', '0101101100', '1010101110', '0100011111', '1101000100']