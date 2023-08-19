#!/bin/bash
cd "$(dirname "$0")"
dir=$PWD
cd ../llama2.c
./run stories110M.bin 
cp output.txt "$dir/output.txt"
cd "$dir"
python ./create_post.py --content output.txt
python ./create_podcast.py
git add *
git commit -a -m "New Story"
git push
