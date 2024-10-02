#!/bin/sh

current_dir=$(basename "$PWD")

    cd ..
    rm -rf "$current_dir"
    
    git clone https://www.github.com/wanqiuZzz/file
    cd
    cd file
    bash req.sh
    python3 main.py
else
    echo "取消。"
fi