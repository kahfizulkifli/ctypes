import sys, platform
import ctypes, ctypes.util
import numpy.ctypeslib as ctl

# Find lib and load
# mylib_path = ctypes.util.find_library('./mylib')
# if not mylib_path:
#     print("Can't find lib")
#     sys.exit()

# try:
#     mylib = ctypes.CDLL(mylib_path)
# except OSError:
#     print("Can't find C library")
#     sys.exit()

test_library = ctl.load_library('libcachemanager.so', "/mnt/c/Users/Kahfi Zulkifli/GIK Lab/ctypes/mylib")

if platform.system() == "Windows":
    path_libc = ctypes.util.find_library("msvcrt")
else:
    path_libc = ctypes.util.find_library("c")
# Get a handle to the sytem C library
try:
    libc = ctypes.CDLL(path_libc)
except OSError:
    print("Unable to load the system C library")
    sys.exit()

test_empty = test_library.test_empty

test_add = test_library.test_add
test_add.argtypes = [ctypes.c_float, ctypes.c_float]
test_add.restype = ctypes.c_float

test_passing_array = test_library.test_passing_array
test_passing_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
test_passing_array.restype = None

get_address = test_library.get_address
get_address.argtypes = None
get_address.restype = ctypes.c_char_p