import argparse
import Image

from functions.binary import hideASCII
from functions.binary import showASCII
from functions.mask import encode
from functions.mask import decode



if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--image', required=True, action='store', help='Image which will be decoded')
    args = vars(arg.parse_args())

    showASCII(Image.open(args['image']))




    #hidden = hideASCII("Hello World!")
    #showASCII(hidden)

    #img = hide(Image.open("../img/message.png"), Image.open("../img/background.png"))
    #decoded = decode(img)
    #decoded.show()
    #img.save("../img/output2.png")