EGZOPIX - digilat images analyzers
==================================

Concepts
--------

1. Extracting image detail concept

![Extracting image detail concept flow](https://raw.githubusercontent.com/bieli/egzopix__digital_images_analyzer/master/egzopix/solutions/extracting_image_detail/concept/extracting_image_detail.png)


HOW TO RUN ANALYZER
-------------------
```
$ git clone https://github.com/bieli/egzopix__digital_images_analyzer.git
$ cd egzopix__digital_images_analyzer/
$ python egzopix/analyzer.py -c=create_images_blocks_10x10 -i=/tmp/123.jpg -o=/tmp/image_blocks_10x10/ -v=DEBUG
[VERBOSE DEBUG MODE] concept: 'create_images_blocks_10x10' input: '<open file '/tmp/123.jpg', mode 'r' at 0x7f61f1c505d0>' output: '/tmp/image_blocks_10x10/' verbose: 'DEBUG' 
Hello, world !
CONCEPT: create_images_blocks_10x10
0x0
0x1
0x2
0x3
0x4
0x5
0x6
0x7
0x8
0x9
1x0
1x1
1x2
1x3
1x4
1x5
1x6
1x7
1x8
1x9
2x0
2x1
2x2
2x3
2x4
2x5
2x6
2x7
2x8
2x9
3x0
3x1
3x2
3x3
3x4
3x5
3x6
3x7
3x8
3x9
4x0
4x1
4x2
4x3
4x4
4x5
4x6
4x7
4x8
4x9
5x0
5x1
5x2
5x3
5x4
5x5
5x6
5x7
5x8
5x9
6x0
6x1
6x2
6x3
6x4
6x5
6x6
6x7
6x8
6x9
7x0
7x1
7x2
7x3
7x4
7x5
7x6
7x7
7x8
7x9
8x0
8x1
8x2
8x3
8x4
8x5
8x6
8x7
8x8
8x9
9x0
9x1
9x2
9x3
9x4
9x5
9x6
9x7
9x8
9x9

$ ls /tmp/image_blocks_10x10/
0x0.png  0x5.png  1x0.png  1x5.png  2x0.png  2x5.png  3x0.png  3x5.png  4x0.png  4x5.png  5x0.png  5x5.png  6x0.png  6x5.png  7x0.png  7x5.png  8x0.png  8x5.png  9x0.png  9x5.png
0x1.png  0x6.png  1x1.png  1x6.png  2x1.png  2x6.png  3x1.png  3x6.png  4x1.png  4x6.png  5x1.png  5x6.png  6x1.png  6x6.png  7x1.png  7x6.png  8x1.png  8x6.png  9x1.png  9x6.png
0x2.png  0x7.png  1x2.png  1x7.png  2x2.png  2x7.png  3x2.png  3x7.png  4x2.png  4x7.png  5x2.png  5x7.png  6x2.png  6x7.png  7x2.png  7x7.png  8x2.png  8x7.png  9x2.png  9x7.png
0x3.png  0x8.png  1x3.png  1x8.png  2x3.png  2x8.png  3x3.png  3x8.png  4x3.png  4x8.png  5x3.png  5x8.png  6x3.png  6x8.png  7x3.png  7x8.png  8x3.png  8x8.png  9x3.png  9x8.png
0x4.png  0x9.png  1x4.png  1x9.png  2x4.png  2x9.png  3x4.png  3x9.png  4x4.png  4x9.png  5x4.png  5x9.png  6x4.png  6x9.png  7x4.png  7x9.png  8x4.png  8x9.png  9x4.png  9x9.png


```

Output images example with background specific images blocks and important content:

![Images blocks 10x10](https://raw.githubusercontent.com/bieli/egzopix__digital_images_analyzer/master/egzopix/solutions/create_images_blocks/docs/image_blocks_10x10.png)


TODO
----
- [x] add conceptual image and first README
- [x] add HOW TO with first script arguments parser
- [x] add first runnable block code
- [ ] add travis CI
- [ ] add examples input images and outputs from analyzer
