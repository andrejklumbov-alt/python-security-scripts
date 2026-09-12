import re

dirty_text = "Логин admin, хэш: HASH_1a2b3c4d, логин moderator, хэш: HASH_9e8f7d6c, а хэш HASH_123 — битый"


reg = r"HASH_([a-z0-9]{8})"
res = re.findall(reg, dirty_text)
print(res)