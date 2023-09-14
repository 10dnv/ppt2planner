#!/usr/bin/env python
from pptx import Presentation
from tools import RetVal
import os

class Pptx_Format():
    def __init__(self, in_path, out_path) -> None:
         self.input_dir = in_path
         self.output_dir = out_path

    def CountFiles(self):
         dir_list = os.listdir(self.input_dir)
         dir_list_pptx = [file for file in dir_list if file.endswith(".pptx")]
         return len(dir_list_pptx)
    
    def ListFiles(self):
         dir_list = os.listdir(self.input_dir)
         dir_list_pptx = [file for file in dir_list if file.endswith(".pptx")]
         return dir_list_pptx
    
    def ProcessFiles(self):
        retVal = RetVal.ERROR
         
        if self.CountFiles() == 0:
            print("ERROR: Skipping PPTX processing, no files found!")
            return retVal
        
        pptx_file_list = self.ListFiles()
        
        for file_name in pptx_file_list:
            input_file = open(self.input_dir  + file_name, "rb")
            prs = Presentation(input_file)


        return retVal