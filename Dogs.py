ftom tkinter import *
from tkinter import message box as mb
import requests
from PIL import Image,Image TK
from io import BytesIO



def show image():
    image_url=dog_get_image()
    if image_ url:
        try:
            response=requests.get(image_url,stream=True)
            response.raise_for_status()
            img_data=Bytes.io(response.content)
            img=Image.open(img_data)
            img.thumbnail((300,300))
            label.config(image=img)
            label.image=img
            except=Expection as e:
            mb.showerror("ощибка")

window=Tk()
window.title("Картинки с собачками")
window.geometry("360*420")

label=label(pady=10)
label.pack

button=Button("Загрузить изображение",command=show_image)
button.pack(pady=10)


window.mainloop()

