#!/usr/bin/env python3
import sys
import os.path
import yaml
from fontTools import ttLib

try: 
    y = sys.argv[1]
except: 
    print('provide YAML file path')
    sys.exit(2)

files = None
with open(y, 'r') as stream:
    try:
        files = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if files: 
    psort = {}
    for p in files:
        u2n = None
        ttx = ttLib.TTFont(p)
        cmap = ttx["cmap"].getcmap(3,10)
        if not cmap:
            cmap = ttx["cmap"].getcmap(3,1)
        if not cmap:
            cmap = ttx["cmap"].getcmap(0,4)
        if not cmap:
            cmap = ttx["cmap"].getcmap(0,3)
        if cmap:
            u2n = dict((u,n) for u, n in cmap.cmap.items() if u not in range(0xE000, 0xF8FF + 1))
        if u2n: 
            us = list(u2n.keys())
            repru = us[int(len(us) * 0.5)]
            psort[p] = repru
    psort = sorted(psort, key=psort.get)
    with open(y, 'w') as stream:
        try:
            yaml.safe_dump(psort, stream)
        except yaml.YAMLError as exc:
            print(exc)
