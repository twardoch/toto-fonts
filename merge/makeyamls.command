#!/usr/bin/env bash
dir=${0%/*}; if [ "$dir" = "$0" ]; then dir="."; fi; cd "$dir";

f='sans-reg'; find ../ttf/$f/ -iname "*.ttf" | while read p; do echo "- $p" >> $f.yaml; done; ./sort_fonts.py $f.yaml;
f='sans-bol'; find ../ttf/$f/ -iname "*.ttf" | while read p; do echo "- $p" >> $f.yaml; done; ./sort_fonts.py $f.yaml;
f='serif-reg'; find ../ttf/$f/ -iname "*.ttf" | while read p; do echo "- $p" >> $f.yaml; done; ./sort_fonts.py $f.yaml;
f='serif-bol'; find ../ttf/$f/ -iname "*.ttf" | while read p; do echo "- $p" >> $f.yaml; done; ./sort_fonts.py $f.yaml;
