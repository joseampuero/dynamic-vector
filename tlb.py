from tlbEntry import TLBEntry

class TLB:
    def __init__(self, size=16):
        self.size = size
        self.entries = []
        self.lru_counter = 0

    def lookup(self, virtual_address):
        for entry in self.entries:
            if entry.virtual_address == virtual_address:
                entry.lru = self.lru_counter
                self.lru_counter += 1
                return entry
        return None

    def update(self, virtual_address, physical_address, modified):
        if self.size <= len(self.entries):
            self._applyReplacementPolicy()

        newEntry = TLBEntry(virtual_address, physical_address, True, modified, self.lru_counter)
        self.lru_counter += 1
        self.entries.append(newEntry)
    
    def _applyReplacementPolicy(self):
        leastRecentlyUsedEntry = min(self.entries, key=lambda entry: entry.lru)
        self.entries.remove(leastRecentlyUsedEntry)