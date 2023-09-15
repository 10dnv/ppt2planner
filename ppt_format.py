#!/usr/bin/env python

import os
from tools import Tools, RetVal, Settings

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
    
    def ProcessFiles(self):
        retVal = RetVal.ERROR
            
        print("Processing ppt files...")
        if self.CountFiles() == 0:
            print("ERROR: Skipping PPT processing, no files found!")
            return retVal
        
        ppt_file_list = self.ListFiles()
        
        for i in range(0, len(ppt_file_list)):
        # for i in range(0, 1):
            print(f"    > File {i + 1}/{len(ppt_file_list)}", end='')
            print(" - DONE")

            #Extract song title
            song_title = Settings.SONG_PREFIX + ppt_file_list[i].split('.')[0]
            file_path =f"{self.input_dir}/{ppt_file_list[i]}"
            file_path = file_path.replace(' ', '\\ ')

            song_text = str(os.popen(f"tika --text {file_path}").read())
            # print(song_text)
