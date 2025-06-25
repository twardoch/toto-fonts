#!/usr/bin/env bash
dir=${0%/*}; if [ "$dir" = "$0" ]; then dir="."; fi; cd "$dir";

mkdir -p yaml;
f='sans-reg'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
f='sans-ita'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
f='sans-bol'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
f='sans-bolita'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
f='serif-reg'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
f='serif-ita'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
f='serif-bol'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
f='serif-bolita'; find ../ttf/$f -iname "*.ttf" | while read p; do echo "- $p" >> yaml/$f.yaml; done; ./sort_fonts.py yaml/$f.yaml;
