import tkinter as tk
from tkinter import Menu
from tkinter import Menu, PhotoImage
import subprocess
from PIL import Image, ImageTk
from tkinter import Menu, Toplevel
import os

img_label = None

def show_image(image_file, width, height):
    global img_label  # ใช้ตัวแปร img_label ที่เป็น global

    # ถ้ามี Label เก่าที่แสดงรูปภาพอยู่ ให้ลบออกก่อน
    if img_label is not None:
        img_label.destroy()

    # ใช้ Pillow เพื่อเปิดและปรับขนาดรูปภาพ
    img = Image.open(image_file)
    img = img.resize((width, height), Image.Resampling.LANCZOS)  # ใช้ LANCZOS แทน ANTIALIAS
    img_tk = ImageTk.PhotoImage(img)  # แปลงรูปให้ใช้งานกับ Tkinter ได้

    # แสดงรูปภาพในหน้าต่าง
    img_label = tk.Label(window, image=img_tk)
    img_label.image = img_tk  # เก็บอ้างอิงเพื่อป้องกัน GC
    img_label.pack()

def show_popup():
    """แสดงข้อมูลผู้ใช้"""
    popup = Toplevel(window)
    popup.title("My Info")
    popup.geometry("600x600")

    try:
        # โหลดและปรับขนาดรูปภาพ
        image_path = r"img/imageinfo.png"  # แก้ไขเส้นทางไฟล์เป็นแบบ raw string หรือใช้ \\ สำหรับ Windows
        if not os.path.exists(image_path):
            raise FileNotFoundError
        image = Image.open(image_path).resize((300, 300))
        photo = ImageTk.PhotoImage(image)
        
        image_label = tk.Label(popup, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)

        # แสดงข้อความข้อมูล
        info_label = tk.Label(popup, text="66209010012\nนาย ธีรภัทร อุปนัน ทส.66.1", font=("Arial", 16))
        info_label.pack(pady=20)

    except FileNotFoundError:
        tk.Label(popup, text=f"Image file not found: {image_path}", fg="red", font=("Arial", 14)).pack(pady=10)
    except Exception as e:
        tk.Label(popup, text=f"Error: {e}", fg="red", font=("Arial", 14)).pack(pady=10)

    tk.Button(popup, text="Close", command=popup.destroy).pack(pady=10)
# ตัวแปรหน้าต่าง
window = tk.Tk()

# ขนาดหน้าต่าง
window.minsize(width=900, height=650)

# ชื่อหน้าต่าง
window.title('Mr.Thiraphat Auppananan')

# เมนูบาร์
menubar = Menu(window)
window.config(menu=menubar)

# เมนูย่อย File
file_menu = Menu(menubar, tearoff=0, activebackground="#0066FF", activeforeground="black")
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_command(label="Save", command=lambda: print("Save File"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file_menu)

# เมนูย่อย Tuesday
tuesday_menu = Menu(menubar, tearoff=0)
tuesday_menu.add_command(label="งานที่ 1 class and if", command=lambda: show_image("img/img1.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 2 multiply", command=lambda: show_image("img/img2.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 3 even numbers, odd numbers", command=lambda: show_image("img/img3.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 4 AD", command=lambda: show_image("img/img4.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 5 grad_Eng", command=lambda: show_image("img/img5.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 6 grad_Num", command=lambda: show_image("img/img6.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 7 allclass", command=lambda: show_image("img/img7.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 8 login", command=lambda: show_image("img/img8.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 9 Bank", command=lambda: show_image("img/img9.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 10 while_loop", command=lambda: show_image("img/img10.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 11 spell", command=lambda: show_image("img/img11.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 12 print_Num", command=lambda: show_image("img/img12.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 13 while_login", command=lambda: show_image("img/img13.png", 800, 600))
tuesday_menu.add_command(label="งานที่ 14 grad_TH", command=lambda: show_image("img/img14.png", 800, 600))


menubar.add_cascade(label="Tuesday", menu=tuesday_menu)

# เมนูย่อย Thursday
Friday_menu = Menu(menubar, tearoff=0)
Friday_menu.add_command(label="งานที่ 1 คัดลอกคำ", command=lambda: subprocess.run(["python", "jobmenu/ccword.py"]))
Friday_menu.add_command(label="งานที่ 2 login", command=lambda: subprocess.run(["python", "jobmenu/logintest1.py"]))
Friday_menu.add_command(label="งานที่ 3 อะไรก็ได้", command=lambda: subprocess.run(["python", "jobmenu/anything.py"]))
Friday_menu.add_command(label="งานที่ 4 simpleWindow", command=lambda: subprocess.run(["python", "jobmenu/menutest.py"]))
Friday_menu.add_command(label="งานที่ 5 Menu", command=lambda: subprocess.run(["python", "jobmenu/simplelogin.py"]))
Friday_menu.add_command(label="งานที่ 6 simpleMenu", command=lambda: subprocess.run(["python", "jobmenu/todolist.py"]))

menubar.add_cascade(label="Friday", menu=Friday_menu)

# เมนูย่อย Name
info_menu = Menu(menubar, tearoff=0)
info_menu.add_command(label="My Info", command=show_popup)  # เมื่อคลิก "My Info" จะเปิดป๊อปอัพ
menubar.add_cascade(label="My Info", menu=info_menu)

# เริ่มต้นหน้าต่าง
window.mainloop()
