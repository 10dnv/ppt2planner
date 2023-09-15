#!/usr/bin/env python

import os

class Ppt_Format:
    def __init__(self, in_path, out_path) -> None:
        self.input_dir = in_path
        self.output_dir = out_path

    def CountFiles(self):
         dir_list = os.listdir(self.input_dir)
         dir_list_pptx = [file for file in dir_list if file.endswith(".ppt")]
         return len(dir_list_pptx)
    
    def ListFiles(self):
         dir_list = os.listdir(self.input_dir)
         dir_list_pptx = [file for file in dir_list if file.endswith(".ppt")]
         return dir_list_pptx