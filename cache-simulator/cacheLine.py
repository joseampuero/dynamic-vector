from enums.cacheLineState import CacheLineState

class CacheLine:
    def __init__(self):
        self.tag = None
        self.state = CacheLineState.INVALID
        self.data = None