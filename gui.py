
from tools import Tools
import tkinter as tk
from tkinter import filedialog as fd
from pptx_format import Pptx_Format
from ppt_format import Ppt_Format

class Gui:
    def render(self):
        window = tk.Tk()
        window.title(f"{Tools.APP_NAME}     v{Tools.APP_VERSION}")
        window.resizable(False, False)
        window.geometry('560x480')


        label1 = tk.Label(text="Select the input directory containing PPT/PPTX files").place(x=5, y=20)
        self.input1 = tk.Entry(fg="white", bg="gray", width=50)
        self.input1.place(x=5, y=50)
        btn1 = tk.Button(text="Browse",command= lambda: self.GetInPath(self.input1)).place(x=470, y=48)
        
        label2 = tk.Label(text="Select the output directory").place(x=5, y=100)
        self.input2 = tk.Entry(fg="white", bg="gray", width=50)
        self.input2.place(x=5, y=130)
        btn2 = tk.Button(text="Browse", command= lambda: self.GetOutPath(self.input2)).place(x=470, y=128)


        label3 = tk.Label(text="PPT   files found: ").place(x=5, y=180)
        self.label_ppt_files_number = tk.Label(text="None")
        self.label_ppt_files_number.place(x=115, y=180)

        label4 = tk.Label(text="PPTX files found: ").place(x=5, y=205)
        self.label_pptx_files_number = tk.Label(text="None")
        self.label_pptx_files_number.place(x=115, y=205)

        #Create objects to interact with
        self.pptx_obj = Pptx_Format()
        self.ppt_obj  = Ppt_Format()
       
        btn_start = tk.Button(text="START", command= lambda: self.StartBtnHandler()).place(x=470, y=205)
        window.mainloop()


    def ClearInputs(self):
        self.input_path.delete(0, tk.END)
        self.output_path.delete(0, tk.END)


    def GetInPath(self, inputX):
        path = fd.askdirectory()
        inputX.delete(0, tk.END)
        inputX.insert(0,path)
        self.pptx_obj.init(path)
        self.ppt_obj.init(path)

        #update label with number of pptx files
        self.label_ppt_files_number.config(text=self.ppt_obj.CountFiles())
        self.label_pptx_files_number.config(text=self.pptx_obj.CountFiles())


    def GetOutPath(self, inputX):
        path = fd.askdirectory()
        inputX.delete(0, tk.END)
        inputX.insert(0,path)


    def StartBtnHandler(self):
       pass
    