from tkinter import *
import instaloader

root = Tk()
root.title('Instagram profile downloader')
root.geometry('300x200')
root.resizable(width=False, height=False)

id_input = Entry(root)
id_input.place(x=10, y=10)


def get_profile_image():
    il = instaloader.Instaloader()
    il.download_profile(id_input.get(), profile_pic_only=True)


btn = Button(root, text='Get Image', command=lambda: get_profile_image())
btn.place(x=135, y=10)

root.mainloop()
