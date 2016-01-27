#!/usr/bin/python3.4

import Image
import logging

module_logger = logging.getLogger('spam_application.auxiliary')

class RunnableBlock:
  def __init__(self, infile, output_dir='/tmp'):
    self.infile = infile
    self.output_dir = output_dir
    self.logger = logging.getLogger('solutions.create_images_blocks.module.RunnableBlock')
    self.img = Image.open(infile)
    log = "[__init__] infile: '{}', output_dir: '{}'".format(
          infile,
          output_dir,
          )
    self.logger.debug(log)

    self.imgwidth, self.imgheight = self.img.size
    log = "[__init__] imgwidth: '{}', imgheight: '{}'".format(
          self.imgwidth,
          self.imgheight,
          )
    self.logger.debug(log)

  def run(self):
    for x in xrange(0, 10):
      for y in xrange(0, 10):
        print str(x) + "x" + str(y)
        tmp_output_img = self.img.crop(self._get_coordinates(x, y, self.imgwidth, self.imgheight))
        tmp_output_img.save(self.output_dir + "/%sx%s.png" % (x, y), 'png')

  def _get_coordinates(self, x, y, imgwidth, imgheight, block_size_percent=10.0):
    block_size_percent *= 0.01
    dx = int(imgwidth * block_size_percent)
    dy = int(imgheight * block_size_percent)  
    dx2 = dx * (x + 1) - 1
    dy2 = dy * (y + 1) - 1  

    if dx2 >= imgwidth - 10:
      dx2 = imgwidth

    if dy2 >= imgheight - 10:
      dy2 = imgheight

    return (dx * x, dy * y, dx2, dy2)

