import logging
import statistics


class RunnableBlock:
    MAGIC_REMOVE_BLOC_MEDIAN_LOW_LIMIT = 235

    def __init__(self, last_runnable_instance=None, logger=logging, **args):
        self.last_runnable_instance = last_runnable_instance
        self.logger = logger
        self.args = args

    def run(self, last_output_data={}):
        self.logger.debug(f'self.args: {self.args}')
        output_data = {}
        for block_position, block_stats in last_output_data.items():
            # self.logger.debug(f"block_position: {str(block_position)}")
            # self.logger.debug(f"block_stats: {str(block_stats)}")
            # TODO: check harmonic_mean metric
            median_from_block = statistics.median(block_stats['image_stats']['mean'])
            output_data[block_position] = {
                'median_from_block': median_from_block,
                'block_to_remove': self.__is_block_to_remove(median_from_block)
            }
            #self.logger.debug(f"output_data[block_position]: {str(output_data[block_position])}")
        # self.logger.debug(f"output_data: {str(output_data)}")
        return output_data

    def __is_block_to_remove(self, median):
        return median > self.MAGIC_REMOVE_BLOC_MEDIAN_LOW_LIMIT
