import constants

class TLB:
    def __init__(self, size=16, replacement_policy=constants.FIFO):
        self.size = size
        self.entries = {}
        self.replacement_policy = replacement_policy
        self.replacement_data = self._initReplacementData()

    def lookup(self, virtual_address):
        if virtual_address in self.entries:
            return self.entries[virtual_address]
        else:
            return None

    def update(self, virtual_address, physical_address):
        if self.size <= len(self.entries):
            self._applyReplacementPolicy()

        self.entries[virtual_address] = physical_address
        self._updateReplacementData(virtual_address)

    def _initReplacementData(self):
        if self.replacement_policy == constants.FIFO:
            return []
        elif self.replacement_policy == constants.LRU:
            return {}
        else:
            return []
    
    def _applyReplacementPolicy(self):
        if self.replacement_policy == constants.FIFO:
            oldestEntry = self.replacement_data.pop(0)
            del self.entries[oldestEntry]
        elif self.replacement_policy == constants.LRU:
            leastUsedEntry = min(self.replacement_data, key=self.replacement_data.get)
            del self.entries[leastUsedEntry]
            del self.replacement_data[leastUsedEntry]
        else:
            pass

    def _updateReplacementData(self, virtual_address):
        if self.replacement_policy == constants.FIFO:
            self.replacement_data.append(virtual_address)
        elif self.replacement_policy == constants.LRU:
            self.replacement_data[virtual_address]
            self.replacement_data[virtual_address] = self.replacement_data.get(virtual_address, 1) + 1
        else:
            pass