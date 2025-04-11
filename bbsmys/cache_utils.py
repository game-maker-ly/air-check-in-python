from diskcache import Cache
from diskcache import JSONDisk

# 实例化缓存对象，指定缓存目录
# 基于sqlite数据库，本质上就是封装了数据库的操作

class CacheUtils:
    """
    缓存工具类
    """

    def __init__(self, cache: Cache = None):
        self.cache = cache if cache else Cache('./tmp')

    def get_value(self, cache_key: str):
        value = self.cache.get(cache_key, None)
        # if value is not None:
        #     print(f"Cache hit for key: {cache_key}")
        # else:
        #     print(f"Cache miss for key: {cache_key}")
        return value

    def set_key_value(self, cache_key: str, value):
        self.cache.set(cache_key, value)
        # print(f"Set cache key: {cache_key} with value: {value}")

    def clear_cache(self):
        self.cache.clear()


# TODO 如果后续生成过程改为多线程并发，需考虑数据竞争问题
cache = CacheUtils()