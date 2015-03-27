import random

def binary(message):
  string = ""

  for char in message:
    string += (bin(ord(char))[2:])
  string += '10101010'


  print("Encoded:%s" % string)
  for char in string:
    yield int(char)

  while True:
    yield(int(random.randrange(1)))



def setbit(byte, bit):
  return (byte | bit) if bit else (byte & 0xFE)


def encode(message, img):

  stream = binary(message)
  w, h = img.size

  for x in range(w):
    for y in range(h):

      r, g, b = img.getpixel((x, y))

      r = setbit(r, stream.next())
      g = setbit(g, stream.next())
      b = setbit(b, stream.next())

      img.putpixel((x, y), (r,g,b))

  return img


def decode(image):
  #branch here for image type ,path, etc
  message = ""

  w, h = image.size


  for x in range(w):
    for y in range(h):
      r, g, b = image.getpixel((x, y))

      message += str(r & 1) # get lsb
      message += str(g & 1) # get lsb
      message += str(b & 1) # get lsb


  offset = message.find("10101010")

  print("Offset:%i" % offset)
  message = message[:offset+8]
  print("Decoded:%s" % message)

  # chr(0b1101100)


