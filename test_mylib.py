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
libc.puts(string)

#Create mutable string 
mut_str = ctypes.create_string_buffer(b"Kahfi:", 20)

libc.puts(mut_str)

p = ctypes.cast(ctypes.addressof(mut_str)+6, ctypes.POINTER(ctypes.c_char))

libc.memmove(p, string, 15)

libc.puts(mut_str)
# libc.memset(mut_str, ctypes.c_wchar_p("K"), 1)
# libc.puts(mut_str)

# p = ctypes.cast(ctypes.addressof(mut_str) + 6, ctypes.POINTER(ctypes.c_char))

# libc.memset(p, string, 1)
# libc.puts(mut_str)

# p = ctypes.cast(ctypes.addressof(mut_str) + 6, ctypes.POINTER(ctypes.c_char))

# libc.memset(p, string, 1)

# libc.puts(mut_str)