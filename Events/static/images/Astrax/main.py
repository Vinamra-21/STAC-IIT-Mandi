import os
from PIL import Image

for i in os.listdir():
    try:
        if i != 'main.py':
            p = f'./{i}'
            img = Image.open(p)
            img.save(p, optimize=True, quality=90)
    except IsADirectoryError:
        pass
