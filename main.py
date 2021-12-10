import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter.messagebox import showinfo

root = tk.Tk()
root.resizable(False, False)
root.geometry('600x600')
root.title('Water Marker')
watermark_text = tk.StringVar()

label1 = tk.Label(root, text="Watermark Machine", bd=5, font=('calibre', 30, 'bold'))
watermark_text = tk.Entry(root, text="Enter Watermark Text", textvariable=watermark_text, font=('calibre', 15, 'bold'))
Label2 = tk.Label(root, text="Water Mark Text", font=('calibre', 15, 'bold'))
logopath = ""


def choose_logo():
    global logopath
    filepath = filedialog.askopenfilename(title="Open A File")
    logopath = filepath


def add_text(filename, name):
    with Image.open(fp=filename) as im:
        width, height = im.size
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("fonts/Roboto-Black.ttf", 36)
        text_width, text_height = draw.textsize(text=name, font=font)
        print(text_width, text_height, width, height)
        x = width - text_width - 10
        y = height - text_height - 10
        draw.text((x, y), text=name, font=font)
    return im.show()


def add_logo(filename):
    logo_image = Image.open(logopath)
    background_image = Image.open(filename)
    background_image.paste(logo_image, (50, 50))
    background_image.save('final.png')  #set the image format


def openfile():
    '''Opens File Selection Dialog of your Desktop. Choose the image.'''
    name = watermark_text.get()
    filename = filedialog.askopenfilename(title="Open A File")
    showinfo(title='Filename', message=filename)
    if name != "":
        add_text(filename, name)
    elif logopath != "":
        print(logopath)
        add_logo(filename)
    else:
        print(logopath)
        Label3 = tk.Label(root, text="Water Mark Text", fg='red', font=('calibre', 15, 'bold'))
        Label3.grid(row=4, column=2)


file = tk.Button(root, text="Open Image", padx=10, pady=10, fg='blue', bg='#4a7a8c', activebackground='green',
                 activeforeground='white', font=('calibre', 15, 'bold'), command=openfile)
logo = tk.Button(root, text="Choose Logo", padx=10, pady=10, fg="red", font=('calibre', 15, 'bold'),
                 command=choose_logo)
file.grid(row=3, column=2, padx=10, pady=10)
watermark_text.grid(row=2, column=2)
logo.grid(row=3, column=1)
label1.grid(row=1, column=2, padx=(10, 10))
Label2.grid(row=2, column=1)
root.mainloop()
