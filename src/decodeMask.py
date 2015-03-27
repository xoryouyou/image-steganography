import argparse
import Image

from functions.mask import decode

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--image', required=True, action='store', help='Image which will be decoded')
    args = vars(arg.parse_args())

    img = decode(Image.open(args['image']))
    img.show()
