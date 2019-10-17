#!/usr/bin/env bash
dir=${0%/*}; if [ "$dir" = "$0" ]; then dir="."; fi; cd "$dir";

mkdir -p ../ttf_merged
python3 ./merge_fonts.py -f sans-reg-basic.yaml -o ../ttf_merged/sans-reg-basic.ttf
python3 ./merge_fonts.py -f serif-bol.yaml -o ../ttf_merged/serif-bol.ttf
python3 ./merge_fonts.py -f serif-reg.yaml -o ../ttf_merged/serif-reg.ttf
python3 ./merge_fonts.py -f sans-bol.yaml -o ../ttf_merged/sans-bol.ttf
#python3 ./merge_fonts.py -f sans-reg.yaml -o ../ttf_merged/sans-reg.ttf
echo "OK"
