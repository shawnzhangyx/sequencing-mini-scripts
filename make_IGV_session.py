#!/usr/env python
import sys
import glob 

argv = sys.argv

if len(argv)< 3: 
  print("Usage: python script.py genome baseurl outfile")
  exit(1)
genome = argv[1]
baseurl = argv[2]
outfile = argv[3]

with open(outfile,'w') as f:
  f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?> <Session genome="'+genome+'" hasGeneTrack="true" hasSequenceTrack="true" version="8">\n')
  f.write('  <Resources>\n')
  ## files 
  for sfile in sorted(glob.glob("*.bigWig")):
    f.write('    <Resource path="'+baseurl+"/" + sfile + '"/>\n')
  for sfile in sorted(glob.glob("*.bw")):
    f.write('    <Resource path="'+baseurl+"/" + sfile + '"/>\n')
  f.write('  </Resources>\n')
  f.write('</Session>\n')
