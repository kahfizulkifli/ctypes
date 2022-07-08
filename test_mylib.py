import mylib
import sys, platform
import ctypes, ctypes.util

# Get the path to the system C library
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

#Get string from mylib
string = mylib.get_address()
print(string)

#Create mutable string 
mut_str = ctypes.create_string_buffer(10)
mut_str = b'Kahfi:'
libc.puts(mut_str)

#Modify with input from ctypes
mut_str = mut_str + string
libc.puts(mut_str)