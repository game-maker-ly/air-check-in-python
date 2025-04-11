from cache_utils import cache
import hashlib

# 计算缓存hash值，目前只考虑cookie和stoken，mid和stuid考虑为固定值
data = f'{cache.get_value("cookie")}-{cache.get_value("stoken")}' 
# print(data)
md5val = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
print(f'cookie_hash={md5val}')