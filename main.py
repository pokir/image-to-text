import os
import PIL
from PIL import Image
import sys


#characters = '.\'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
characters = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'

try:
    image_path = sys.argv[1]
except IndexError:
    image_path = input('Image path: ')

try:
    width, height = os.get_terminal_size()

    with Image.open(image_path) as im:
        #resized = ImageOps.scale(im, width / im.size[0])

        # resize aspect ratio for text output
        # (height of characters is twice the width, so divide height by 2)
        resized = im.resize((width, int(0.5 * im.size[1] * width / im.size[0])))

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

with open('output.txt', 'w') as f:
    f.write(buffer)
