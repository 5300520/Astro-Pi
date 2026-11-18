import importlib.util
from exif import Image 
from time import sleep
from picamzero import Camera
i = 0
name = "json"
if importlib.util.find_spec(name) is not None:
    print("can use json")

def Take_Pictures():
    i + 1
    cam = Camera()
    cam.take_photo(f"image_{i:02d}.jpg")
    sleep(10)
for t in range(1):
    Take_Pictures()
    print(f"iteration:{t}")
