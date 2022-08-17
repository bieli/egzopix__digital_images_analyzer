import logging

from PIL import Image, ImageStat


class RunnableBlock:
    def __init__(self, last_runnable_instance=None, logger=logging, **args):
        self.last_runnable_instance = last_runnable_instance
        self.logger = logger
        self.args = args

    def run(self, last_output_data={}):
        self.logger.debug(f"self.args: {self.args}")
        output_data = {}
        for block_position, block_data_path in last_output_data.items():
            # self.logger.debug(f"block_position: {str(block_position)}")
            # self.logger.debug(f"block_data_path: {str(block_data_path)}")
            img_block = Image.open(block_data_path)
            img_stats = ImageStat.Stat(img_block)
            output_data[block_position] = {
                "histogram": img_block.histogram(),
                "image_stats": {
                    "count": img_stats.count,
                    "extrema": img_stats.extrema,
                    "sum": img_stats.sum,
                    "mean": img_stats.mean,
                    "median": img_stats.median,
                    "rms": img_stats.rms,
                    "sum": img_stats.sum2,
                    "var": img_stats.var,
                    "stddev": img_stats.stddev,
                },
            }
            # self.logger.debug(f"output_data[block_position]: {str(output_data[block_position])}")
        # self.logger.debug(f"output_data: {str(output_data)}")
        return output_data
