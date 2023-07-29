#!/bin/bash
cd "$(dirname "$0")"
dir=$PWD

cd ../llama2.c
./run out44m/model44m.bin
cp output.txt "../$dir/output.txt"
cd "$dir"
python ./create_post.py --content output.txt
git add *
git commit -a -m "New Story"
git push

