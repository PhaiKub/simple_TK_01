import tkinter as tk


def set_message():
    text=title_text.get()
    title_label.configure(text=text)

Window = tk.Tk()
Window.title("Mr.Kittapas Subesing")

title_label=tk.Label(master=Window, text="SAWAD")
title_label.pack()

title_text=tk.Entry(master=Window)
title_text.pack()

title_button=tk.Button(master=Window , text="Why WHY wHy",command=set_message)
title_button.pack()

title_button=tk.Button(master=Window , text="exit" ,command=exit)
title_button.pack()

Window.minsize(width=500 , height=500)
Window.mainloop()

