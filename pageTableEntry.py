class PageTableEntry:
    def __init__(self, virtual_address, physical_address, present=True):
        self.virtual_address = virtual_address
        self.physical_address = physical_address
        self.valid = present

    def __repr__(self):
        return f"PageTableEntry(Virtual: {self.virtual_address}, Physical: {self.physical_address}, Valid: {self.valid})"
