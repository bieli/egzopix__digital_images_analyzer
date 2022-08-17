import os
import logging

from PIL import Image


class RunnableBlock:
    def __init__(self, last_runnable_instance=None, **args):
        self.infile = args["input"].name
        self.output_dir = args["output"]
        self.from_module_instance = last_runnable_instance
        self.logger = logging.getLogger("solutions.create_images_blocks.RunnableBlock")
        self.img = Image.open(self.infile)
        log = "[__init__] infile: '{}', output_dir: '{}'".format(
            self.infile,
            self.output_dir,
        )
        self.logger.debug(log)

        self.imgwidth, self.imgheight = self.img.size
        log = "[__init__] imgwidth: '{}', imgheight: '{}'".format(
            self.imgwidth,
            self.imgheight,
        )
        self.logger.debug(log)

        try:
            os.mkdir(self.output_dir)
        except OSError as err:
            if "exists" not in str(err):
                self.logger.error(f"Output directory creation error: {err!r}")

    def run(self, last_output_data={}, output_image_format="png"):
        output_data = {}
        for x in range(0, 10):
            for y in range(0, 10):
                block_name = str(x) + "x" + str(y)
                # TODO: check why output_image_format is dict here
                block_file_path = f"{self.output_dir}/{x}x{y}.png"
                self.logger.debug(f"Processing block: {block_name}")
                self.logger.debug(f"block_file_path: {block_file_path}")
                tmp_output_img = self.img.crop(
                    self._get_coordinates(x, y, self.imgwidth, self.imgheight)
                )
                tmp_output_img.save(block_file_path, output_image_format)
                output_data[(x, y)] = block_file_path
        self.logger.debug(f"output_data: {str(output_data)}")
        return output_data

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

        return dx * x, dy * y, dx2, dy2
