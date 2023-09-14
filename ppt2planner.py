#!/usr/bin/env python

from ppt_format import Ppt_Format
from pptx_format import Pptx_Format
from tools import Tools, RetVal



def main():
    in_dir, out_dir = Tools.parse_inputs()
    ppt_obj  = Ppt_Format(in_dir, out_dir)
    pptx_obj = Pptx_Format(in_dir, out_dir)

    #Printing Hello message
    print(Tools.APP_NAME)

    #PPTX files
    print(f"Looking for files inside: {in_dir}")
    number_pptx = pptx_obj.CountFiles()
    print(f"PPTX files found: {number_pptx}")
    pptx_obj.ProcessFiles()

    return 0


if __name__ == "__main__":
    main() 