from cache_utils import cache

# 计算缓存hash值，目前只考虑cookie和stoken，mid和stuid考虑为固定值
str = f'{cache.get_value("cookie")}-{cache.get_value("stoken")}' 
print(f'cookie_hash={hash(str)}')