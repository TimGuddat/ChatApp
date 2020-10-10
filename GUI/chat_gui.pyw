from threading import Thread
from tkinter import *
from tkinter.ttk import *
from ChatServerClient import client


def disable_entry_name():
    if entry_name.get() != '':
        entry_name.config(state='disabled')
    else:
        entry_name.focus_set()


def send_message():
    name = entry_name.get()
    text = entry_chat.get()
    if name != '' and text != '':
        msg = f'{name}: {text}\n'
        client.send(msg)
    entry_chat.delete(0, END)


def receive_message():
    run = True
    while run:
        res = client.receive()
        if res == 'exit':
            run = False
        else:
            text_chat.config(state='normal')
            text_chat.insert(END, res)
            text_chat.config(state='disabled')

    client.close_con()
    window.quit()


def close_window():
    client.send('exit')


if __name__ == '__main__':
    thread = Thread(target=receive_message)
    thread.start()

    window = Tk()
    window.title('Chat Test')
    window.resizable(0, 0)
    window.protocol("WM_DELETE_WINDOW", close_window)
    window.bind('<Escape>', lambda event: close_window())

    lb_name = Label(window, text='Name')
    entry_name = Entry(window)
    entry_name.focus_set()
    entry_name.bind('<FocusOut>', lambda event: disable_entry_name())

    text_chat = Text(window, height=20, width=60, state='disabled')

    entry_chat = Entry(window)
    entry_chat.bind('<Return>', lambda event: send_message())

    lb_name.grid(row=0, column=0, padx=20, pady=10)
    entry_name.grid(row=0, column=1, ipadx=30, padx=5, pady=10)

    text_chat.grid(row=1, column=0, columnspan=2, pady=10)

    entry_chat.grid(row=2, column=0, padx=10, pady=10, ipadx=100)

    window.mainloop()
