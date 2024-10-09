ftom tkinter import *
import requests
from PIL import Image,Image TK
from io import BytesIO



window=Tk()
window.title("Картинки с собачками")
window.geometry("360*420")

label=label(pady=10)
label.pack

button=Button("Загрузить изображение",command=show_image)
button.pack(pady=10)

window.mainloop()

