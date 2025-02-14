import tkinter as tk
from tkinter import messagebox
import subprocess  # ใช้เพื่อรันไฟล์อื่น

def ck_login():
    userid = username_enty.get()
    password = password_enty.get()

    if userid == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome!")
        windows.destroy()  # ปิดหน้าต่างล็อกอิน
        subprocess.run(["python", "code/page1.py"])  # เรียกไฟล์ page1.py
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def exitcom():
    ConfirmExit = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
    if ConfirmExit == "yes":
        windows.destroy()

# สร้างหน้าต่างหลัก
windows = tk.Tk()
windows.minsize(width=500, height=400)
windows.title('Login Form')

# Frame สำหรับ Username
username_frame = tk.Frame(windows)
username_frame.pack(pady=10)
username_label = tk.Label(username_frame, text="UserName: ")
username_label.pack(side=tk.LEFT)
username_enty = tk.Entry(username_frame)
username_enty.pack(side=tk.LEFT)

# Frame สำหรับ Password
password_frame = tk.Frame(windows)
password_frame.pack(pady=10)
password_label = tk.Label(password_frame, text="PassWord: ")
password_label.pack(side=tk.LEFT)
password_enty = tk.Entry(password_frame, show="*")
password_enty.pack(side=tk.LEFT)

# Frame สำหรับปุ่ม Login และ Exit
button_frame = tk.Frame(windows)
button_frame.pack(pady=20)
login_button = tk.Button(button_frame, text="Login", command=ck_login)
login_button.pack(side=tk.LEFT, padx=10)
logout_button = tk.Button(button_frame, text="Exit", command=exitcom)
logout_button.pack(side=tk.LEFT, padx=10)

windows.mainloop()
