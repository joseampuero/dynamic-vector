from pageTableEntry import PageTableEntry

class PageTable:
    def __init__(self):
        self.entries = {}

    def update(self, virtual_address, physical_address):
        self.entries[virtual_address] = PageTableEntry(virtual_address, physical_address)

    def lookup(self, virtual_address):
        return self.entries.get(virtual_address, None)

    def __repr__(self):
        return "\n".join([str(entry) for entry in self.entries.values()])