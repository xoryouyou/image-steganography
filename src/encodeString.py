import argparse
import Image

from functions.binary import hideASCII
from functions.binary import showASCII
from functions.mask import encode
from functions.mask import decode



if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('-m', '--message', required=True, action='store', help='Message string to be hidden in the target')
    arg.add_argument('-t', '--target', required=True, action='store', help='Target image on which the mask shall be applied')
    arg.add_argument('-o', '--output', required=True, action='store', help='Output image name')
    args = vars(arg.parse_args())

    img = hideASCII(args['message'], Image.open(args['target']))
    img.save(args['output'])




    #hidden = hideASCII("Hello World!")
    #showASCII(hidden)

    #img = hide(Image.open("../img/message.png"), Image.open("../img/background.png"))
    #decoded = decode(img)
    #decoded.show()
    #img.save("../img/output2.png")