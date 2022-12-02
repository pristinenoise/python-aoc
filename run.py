import os
from glob import glob1
import sys
from shutil import copyfile
import requests
from datetime import date
import logging
from argparse import ArgumentParser

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(funcName)s: %(message)s",
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--day", default=date.today().day, type=int)
    parser.add_argument("-y", "--year", default=date.today().year, type=int)
    parser.add_argument("-l", "--language", default=["py"], nargs="+")
    args = parser.parse_args()

    directory = f"year{args.year}/day{args.day:02d}"
    os.system(f"python {directory}/solver.py")
