import argparse
import logging
import sys

import runner


def get_args():
    parser = argparse.ArgumentParser(description="EGZOPIX - digilat images analyzers.")
    parser.add_argument("-c", "--concept", type=str, help="concept name")
    parser.add_argument(
        "-i", "--input", type=argparse.FileType("r"), help="input original image path"
    )
    parser.add_argument("-o", "--output", type=str, help="output changed image(s) path")
    parser.add_argument(
        "-v",
        "--verbose",
        type=str,
        default="INFO",
        help="verbose level [DEBUG|INFO|WARNING|ERROR] (default: INFO)",
    )
    parser.add_argument(
        "-rp",
        "--runner_plan",
        type=str,
        default="create_images_blocks2,blocks_stats,remove_background",
        help="runner plan of transformations (default: "
        "read input image "
        "-> convert to blocks 10x10 "
        "-> get image histogram "
        "-> cut background based on histogram results)",
    )

    return parser.parse_args()


def get_logger(arguments):
    if arguments.verbose == "DEBUG":
        log_level = logging.DEBUG
    elif arguments.verbose == "INFO":
        log_level = logging.INFO
    elif arguments.verbose == "WARNING":
        log_level = logging.WARNING
    elif arguments.verbose == "ERROR":
        log_level = logging.ERROR
    else:
        log_level = logging.INFO

    logging.basicConfig(level=log_level, stream=sys.stdout)

    logging.info(
        f"concept: '{arguments.concept}', input: '{arguments.input.name}', output: '{arguments.output}', "
        f"verbose: '{arguments.verbose}', runner_plan: {arguments.runner_plan} "
    )
    return logging


if __name__ == "__main__":
    args = get_args()
    logger = get_logger(args)

    logging.info("--- STARTing egzopix processing ...")
    runner_instance = runner.Runner(
        logger=logger,
        concept=args.concept,
        input=args.input,
        output=args.output,
        verbose=args.verbose,
        runner_plan=args.runner_plan,
    )
    last_output_data, last_module_name = runner_instance.run()

    logging.info("\n--- RESULTS from processing:")
    for pos, item in last_output_data[last_module_name].items():
        if not item["block_to_remove"]:
            logger.info(f"+++ pos: {str(pos)}:")

    logger.debug(f"FINAL: last_output_data: {str(last_output_data)}")
    logging.info("--- STOP egzopix processing.")
