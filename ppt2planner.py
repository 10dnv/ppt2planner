#!/usr/bin/env python

import argparse
import os

APP_NAME = "Powerpoint to planner"

def main():
    print(APP_NAME)
    parse_inputs()
    return 0


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def parse_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type = dir_path, required = True, help = "Input directory containing ppt/pptx files")
    parser.add_argument('-o', '--output', type = dir_path, required = True, help = "Output directory for the converted files")
    args = parser.parse_args()

    print(args.input)

if __name__ == "__main__":
    main() 