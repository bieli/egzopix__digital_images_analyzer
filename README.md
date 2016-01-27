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
[VERBOSE MODE] concept: 'create_images_blocks_10x10' input: '<open file '/tmp/123.jpg', mode 'r' at 0x7f94ff2070c0>' output: '/tmp/image_blocks_10x10/' verbose: 'DEBUG' 
Hello, world !

```

TODO
----
- [x] add conceptual image and first README
- [x] add HOW TO with first script arguments parser
- [ ] add first runnable block code
- [ ] add travis CI
- [ ] add examples input images and outputs from analyzer
