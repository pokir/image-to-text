import os
import PIL
from PIL import Image
from PIL import ImageOps
import sys


#characters = '.\'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
characters = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'

try:
    image_path = sys.argv[1]
except IndexError:
    image_path = input('Image path: ')

try:
    width, _ = os.get_terminal_size()
    with Image.open(image_path) as im:
        #resized = im.resize((width, int(im.size[1] * im.size[0] / width)))
        resized = ImageOps.scale(im, width / im.size[0])

except (FileNotFoundError, PIL.UnidentifiedImageError):
    print(f'No image found at "{image_path}".')


pixels = resized.load()

buffer = ''
for y in range(resized.size[1]):
    for x in range(resized.size[0]):
        grayscale = sum(pixels[x, y][:-1]) / 3
        character = characters[int((len(characters) - 1) * grayscale / 255)]
        buffer += character
    buffer += '\n'

print(buffer)
