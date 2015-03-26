import Image
import random

def encode(message, image):
  w, h = message.size

  for x in range(w):
    for y in range(h):

      input = message.getpixel((x, y))[0]  # get the red pixel
      original = image.getpixel((x, y))
      if input == 255:  # if input mask
        image.putpixel((x, y), (original[0] | 1, original[1], original[2]))   # set pixel
      else:
        image.putpixel((x, y), (original[0] & 0xFE, original[1],original[2])) # unset pixel
  return image

def decode(source):
  new = Image.new('RGB', source.size)

  w, h = source.size

  for x in range(w):
    for y in range(h):
      red = source.getpixel((x,y))[0]
      if red & 1 == 1:
        new.putpixel((x,y),(255,255,255))
    else:
        new.putpixel((x,y), (0,0,0))

  return new