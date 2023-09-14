#!/usr/bin/env python

from ppt_format import Ppt_Format
from pptx_format import Pptx_Format
from tools import Tools


def main():
    print(Tools.APP_NAME)
    in_dir, out_dir = Tools.parse_inputs()
    ppt_obj  = Ppt_Format(in_dir, out_dir)
    pptx_obj = Pptx_Format(in_dir, out_dir)

    return 0


if __name__ == "__main__":
    main() 