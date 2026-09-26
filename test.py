from lru_cache import Cache


cache = Cache(2)


cache.put("A",10)
cache.put("B",20)

cache.display()


cache.get("A")

cache.display()


cache.put("C",30)

cache.display()


cache.get("B")

cache.get("C")

cache.get("A")