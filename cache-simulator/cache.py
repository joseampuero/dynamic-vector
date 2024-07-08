from collections import OrderedDict
from enums.unitStorage import UnitStorageEnum
from cacheLine import CacheLine
from enums.cacheLineState import CacheLineState

class Cache():
    def __init__(self, size, unitStorageEnum, lineSize, num_ways=1):
        self.size = size
        self.unitStorage = unitStorageEnum
        self.lineSize = lineSize
        self.numberLines = self.__numberOfLines()
        self.cache = OrderedDict()
        self.hits = 0
        self.misses = 0

    def __numberOfLines(self):
        lines = 0
        if self.unitStorage == UnitStorageEnum.B:
            lines = (self.size * 1) // self.lineSize 
        elif self.unitStorage == UnitStorageEnum.KB:
            lines = (self.size * 1024) // self.lineSize 
        elif self.unitStorage == UnitStorageEnum.MB:
            lines = (self.size * 1024 ** 2) // self.lineSize 
        elif self.unitStorage == UnitStorageEnum.GB:
            lines = (self.size * 1024 ** 3) // self.lineSize 

        return lines

    def read(self, address):
        index = (address // self.lineSize) % self.numberLines
        tag = address // (self.lineSize * self.numberLines)

        if index in self.cache and self.cache[index].tag == tag:
            # Cache hit
            self.hits += 1
            self.cache.move_to_end(index)  # Move to the end to mark as recently used
            return self.cache[index].data
        else:
            # Cache miss
            self.misses += 1
            if index in self.cache:
                self.cache.pop(index)
            self.cache[index] = CacheLine()
            self.cache[index].tag = tag
            self.cache[index].state = CacheLineState.EXCLUSIVE
            if len(self.cache) > self.numberLines:
                self.cache.popitem(last=False)
            return None

    def write(self, address, value):
        index = (address // self.lineSize) % self.numberLines
        tag = address // (self.lineSize * self.numberLines)

        if index in self.cache and self.cache[index].tag == tag:
            # Cache hit
            if self.cache[index].state == CacheLineState.SHARED:
                self.invalidateOtherCaches(address)
            self.cache[index].state = CacheLineState.MODIFIED
            self.cache[index].data = value
            self.hits += 1
            self.cache.move_to_end(index)  # Move to the end to mark as recently used
        else:
            # Cache miss
            self.misses += 1
            if index in self.cache:
                self.cache.pop(index)
            self.cache[index] = CacheLine()
            self.cache[index].tag = tag
            self.cache[index].state = CacheLineState.MODIFIED
            self.cache[index].data = value
            if len(self.cache) > self.numberLines:
                self.cache.popitem(last=False)

    def invalidateOtherCaches(self, address):
        # Implement invalidation logic for other caches in a multi-core setup
        pass

    def getStats(self):
        return self.hits, self.misses
