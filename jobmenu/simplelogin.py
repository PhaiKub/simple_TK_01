from tkinter import Tk,Menu
import tkinter as tk
window =tk.Tk()

def new_file():
    print("สร้างไฟล์ใหม่")

def open_file():
    print("เปิดไฟล์")

def open_foder():
    print("เปิดโฟลเดอร์")

def Save():
    print("save")

def open_recent():
    print("open_recent")
    
def new_text_file():
    print("สร้างไฟล์ข้อความใหม่")
    
def new_Window():
    print("new_Window")
     
def open_WS_F_File():
    print("save")

def Save_As():
    print("save")
    
def Save_All():
    print("save")

# กำหนดชื่อ title
window.title('Mr.Mananchai Kaewmung')

# สร้างเมนูหลัก
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
window.minsize(width=500, height=500)

# เมนู File
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Text File", command=new_text_file, accelerator="Ctrl+N")
file_menu.add_command(label="New File...", command=new_file, accelerator="Ctrl+Alt+Windows+N")
file_menu.add_command(label="New Window", command=new_Window, accelerator="Ctrl+Shift+N")

sud_memu = Menu(file_menu , tearoff=0)
sud_memu.add_cascade(label="New Profile")
file_menu.add_cascade(label="New Window with profile",menu=sud_memu)

file_menu.add_separator()
file_menu.add_command(label="Open File...", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Open Folder", command=open_foder, accelerator="Ctrl+k Ctrl+O")
file_menu.add_command(label="Open Workspace from File...", command=open_WS_F_File,)

file_menu.add_cascade(label="Open Recent",)
file_menu.add_separator()
file_menu.add_command(label="Save", command=Save, accelerator="Ctrl+s")
file_menu.add_command(label="Save As...", command=Save_As, accelerator="Ctrl+Shift+s")
file_menu.add_command(label="Save All", command=Save_All, accelerator="Ctrl+K S")
file_menu.add_separator()

sud_memu = Menu(file_menu,tearoff=0)
sud_memu.add_cascade(label="Export Profile")
file_menu.add_cascade(label="Share", menu=sud_memu)
file_menu.add_separator()
file_menu.add_command(label="Auto Save", command=open_foder, )

sud_memu = Menu(file_menu,tearoff=0)
sud_memus = Menu(sud_memu,tearoff=0)
sud_memu.add_cascade(label="Profiles")
sud_memu.add_cascade(label="Settings")
sud_memu.add_cascade(label="Extensions")
sud_memu.add_cascade(label="Keyboard Shortcuts")
sud_memu.add_cascade(label="Configure Snippets")
sud_memu.add_cascade(label="Tasks")
sud_memus.add_cascade(label="Color")
sud_memu.add_cascade(label="Theme")
sud_memu.add_separator()
sud_memu.add_cascade(label="Backup and Sync Settings")
sud_memu.add_separator()
sud_memu.add_cascade(label="Online Services Settings")

file_menu.add_cascade(label="Preferences", menu=sud_memu)
file_menu.add_separator()
file_menu.add_command(label="Revert File", command=open_foder,)
file_menu.add_command(label="Close Editor", command=open_foder, accelerator="Ctrl+F4")
file_menu.add_command(label="Close Folder", command=open_foder, accelerator="Ctrl + K F")
file_menu.add_command(label="Close Window", command=open_foder, accelerator="Alt + F4")
file_menu.add_command(label="Exit", command=open_foder,)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=open_foder, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=open_foder, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=open_foder, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=open_foder, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=open_foder, accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=open_foder, accelerator="Ctrl+F")
edit_menu.add_command(label="Replace", command=open_foder, accelerator="Ctrl+H")
edit_menu.add_separator()
edit_menu.add_command(label="Find in Files", command=open_foder, accelerator="Ctrl+Shift+F")
edit_menu.add_command(label="Replace in Files", command=open_foder, accelerator="Ctrl+Shift+H")
edit_menu.add_separator()
edit_menu.add_command(label="Toggle Line Comment", command=open_foder, accelerator="Ctrl+/")
edit_menu.add_command(label="Toggle Block Comment", command=open_foder, accelerator="Shift+Alt+A")
edit_menu.add_command(label="Emmet: Expand Abbreviation", command=open_foder, accelerator="Tab")



selection_menu = tk.Menu(menu_bar, tearoff=0)
selection_menu.add_command(label="Select All", command=open_foder, accelerator="Ctrl+A")
selection_menu.add_command(label="Expand Selection", command=open_foder, accelerator="Shift+Alt+RightArrow")
selection_menu.add_command(label="Shrink Selection", command=open_foder, accelerator="Shift+Alt+LeftArrow")
selection_menu.add_separator()
selection_menu.add_command(label="Copy Line Up", command=open_foder, accelerator="Shift+Alt+UpArrow")
selection_menu.add_command(label="Copy Line Down", command=open_foder, accelerator="Shift+Alt+DownArrow")
selection_menu.add_command(label="Duplicate Selection", command=open_foder, )
selection_menu.add_separator()
selection_menu.add_command(label="Add Cursor Above", command=open_foder, accelerator="Alt+UpArrow")
selection_menu.add_command(label="Add Cursor Below", command=open_foder, accelerator="Alt+DownArrow")
selection_menu.add_command(label="Add Next Occurrence", command=open_foder, accelerator="Shift+Alt+1")
selection_menu.add_command(label="Add Previous Occurrenc", command=open_foder, accelerator="Ctrl+D")
selection_menu.add_command(label="Select All Occurrences", command=open_foder, accelerator="Ctrl+Shift+L")
selection_menu.add_separator()
selection_menu.add_command(label="Switch to Ctrl+Click for Multi-Cursor", command=open_foder, )
selection_menu.add_command(label="Column Selection Mode", command=open_foder,)

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Command Palette...", command=open_foder, accelerator="Ctrl+Shift+P")
view_menu.add_command(label="Open View...", command=open_foder, )
view_menu.add_separator()
view_menu.add_command(label="Appearance", command=open_foder,)
view_menu.add_command(label="Editor Layout", command=open_foder,)
view_menu.add_separator()
view_menu.add_command(label="Explorer", command=open_foder,accelerator="Ctrl+Shift+E")
view_menu.add_command(label="Search", command=open_foder, accelerator="Ctrl+Shift+F")
view_menu.add_command(label="Source Control", command=open_foder, accelerator="Ctrl+Shift+G")
view_menu.add_command(label="Run", command=open_foder, accelerator="Ctrl+Shift+D")
view_menu.add_command(label="Extensions", command=open_foder, accelerator="Ctrl+Shift+X")
view_menu.add_command(label="Testing", command=open_foder,)
view_menu.add_separator()
view_menu.add_command(label="Problems", command=open_foder, accelerator="Ctrl+Shift+M")
view_menu.add_command(label="Output", command=open_foder, accelerator="Ctrl+Shift+U")
view_menu.add_command(label="Debug Console", command=open_foder, accelerator="Ctrl+Shift+Y")
view_menu.add_command(label="Terminal", command=open_foder, accelerator="Ctrl+")
view_menu.add_separator()
view_menu.add_command(label="Word Wrap", command=open_foder, accelerator="Alt+Z")


go_menu = tk.Menu(menu_bar, tearoff=0)
go_menu.add_command(label="Back", command=open_foder, accelerator="Alt+LeftArrow")
go_menu.add_command(label="Forward", command=open_foder, accelerator="Alt+RightArrow")
go_menu.add_command(label="Last Edit Location", command=open_foder, accelerator="Ctrl+K Ctrl+Q")
go_menu.add_separator()
go_menu.add_command(label="Switch Editor", command=open_foder,)
go_menu.add_command(label="Switch Group", command=open_foder,)
go_menu.add_separator()
go_menu.add_command(label="Go to File...", command=open_foder, accelerator="Ctrl+P")
go_menu.add_command(label="Go to Symbol in Workspace...", command=open_foder, accelerator="Ctrl+T")
go_menu.add_separator()
go_menu.add_command(label="Go to Symbol in Editor...", command=open_foder, accelerator="Ctrl+Shift+O")
go_menu.add_command(label="Go to Definition", command=open_foder, accelerator="F12")
go_menu.add_command(label="Go to Declaration", command=open_foder,)
go_menu.add_command(label="Go to Type Definition", command=open_foder,)
go_menu.add_command(label="Go to Implementations", command=open_foder, accelerator="Ctrl+F12")
go_menu.add_command(label="Go to References", command=open_foder, accelerator="Shift+F12")
go_menu.add_separator()
go_menu.add_command(label="Go to Line/Column...", command=open_foder, accelerator="Ctrl+G")
go_menu.add_command(label="Go to Bracket", command=open_foder, accelerator="Ctrl+Shift+")
go_menu.add_separator()
go_menu.add_command(label="Next Problem", command=open_foder, accelerator="F8")
go_menu.add_command(label="Previous Problem", command=open_foder, accelerator="Shift+F8")
go_menu.add_separator()
go_menu.add_command(label="Next Change", command=open_foder, accelerator="Shift+Alt+F3")
go_menu.add_command(label="Previous Change", command=open_foder, accelerator="Alt+F3")

run_menu = tk.Menu(menu_bar, tearoff=0)
run_menu.add_command(label="Start Debugging", command=open_foder, accelerator="F5")
run_menu.add_command(label="Run Without Debugging", command=open_foder, accelerator="Ctrl+F5")
run_menu.add_command(label="Stop Debugging", command=open_foder, accelerator="Shift+F5")
run_menu.add_command(label="Restart Debugging", command=open_foder, accelerator="Ctrl+Shift+F5")
run_menu.add_separator()
run_menu.add_command(label="Open Configurations", command=open_foder, )
run_menu.add_command(label="Add Configuration...", command=open_foder, )
run_menu.add_separator()
run_menu.add_command(label="Step Over", command=open_foder, accelerator="F10")
run_menu.add_command(label="Step Into", command=open_foder, accelerator="F11")
run_menu.add_command(label="Step Out", command=open_foder, accelerator="Shift+F11")
run_menu.add_command(label="Continue", command=open_foder, accelerator="F5")
run_menu.add_separator()
run_menu.add_command(label="Toggle Breakpoint", command=open_foder, accelerator="F9")
run_menu.add_command(label="New Breakpoint", command=open_foder, )
run_menu.add_separator()
run_menu.add_command(label="Enable All Breakpoints", command=open_foder, )
run_menu.add_command(label="Disable All Breakpoints", command=open_foder, )
run_menu.add_command(label="Remove All Breakpoints", command=open_foder,)
run_menu.add_separator()
run_menu.add_command(label="Install Additional Debuggers...", command=open_foder,)

terminal_menu = tk.Menu(menu_bar, tearoff=0)
terminal_menu.add_command(label="New Terminal", command=open_foder, accelerator="Ctrl+Shift+")
terminal_menu.add_command(label="Split Terminal", command=open_foder, accelerator="Ctrl+Shift+5")
terminal_menu.add_separator()
terminal_menu.add_command(label="Run Task...", command=open_foder, )
terminal_menu.add_command(label="Run Build Task...", command=open_foder, accelerator="Ctrl+Shift+B")
terminal_menu.add_command(label="Run Active File", command=open_foder,)
terminal_menu.add_command(label="Run Selected Text", command=open_foder,)
terminal_menu.add_separator()
terminal_menu.add_command(label="Show Running Tasks...", command=open_foder,)
terminal_menu.add_command(label="Restart Running Task...", command=open_foder,)
terminal_menu.add_command(label="Terminate Task...", command=open_foder,)
terminal_menu.add_separator()
terminal_menu.add_command(label=" Configure Tasks...", command=open_foder,)
terminal_menu.add_command(label="Configure Default Build Task...", command=open_foder,)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Welcome", command=open_foder,)
help_menu.add_command(label="Show All Commands", command=open_foder, accelerator="Ctrl+Shift+P")
help_menu.add_command(label="Documentation", command=open_foder, )
help_menu.add_command(label="Editor Playground", command=open_foder, )
help_menu.add_command(label="Show Release Notes", command=open_foder, )
help_menu.add_command(label="Get Started with Accessibility Features", command=open_foder, )
help_menu.add_separator()
help_menu.add_command(label="Keyboard Shortcuts Reference", command=open_foder, accelerator="Ctrl+K Ctrl+R")
help_menu.add_command(label="Video Tutorials", command=open_foder, )
help_menu.add_command(label="Tips and Tricks", command=open_foder,)
help_menu.add_separator()
help_menu.add_command(label="Join Us on YouTube", command=open_foder, )
help_menu.add_command(label="Search Feature Requests", command=open_foder, )
help_menu.add_command(label="Report Issue", command=open_foder,)
help_menu.add_separator()
help_menu.add_command(label="View License", command=open_foder, )
help_menu.add_command(label="Privacy Statement", command=open_foder, )
help_menu.add_separator()
help_menu.add_command(label="Toggle Developer Tools", command=open_foder,)
help_menu.add_command(label="Open Process Explorer", command=open_foder,)
help_menu.add_separator()
help_menu.add_command(label="Restart to Update", command=open_foder,)
help_menu.add_separator()
help_menu.add_command(label="About", command=open_foder,)





# เพิ่มเมนูหลักลงใน menu bar
menu_bar.add_cascade(label="File", menu=file_menu,underline=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu,underline=0)
menu_bar.add_cascade(label="Selection", menu=selection_menu,underline=0)
menu_bar.add_cascade(label="View", menu=view_menu,underline=0)
menu_bar.add_cascade(label="Go", menu=go_menu,underline=0)
menu_bar.add_cascade(label="Run", menu=run_menu,underline=0)
menu_bar.add_cascade(label="Terminal", menu=terminal_menu,underline=0)
menu_bar.add_cascade(label="Help", menu=help_menu,underline=0)



# สร้างเมนูหลัก
ok_button = tk.Button(master=window, text='ออกโปรแกรม',command=exit)
ok_button.pack()

# สร้างหน้าต่างฟอร์ม

window.mainloop()