#!/usr/bin/env python

import os
from tools import RetVal, Settings

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

            #Extract song text using tika
            song_text = str(os.popen(f"tika --text {file_path}").read())

            #Open output file
            output_file = open(f"{self.output_dir}/{song_title}.txt", "w+",encoding="utf-8")

            all_lines = []

            # print(f"{{title: {song_title}}}\n")
            all_lines.append(f"{{title: {song_title}}}\n")

            prev_line =""
            verse = 1
            # print(f"\n{{comment: Verse {verse}}}")
            all_lines.append(f"\n{{comment: Verse {verse}}}")
            verse += 1

            for line in song_text.split("\n"):
                if  line == "" and prev_line =="":
                    continue
                elif line =="":
                    # print(f"\n{{comment: Verse {verse}}}")
                    all_lines.append(f"\n{{comment: Verse {verse}}}")
                    verse +=1
                else:
                    # print(line.strip())
                    #Filter for small words, like slide 1/3 and ignored words
                    if len(line.strip()) > Settings.MIN_SENTENCE_LEN and line.strip() not in Settings.ignored_keywords:
                        all_lines.append(line.strip())
                prev_line = line


            #Write lines into the output file
            for line in range(0, len(all_lines) - 1):
                output_file.write(all_lines[line] + '\n')

            #Close the output file
            output_file.close()
