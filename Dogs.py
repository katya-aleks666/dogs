ftom tkinter import *
from tkinter import message box as mb
import requests
from PIL import Image,Image TK
from io import BytesIO


def get_dog_image
    try:
     response=requests.get
     response.reis_for_status()
     data=response.json()
     return data('message')
    except Exception as e:
        mb.showerror(title:"Ощибка", message: f"Возникла ошибка при запросе к API {e}")


def show image():
    image_url=dog_get_image(https://dog.ceo/api/breeds/image/random)
    if image_ url:
        try:
            response=requests.get(image_url,stream=True)
            response.raise_for_status()
            img_data=Bytes.io(response.content)
            img=Image.open(img_data)
            img.thumbnail((300,300))
            img=ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image=img
            except=Expection as e:
            mb.showerror(title:"Ощибка",message:f"Возникла ошибка при загрузке изоюражения {e}")
            return None


window=Tk()
window.title("Картинки с собачками")
window.geometry("360*420")

label=label(pady=10)
label.pack

button=Button("Загрузить изображение",command=show_image)
button.pack(pady=10)


window.mainloop()

