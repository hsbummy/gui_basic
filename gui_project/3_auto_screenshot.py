import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1,11):
    img = ImageGrab.grab()
    img.save("image{0}.png".format(i))
    time.sleep(2)