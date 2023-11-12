import binascii
from tkinter import *
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
from tkinter import messagebox

# Window
window = Tk()
window.title('Crypto Message')
window.minsize(500, 700)
window.configure()

# Image
image = Image.open('key.jpeg')
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)

label_image = Label(image=img)
label_image.image = img
label_image.place(x=200, y=50)

# Label1
label1 = Label(text="Enter your title", font=('Italic', 10, 'bold'))
label1.place(x=200, y=170)


# File Handling
def append_file(filename, text_):
    try:
        with open("Crypto.txt", 'a') as f:
            f.write("\n" + text_)
        print(f"The appended to file {filename} successfully.")
    except IOError:
        print(f"Error: could not append to file{filename}")


# Title Entry
title_entry = Entry(width=30)
title_entry.place(x=160, y=200)

# Label2
label2 = Label(text="Enter your secret", font=('Italic', 10, 'bold'))
label2.place(x=200, y=230)

# Text
text = Text(width=24, height=13)
text.focus()
text.place(x=150, y=250)

# label3
label3 = Label(text="Enter master key", font=('Italic', 10, 'bold'))
label3.place(x=200, y=470)

# Master Key
entry2 = Entry(width=20)
entry2.place(x=190, y=490)

key = Fernet.generate_key()
fernet = Fernet(key)

master_key = ""


def save_encrypt():
    title = title_entry.get()
    append_file(filename='Crypto.txt', text_=title)
    message_text = text.get('1.0', END)
    message = message_text
    enc_message = fernet.encrypt(message.encode())
    append_file(filename='Crypto.txt', text_=str(enc_message))

    global master_key
    master_key = entry2.get()

    title_entry.delete(first=0, last=END)
    text.delete('1.0', END)
    entry2.delete(first=0, last=END)


def decoder():
    if master_key == entry2.get():
        try:
            text_ = text.get('1.0', END)
            dec_message = fernet.decrypt(text_).decode()
            text.delete('1.0', END)
            text.update()
            text.insert(END, dec_message)
        except:
            messagebox.showerror("ValueError", "Please Encode text the given.")
    else:
        messagebox.showwarning(title="Warning", message="Master key not True")


# Button1
button1 = Button(text="Save & Encrypt", command=save_encrypt)
button1.place(x=200, y=520)

# Button2
button2 = Button(text="Decrypt", command=decoder)
button2.place(x=215, y=560)

window.mainloop()
