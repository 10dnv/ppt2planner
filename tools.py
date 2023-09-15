#!/usr/bin/env python

import argparse
import os

class RetVal():
    OK = 0
    ERROR = 1

class Settings():
    SONG_PREFIX = ""
    MIN_SENTENCE_LEN = 3
    ignored_keywords ={''}

class Tools:
    APP_NAME = "P O W E R P O I N T   T O   P L A N N E R"
    APP_VERSION = "1.0.0"

    def dir_path(string):
        if os.path.isdir(string):
            return string
        else:
            raise NotADirectoryError(string)
    
    def parse_inputs():
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input', type = Tools.dir_path, required = True, help = "Input directory containing ppt/pptx files")
        parser.add_argument('-o', '--output', type = Tools.dir_path, required = True, help = "Output directory for the converted files")
        args = parser.parse_args()

        return args.input, args.output