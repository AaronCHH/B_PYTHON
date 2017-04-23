#! /usr/bin/env python3.1
import fileinput, glob, sys, os

def main():
  if os.name == 'nt':
    if sys.path[0]:
      os.chdir(sys.path[0])
      input_filename = input("Name of input file:")
      input_list = glob.glob(input_filename)
      output_filename = input("Name of output file:")
      sys.stdout = open(output_filename, 'w')
    else:
      input_list = sys.argv[1:]
      for line in fileinput.input(input_list):
        if not line.startswith('##'):
          print(line, end="")
main()