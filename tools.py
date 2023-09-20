#!/usr/bin/env python

import argparse
import os
import tkinter as tk
from tkinter import filedialog as fd

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
        parser.add_argument('-i', '--input', type = Tools.dir_path, required = True, help = "Input directory containing ppt/pptx files")
        parser.add_argument('-o', '--output', type = Tools.dir_path, required = True, help = "Output directory for the converted files")
        args = parser.parse_args()

        return args.input, args.output
    

class Gui:
    def render(self):
        window = tk.Tk()
        window.title(f"{Tools.APP_NAME}     v{Tools.APP_VERSION}")
        window.resizable(False, False)
        window.geometry('560x480')


        label1 = tk.Label(text="Select the input directory containing PPT/PPTX files").place(x=5, y=20)
        self.input1 = tk.Entry(fg="white", bg="gray", width=50)
        self.input1.place(x=5, y=50)
        btn1 = tk.Button(text="Browse",command= lambda: self.GetFilePath(self.input1)).place(x=470, y=48)
        
        label2 = tk.Label(text="Select the output directory").place(x=5, y=100)
        self.input2 = tk.Entry(fg="white", bg="gray", width=50)
        self.input2.place(x=5, y=130)
        btn2 = tk.Button(text="Browse", command= lambda: self.GetFilePath(self.input2)).place(x=470, y=128)
 
        window.mainloop()


    def ClearInputs(self):
        self.input_path.delete(0, tk.END)
        self.output_path.delete(0, tk.END)


    def GetFilePath(self, inputX):
        path = fd.askdirectory()
        inputX.delete(0, tk.END)
        inputX.insert(0,path)

    