
import Image
import random



def hide(message, image):

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


def hideASCII(message):

  stream = binary(message)
  img = Image.open("img/background.png")
  w, h = img.size

  for x in range(w):
    for y in range(h):

      r, g, b = img.getpixel((x, y))

      r = setbit(r, stream.next())
      g = setbit(g, stream.next())
      b = setbit(b, stream.next())

      img.putpixel((x, y), (r,g,b))

  img.show()
  return img


def showASCII(image):
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

if __name__ == '__main__':
#  hidden = hideASCII("Hello World!")
#  showASCII(hidden)

  img = hide(Image.open("img/message.png"), Image.open("img/background.png"))
  decoded = decode(img)
  decoded.show()
  img.save("img/output2.png")



