class TLBEntry:
    def __init__(self, virtual_address, physical_address, valid, modified, lru):
        self.virtual_address = virtual_address
        self.physical_address = physical_address
        self.valid = valid
        self.modified = modified
        self.lru = lru

    def __repr__(self):
        return (f"TLBEntry(Virtual: {self.virtual_address}, Physical: {self.physical_address}, "
                f"Valid: {self.valid}, Modified: {self.modified}, LRU: {self.lru})")
