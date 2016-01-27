#!/usr/bin/python3.4

import argparse

parser = argparse.ArgumentParser(description='EGZOPIX - digilat images analyzers.')
parser.add_argument('-c', '--concept', type=str, 
                    help='concept name')
parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                   help='input original image path')
parser.add_argument('-o', '--output', type=str,
                   help='outtput changed image(s) path')
parser.add_argument('-v', '--verbose', type=str, default='INFO',
                   help='verbose level [DEBUG|INFO|WARNING|ERROR] (default: INFO)')

args = parser.parse_args()

if args.verbose and args.verbose == 'DEBUG':
  print("[VERBOSE MODE] concept: '{}' input: '{}' output: '{}' verbose: '{}' ".format(
         args.concept,
         args.input,
         args.output,
         args.verbose
         ))

print("Hello, world !")

