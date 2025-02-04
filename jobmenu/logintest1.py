import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับตรวจสอบข้อมูลการเข้าสู่ระบบ
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# ฟังก์ชันสำหรับแสดงหรือซ่อนรหัสผ่าน
def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_btn.config(text="Hide Password")
    else:
        password_entry.config(show='*')
        toggle_btn.config(text="Show Password")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title('Login Form')
window.minsize(width=300, height=150)

# การจัดวางองค์ประกอบด้วย grid
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

toggle_btn = tk.Button(window, text="Show Password", command=toggle_password)
toggle_btn.grid(row=1, column=2, padx=10, pady=10)

login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=3, pady=10)

# เริ่มต้นโปรแกรม
window.mainloop()
