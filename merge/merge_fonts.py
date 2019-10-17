#!/usr/bin/env python3
#
# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Merges fonts.
Two notable differences between merge_noto and this script are:
1. merge_noto merges all fonts in Noto, or merges a subset of Noto
   clustered by region. While This script merges a selected font subset.
2. The line metrics in the final merged font are substituted by those in
   NotoSans-Regular.ttf (LGC). This is to optimize the user experience in LGC.
   The drawback is some tall scripts in the file list (like Balinese, Cuneiform,
  Javaness) might vertically overlap with each other and also be clipped by the
  edge of the UI. This should be handled carefully by the UI designer, say
  changing the line height or adding the margin.


Sample Usage:
    $ merge_fonts.py -d noto-fonts/unhinted -o NotoSansMerged-Regular.ttf

"""
import sys
import os.path
import logging
from argparse import ArgumentParser
import yaml

from fontTools import ttLib
from fontTools import merge
from merge_noto import add_gsub_to_font, has_gsub_table
from nototools.substitute_linemetrics import read_line_metrics, set_line_metrics
from fontTools.misc.loggingTools import Timer

log = logging.getLogger("nototools.merge_fonts")


def main():
    t = Timer()
    parser = ArgumentParser()
    parser.add_argument('-f', '--files',
        help='Path to YAML file containing paths to the fonts')
    parser.add_argument('-o', '--output', default='merged.ttf',
        help='Path to output file.')
    parser.add_argument('-v', '--verbose', action='store_true',
        help='Verbose mode, printing out more info')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING)

    if not args.files: 
        print('add -h for usage')
        sys.exit(2)

    with open(args.files, 'r') as stream:
        try:
            valid_files = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    if len(valid_files) <= 1:
        log.warn('expecting at least two fonts to merge, but only got %d '
            + 'font(s).', len(valid_files))
        sys.exit(-1)

    for idx, file in enumerate(valid_files):
        if not has_gsub_table(file):
            log.info('adding default GSUB table to %s.' % file)
            valid_files[idx] = add_gsub_to_font(file)

    merger = merge.Merger()
    print('Merging %d Fonts...' % len(valid_files))
    font = merger.merge(valid_files)
    # Use the line metric in the first font to replace the one in final result.
    metrics = read_line_metrics(ttLib.TTFont(valid_files[0]))
    set_line_metrics(font, metrics)
    font.save(args.output)
    font.close()

    print('%d fonts are merged. Cost %0.3f s.' % (len(valid_files), t.time()))
    print('Please check the result at %s.' % os.path.abspath(
        os.path.realpath(args.output)))


if __name__ == '__main__':
    main()
