# CMSC5741_Project

## Redis

* redis service start: `brew services start redis` or `redis-server /usr/local/etc/redis.conf`
* redis service detect: `redis-cli ping`
* redis shutdown: `redis-cli shutdown`
* redis get all keys: `redis-cli keys "*"`
* redis delete all data: `redis-cli FLUSHALL`

## Unix

* find file path under directory: `find ./ -name "xxx"`