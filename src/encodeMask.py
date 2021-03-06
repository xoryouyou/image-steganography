import argparse
import Image

from functions.mask import encode

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('-m', '--message', required=True, action='store', help='Message image to be hidden in the target')
    arg.add_argument('-t', '--target', required=True, action='store', help='Target image on which the mask shall be applied')
    arg.add_argument('-o', '--output', required=True, action='store', help='Output image name')
    args = vars(arg.parse_args())

    img = encode(Image.open(args['message']), Image.open(args['target']))
    img.save(args['output'])
