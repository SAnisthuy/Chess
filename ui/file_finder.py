from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as msg

class FindFile:

    def __init__(self):
        self.root = Tk()
        self.path = StringVar()
    
    def select_file(self):
        """Open a file dialog and return the selected file path."""
        filetypes = (
            ('Executables', '*.exe'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/', 
            filetypes=filetypes
        )
        
        if filename:
            self.file_path_entry.delete(0, END) 
            self.file_path_entry.insert(0, filename)

    def submit_button(self):
        if "avx2.exe" not in str(self.path.get()):
            self.file_path_entry.delete(0, END) 
            self.path = StringVar()
            msg.showerror("Wrong File Error", "The file selected is not the stockfish engine. \n Please try a different file")
        else:
            self.root.quit()
            self.root.destroy()

    def run(self):
        
        self.root.title('File Finder GUI')
        self.root.geometry('458x100')

        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(W, E, N, S))

        frame_button = ttk.Frame(self.root, padding="10")
        frame_button.grid(row=1, column=0, sticky=(W, E, N, S))

        ttk.Label(frame, text="Selected File Path:").grid(row=0, column=0, sticky=W, pady=5)
        submit = Button(frame_button, text="Submit", command=self.submit_button)
        submit.pack()



        self.file_path_entry = ttk.Entry(frame, width=40, textvariable=self.path)
        self.file_path_entry.grid(row=0, column=1, sticky=(W, E), pady=5, padx=5)

        select_button = ttk.Button(frame, text='Browse', command=self.select_file)
        select_button.grid(row=0, column=2, sticky=W, pady=5, padx=5)

        if self.path.get().endswith(".exe"):
            return self.path.get()
        self.root.mainloop()

        return self.path.get()        
