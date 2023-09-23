
from tools import Tools
import tkinter as tk
from tkinter import filedialog as fd
from pptx_format import Pptx_Format

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


        label3 = tk.Label(text="PPT   files found: ").place(x=5, y=180)
        label_ppt_files_number = tk.Label(text="None").place(x=115, y=180)

        label4 = tk.Label(text="PPTX files found: ").place(x=5, y=205)
        label_pptx_files_number = tk.Label(text="None").place(x=115, y=205)

       
        # from pptx_format import Pptx_Format
        # pptx_obj = Pptx_Format()


        # print(self.input1.get())
        btn_start = tk.Button(text="START", command= lambda: self.StartBtnHandler()).place(x=470, y=205)
        window.mainloop()


    def ClearInputs(self):
        self.input_path.delete(0, tk.END)
        self.output_path.delete(0, tk.END)


    def GetFilePath(self, inputX):
        path = fd.askdirectory()
        inputX.delete(0, tk.END)
        inputX.insert(0,path)


    def StartBtnHandler(self):
       print(self.input1.get())
       pptx_obj = Pptx_Format(self.input1.get())
       self.input2.insert(0,pptx_obj.CountFiles())
    