#!/bin/bash
cd ../piper
cat $1 | ./piper --model /home/tony/piper/en_GB-alba-medium.onnx --output_file $1.wav
ffmpeg -i $1.wav $1.mp3
rm $1.wav
cp $1.mp3 ../storytime/media/
cd ../storytime
