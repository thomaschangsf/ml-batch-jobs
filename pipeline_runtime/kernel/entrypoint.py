import argparse

from utils.logger import Logger


def parse_args():
    parser = argparse.ArgumentParser(description="Entrypoint Job")
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Unrecognized arguments: {unknown}")


def main():
    main_logger = Logger().get_logger()
    main_logger.info("main")


if __name__ == "__main__":
    main()
