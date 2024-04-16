command = "pip install mmap"
import os
os.system(command)
import threading
import mmap

mutex_name = "ROBLOX_singletonMutex"
shm = mmap.mmap(-1, len(mutex_name)+1, tagname=mutex_name, access=mmap.ACCESS_WRITE)
mutex = threading.Lock()

while True:
    mutex.acquire()
    print("Mutex acquired")
