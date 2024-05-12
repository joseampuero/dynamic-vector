import ctypesAdapter

class DynamicVector:
    def __init__(self, initial_capacity=10):
        self._capacity = initial_capacity
        self._size = 0
        self._array = self._create_array(self._capacity)

    def _create_array(self, capacity):
        return ctypesAdapter.malloc(ctypesAdapter.sizeof(ctypesAdapter.c_int) * capacity)

    def _resize(self, new_capacity):
        print("resize with", new_capacity)
        new_array = ctypesAdapter.malloc(ctypesAdapter.sizeof(ctypesAdapter.c_int) * new_capacity)
        ctypesAdapter.memmove(new_array, self._array, ctypesAdapter.sizeof(ctypesAdapter.c_int) * self._size)
        ctypesAdapter.free(self._array)
        self._array = new_array
        self._capacity = new_capacity

    def push(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        ctypesAdapter.cast(self._array, ctypesAdapter.POINTER(ctypesAdapter.c_int))[self._size] = value
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty vector")
        self._size -= 1

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return ctypesAdapter.cast(self._array, ctypesAdapter.POINTER(ctypesAdapter.c_int))[index]

    def __len__(self):
        return self._size

    def __repr__(self):
        return "[" + ", ".join(str(self[i]) for i in range(self._size)) + "]"
