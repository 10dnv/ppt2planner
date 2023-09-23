#!/usr/bin/env python

import argparse
import os, sys

class RetVal():
    OK = 0
    ERROR = 1

class Settings():
    SONG_PREFIX = ""
    MIN_SENTENCE_LEN = 3
    ignored_keywords ={}
    AUTHOR = ""

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
        parser.add_argument('-g', '--gui', action='store_true', default= False, help = "Start the program in GUI mode")
        parser.add_argument('-i', '--input',  type = Tools.dir_path, help = "Input directory containing ppt/pptx files")
        parser.add_argument('-o', '--output', type = Tools.dir_path, help = "Output directory for the converted files")
        args = parser.parse_args()

        #reject i/o if gui is rendered
        if args.gui == False:
            if args.input == None or args.output == None:
                print("ERROR: input -i DIR and output -o DIR args. are mandatoy in non-GUI mode!")
                sys.exit()

        return args.input, args.output, args.gui