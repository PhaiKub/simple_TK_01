import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def ck_login():
    userid = username_enty.get()
    password = password_enty.get()

    if userid == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome!")
        windows.destroy()  # ปิดหน้าต่าง login
        open_task_manager()  # เรียกฟังก์ชั่นเปิดหน้าต่าง Task Manager
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def exitcom():
    ConfirmExit = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
    if ConfirmExit == "yes":
        windows.destroy()

def open_task_manager():
    root = tk.Tk()
    root.title("Task Manager")

    def add_task():
        """เพิ่มข้อมูลลงในตาราง"""
        task = task_entry.get()
        if task:  # ตรวจสอบว่ากรอกข้อมูลหรือไม่
            task_table.insert("", "end", values=(task,))
            task_entry.delete(0, tk.END)

    def remove_task():
        """ลบแถวที่เลือกในตาราง"""
        selected_item = task_table.selection()
        if selected_item:
            task_table.delete(selected_item[0])

    def complete_task():
        """เปลี่ยนสถานะของงานเป็น 'Completed'"""
        selected_item = task_table.selection()
        if selected_item:
            task_data = task_table.item(selected_item, "values")
            completed_task = f"[Completed] {task_data[0]}"
            task_table.item(selected_item, values=(completed_task,))

    def show_details(event):
        """แสดงข้อมูลของแถวที่เลือก"""
        selected_item = task_table.selection()
        if selected_item:
            task_data = task_table.item(selected_item, "values")
            detail_label.config(text=f"รายละเอียด: {task_data[0]}")

    def exit_task_manager():
        """ฟังก์ชั่นออกจาก Task Manager"""
        ConfirmExit = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
        if ConfirmExit == "yes":
            root.destroy()  # ปิดหน้าต่าง Task Manager

    # ส่วนกรอกข้อมูล
    input_frame = ttk.Frame(root, padding=10)
    input_frame.pack(fill="x")

    task_label = ttk.Label(input_frame, text="Task:")
    task_label.pack(side="left", padx=5)

    task_entry = ttk.Entry(input_frame)
    task_entry.pack(side="left", fill="x", expand=True, padx=5)

    add_button = ttk.Button(input_frame, text="Add Task", command=add_task)
    add_button.pack(side="left", padx=5)

    # ตารางแสดงข้อมูล
    task_table = ttk.Treeview(root, columns=("task",), show="headings", height=10)
    task_table.heading("task", text="Task")
    task_table.pack(fill="both", padx=10, pady=10)

    # ปุ่มลบและสำเร็จงาน
    button_frame = ttk.Frame(root, padding=10)
    button_frame.pack(fill="x")

    remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task)
    remove_button.pack(side="left", padx=5)

    complete_button = ttk.Button(button_frame, text="Complete Task", command=complete_task)
    complete_button.pack(side="left", padx=5)

    # ปุ่ม Exit ใน Task Manager
    exit_button = ttk.Button(button_frame, text="Exit", command=exit_task_manager)
    exit_button.pack(side="left", padx=5)

    # ผูกเหตุการณ์เมื่อเลือกข้อมูลในตาราง
    task_table.bind("<<TreeviewSelect>>", show_details)

    # แสดงข้อมูลด้านล่างตาราง
    detail_label = ttk.Label(root, text="รายละเอียด: ", anchor="w", padding=10)
    detail_label.pack(fill="x", padx=10, pady=5)

    # เริ่มโปรแกรม
    root.mainloop()

# สร้างหน้าต่าง login
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
