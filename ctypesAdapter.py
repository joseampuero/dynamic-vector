import ctypes

# Funciones my_malloc y my_free
libc = ctypes.CDLL("libc.so.6")  # Ajusta según tu sistema operativo

c_int = ctypes.c_int

def malloc(size):
    print("Call malloc with size:", size)
    return libc.malloc(size)

def free(ptr):
    libc.free(ptr)

def sizeof(obj):
    return ctypes.sizeof(obj)

def memmove(newObj, oldObj, size):
    ctypes.memmove(newObj, oldObj, size)

def cast(obj, typ):
    return ctypes.cast(obj, typ)

def POINTER(typ):
    return ctypes.POINTER(typ)

def cast(address, typ):
    return ctypes.cast(address, POINTER(typ))