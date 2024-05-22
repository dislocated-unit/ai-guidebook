
import tkinter as tk
import os

#user
import GUIDEBOOK_FUNCTIONS as GF

#export script 
RUN_TROUGH_FILES = 'check-files.py'

os.chdir(os.path.dirname(__file__))

#app window
window = tk.Tk()

#window size
window.geometry('400x200')

#app title
window.title("AI-guidebook handler")

label = tk.Label(window, text="AI guidebook no-internet handler")
label.pack(padx=20, pady=20)

#export script button
button = tk.Button(window, text="Export ipynb to HTML", command=lambda: GF.RUN_python_script(RUN_TROUGH_FILES))
button.pack(padx=20, pady=20) 

# loop till window is closed
window.mainloop()
