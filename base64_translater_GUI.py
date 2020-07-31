# coding = utf-8

import base64
import os
import sys
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import windnd


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        # base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def translate_base64(file):
    source_file = open(file, "rb")
    base_64_file = base64.b64encode(source_file.read())
    source_file.close()
    return base_64_file


def save_data(data, file_name):
    file = open(file_name, "a")
    file.write(str(data))


def dragged_files(files):
    msg = '\n'.join(item.decode('gbk') for item in files)
    if len(files) > 1:
        tkinter.messagebox.showerror('Oops!', '拖入的文件太多啦\n只能拖一个哦')
    else:
        data = translate_base64(msg)
        save_data(data, msg + '.txt')
        tkinter.messagebox.showinfo(
            'Done!', '存储到 ' + msg + '.txt')
        os.startfile(msg + '.txt')


def clicked_files():
    files = tkinter.filedialog.askopenfilename()

    if len(files) > 0:
        msg = files
        data = translate_base64(msg)
        save_data(data, msg + '.txt')
        tkinter.messagebox.showinfo(
            'Done!', '存储到 ' + msg + '.txt')
        os.system('start ' + msg + '.txt')
    else:
        pass


if __name__ == "__main__":
    tk = tkinter.Tk()
    tk.geometry("450x300")
    tk.title("base64 Translater")
    tk.iconbitmap(resource_path(os.path.join("icon.ico")))

    f1 = tkinter.Frame(width=225, height=300)
    f2 = tkinter.Frame(width=225, height=300)
    f1.place(x=0, y=0)
    f2.place(x=225, y=0)

    label1 = tkinter.Label(f1, text='拖到这里', font=('Arial', 12))
    label1.place(x=112.5, y=150, anchor=tkinter.CENTER)
    button1 = tkinter.Button(f2, text='打开文件...', command=clicked_files)
    button1.place(x=112.5, y=150, anchor=tkinter.CENTER)

    windnd.hook_dropfiles(f1, func=dragged_files)

    tk.mainloop()
