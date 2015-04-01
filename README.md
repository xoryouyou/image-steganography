# image-steganography

This is an example implementation of image stegnography in python.

It allows you to hide visual data in images in a way that the human eye cant detect.

## How to use 

For each de/encoding step I wrote a small argparse interface so it can be used via the commanline.

```
encodeMask.py [-h] -m MESSAGE -t TARGET -o OUTPUT
decodeMask.py [-h] -i IMAGE
encodeString.py [-h] -m MESSAGE -t TARGET -o OUTPUT
decodeString.py [-h] -i IMAGE
```

## How it works

On a basic level its just a simple a binary en/decode which takes the input B/W image and maps each pixel to the lowest bit of the targets image red channel.


![](https://raw.githubusercontent.com/xoryouyou/image-steganography/gh-pages/images/graph.jpg)

## TODO

The string decoding needs some cleanup.
