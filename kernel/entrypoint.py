import argparse

from utils.logger import Logger
from utils.StdinReader import StdinReaderGenerator, StdinReaderIterator


def parse_args():
    parser = argparse.ArgumentParser(description="Entrypoint Job")
    parser.add_argument("--job-to-run", required=False, help="Job to run")
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Unrecognized arguments: {unknown}")
    return args


def main():

    logger = Logger().get_logger()
    args = parse_args()
    logger.info(f"Args={args}")
    logger.info(f"job-to-run={args.job_to_run}")

    stdin_reader = StdinReaderIterator("Say something: ")
    for line in stdin_reader:
        if line.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        print(f"You said: {line}")


if __name__ == "__main__":
    main()
