#! /usr/bin/env python3.1
import fileinput, glob, sys, os
def main():
  if os.name == 'nt':
    sys.argv[1:] = glob.glob(sys.argv[1])
    for line in fileinput.input():
        if not line.startswith('##'):
              print(line, end="")
main()
