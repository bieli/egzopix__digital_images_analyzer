#!/usr/bin/python3.4

import argparse
import logging

parser = argparse.ArgumentParser(description='EGZOPIX - digilat images analyzers.')
parser.add_argument('-c', '--concept', type=str, 
                    help='concept name')
parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                   help='input original image path')
parser.add_argument('-o', '--output', type=str,
                   help='output changed image(s) path')
parser.add_argument('-v', '--verbose', type=str, default='INFO',
                   help='verbose level [DEBUG|INFO|WARNING|ERROR] (default: INFO)')

args = parser.parse_args()

if args.verbose == 'DEBUG':
  log_level=logging.DEBUG
elif args.verbose == 'INFO':
  log_level=logging.INFO
elif args.verbose == 'WARNING':
  log_level=logging.WARNING
elif args.verbose == 'ERROR':
  log_level=logging.ERROR
else:
  log_level=logging.INFO

logging.basicConfig(filename='analyzer.log',level=log_level)

# logging.debug('This message should go to the log file DEBUG')
# logging.info('So should this INFO')
# logging.warning('And this, too WARNING')

if args.verbose and args.verbose == 'DEBUG':
  log = "[VERBOSE DEBUG MODE] concept: '{}' input: '{}' output: '{}' verbose: '{}' ".format(
        args.concept,
        args.input,
        args.output,
        args.verbose
        )
  print(log)
  logging.debug(log)

print("Hello, world !")


if args.concept == 'create_images_blocks_10x10':
  print("CONCEPT: create_images_blocks_10x10")
  from solutions.create_images_blocks.module import RunnableBlock

  rb = RunnableBlock(args.input, args.output)
  rb.run()
else:
  raise ValueError('Unknown concept')

