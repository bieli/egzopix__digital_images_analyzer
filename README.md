# EGZOPIX - digital images analyzers

This is experimental project and non-production ready.

We would like to check a few web services techniques in this PoC on example image manipulation solution.

## Concepts to check with this project

1. Extracting image detail using simple statistics methods
2. Reusable building blocks for image transformations
3. Experiments with LOW-CODE user interface for image modification/extraction/processing 

### Example transformation process

![Extracting image detail concept flow](https://raw.githubusercontent.com/bieli/egzopix__digital_images_analyzer/master/concept/extracting_image_detail.png)

### LOW-CODE transformation concept

![LOW-CODE transformation concept](https://raw.githubusercontent.com/bieli/egzopix__digital_images_analyzer/master/concept/extracting_image_lowcode.png)


## How to run analyzer
```
$ git clone https://github.com/bieli/egzopix__digital_images_analyzer.git

$ cd egzopix__digital_images_analyzer/

$ python egzopix/analyzer.py -rp create_images_blocks,blocks_stats,remove_background -v INFO -i ./egzopix/samples/images/image_test.0.png -o /tmp/image_blocks_10x10
INFO:root:concept: 'None', input: './egzopix/samples/images/image_test.0.png', output: '/tmp/image_blocks_10x10', verbose: 'INFO', runner_plan: create_images_blocks,blocks_stats,remove_background 
INFO:root:--- STARTing egzopix processing ...
INFO:root:Run module_name: create_images_blocks
INFO:root:Run module_name: blocks_stats
INFO:root:Run module_name: remove_background
INFO:root:
--- RESULTS from processing:
INFO:root:+++ pos: (3, 4):
INFO:root:+++ pos: (3, 5):
INFO:root:+++ pos: (4, 3):
INFO:root:+++ pos: (4, 4):
INFO:root:+++ pos: (4, 5):
INFO:root:+++ pos: (4, 6):
INFO:root:+++ pos: (5, 3):
INFO:root:+++ pos: (5, 4):
INFO:root:+++ pos: (5, 5):
INFO:root:+++ pos: (5, 6):
INFO:root:+++ pos: (6, 4):
INFO:root:+++ pos: (6, 5):
INFO:root:--- STOP egzopix processing.

# review temporary catalog with images blocks
$ ls /tmp/image_blocks_10x10/
0x0.png  0x5.png  1x0.png  1x5.png  2x0.png  2x5.png  3x0.png  3x5.png  4x0.png  4x5.png  5x0.png  5x5.png  6x0.png  6x5.png  7x0.png  7x5.png  8x0.png  8x5.png  9x0.png  9x5.png
0x1.png  0x6.png  1x1.png  1x6.png  2x1.png  2x6.png  3x1.png  3x6.png  4x1.png  4x6.png  5x1.png  5x6.png  6x1.png  6x6.png  7x1.png  7x6.png  8x1.png  8x6.png  9x1.png  9x6.png
0x2.png  0x7.png  1x2.png  1x7.png  2x2.png  2x7.png  3x2.png  3x7.png  4x2.png  4x7.png  5x2.png  5x7.png  6x2.png  6x7.png  7x2.png  7x7.png  8x2.png  8x7.png  9x2.png  9x7.png
0x3.png  0x8.png  1x3.png  1x8.png  2x3.png  2x8.png  3x3.png  3x8.png  4x3.png  4x8.png  5x3.png  5x8.png  6x3.png  6x8.png  7x3.png  7x8.png  8x3.png  8x8.png  9x3.png  9x8.png
0x4.png  0x9.png  1x4.png  1x9.png  2x4.png  2x9.png  3x4.png  3x9.png  4x4.png  4x9.png  5x4.png  5x9.png  6x4.png  6x9.png  7x4.png  7x9.png  8x4.png  8x9.png  9x4.png  9x9.png
```


### Input example image

![Input image](https://raw.githubusercontent.com/bieli/egzopix__digital_images_analyzer/master/egzopix/samples/images/image_test.0.png)


### Temporary images blocks

![Images blocks 10x10](https://raw.githubusercontent.com/bieli/egzopix__digital_images_analyzer/master/egzopix/samples/images/image_test.0.image_blocks_10x10.png)

### Results from processing - selected images blocks with dedicated (experimental) attributes (contains median values <= 235 from image stats module)
```bash
INFO:root:+++ pos: (3, 4):
INFO:root:+++ pos: (3, 5):
INFO:root:+++ pos: (4, 3):
INFO:root:+++ pos: (4, 4):
INFO:root:+++ pos: (4, 5):
INFO:root:+++ pos: (4, 6):
INFO:root:+++ pos: (5, 3):
INFO:root:+++ pos: (5, 4):
INFO:root:+++ pos: (5, 5):
INFO:root:+++ pos: (5, 6):
INFO:root:+++ pos: (6, 4):
INFO:root:+++ pos: (6, 5):
```


## TODO / WISH LIST

- [x] add conceptual image and first README
- [x] add HOW TO with first script arguments parser
- [x] add first runnable block code
- [x] add examples input images and outputs from analyzer
- [x] add full example with a few functional modules and sample image
- [x] refactoring first simple version to modular solutions
- [ ] use [Taskler | https://github.com/bieli/Taskler] to chaining proccess
- [ ] add unit tests and CI configuration
- [ ] add user interface, where it will be possible image transformations with LOW-CODE idea PoC
- [ ] add dedicated service/backends for LOW-CODE PoC
