#!/bin/bash

echo "Hiding mask image"
python ./src/encodeMask.py -m img/message.png -t img/background.png -o out.png
echo "Revealing mask image"
python ./src/decodeMask.py -i out.png
echo "Hiding string"
python ./src/encodeString.py -m 'this is a test'  -t img/background.png -o out2.png
echo "Revealing string"
python ./src/decodeString.py -i  out2.png
