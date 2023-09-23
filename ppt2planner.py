#!/usr/bin/env python

from ppt_format import Ppt_Format
from pptx_format import Pptx_Format
from tools import Tools
from gui import Gui



def main():
    in_dir, out_dir, gui_en = Tools.parse_inputs()
    
    if gui_en == True:
        gui_obj = Gui()
        gui_obj.render()
    else:
        ppt_obj  = Ppt_Format()
        pptx_obj = Pptx_Format()
        ppt_obj.init(in_dir, out_dir)
        pptx_obj.init(in_dir, out_dir)

        #Printing Hello message
        print("\n" + Tools.APP_NAME)

        print(f"Looking for files inside: {in_dir}")

        number_pptx = pptx_obj.CountFiles()
        number_ppt  = ppt_obj.CountFiles()

        print(f"PPTX files found:  {number_pptx}")
        print(f"PPT files found:   {number_ppt}")
        print(f"Total input files: {number_ppt + number_pptx}\n")

        pptx_obj.ProcessFiles()
        ppt_obj.ProcessFiles()


    return 0


if __name__ == "__main__":
    main() 