import argparse
import Image

from functions.binary import decode

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--image', required=True, action='store', help='Image which will be decoded')
    args = vars(arg.parse_args())

    decode(Image.open(args['image']))
