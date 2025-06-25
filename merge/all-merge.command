#!/usr/bin/env bash
dir=${0%/*}; if [ "$dir" = "$0" ]; then dir="."; fi; cd "$dir";

mkdir -p ../ttf_merged
ls -1 yaml | while read y; do
	n=$(basename $y ".yaml");
	echo "# Merging $n..."
	python3 ./merge_fonts.py -f "yaml/$y" -o "../ttf_merged/$n.ttf";
done;
echo "# Done"
