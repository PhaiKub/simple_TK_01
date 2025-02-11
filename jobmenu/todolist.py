import tkinter as tk
from tkinter import ttk


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


# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Task Manager")

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

# ผูกเหตุการณ์เมื่อเลือกข้อมูลในตาราง
task_table.bind("<<TreeviewSelect>>", show_details)

# แสดงข้อมูลด้านล่างตาราง
detail_label = ttk.Label(root, text="รายละเอียด: ", anchor="w", padding=10)
detail_label.pack(fill="x", padx=10, pady=5)

# เริ่มโปรแกรม
root.mainloop()
