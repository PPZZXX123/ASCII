import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def ascii_to_char():
    try:
        ascii_code = int(ascii_entry.get())
        result = chr(ascii_code)
        result_label.config(text=f"对应的字符是: {result}")
        # 可以根据复选框和下拉菜单状态做额外处理
        if check_var.get() == 1:
            text_box.insert(tk.END, f"高级模式下转换 ASCII 码 {ascii_code} 为字符 {result}\n")
        else:
            text_box.insert(tk.END, f"标准模式下转换 ASCII 码 {ascii_code} 为字符 {result}\n")
    except ValueError:
        messagebox.showerror("错误", "输入的 ASCII 码无效。")


def char_to_ascii():
    char = char_entry.get()
    if len(char) != 1:
        messagebox.showerror("错误", "请输入单个字符。")
    else:
        result = ord(char)
        result_label.config(text=f"对应的 ASCII 码是: {result}")
        # 可以根据复选框和下拉菜单状态做额外处理
        if check_var.get() == 1:
            text_box.insert(tk.END, f"高级模式下转换字符 {char} 为 ASCII 码 {result}\n")
        else:
            text_box.insert(tk.END, f"标准模式下转换字符 {char} 为 ASCII 码 {result}\n")


# 创建主窗口
root = tk.Tk()
root.title("ASCII 翻译器")
root.geometry("500x650")
root.configure(bg="#e0f7fa")

# 创建样式
style = ttk.Style()
style.theme_use('clam')

# 设置标签样式
style.configure('TLabel', background="#e0f7fa", font=("Helvetica", 12))
style.configure('Title.TLabel', background="#e0f7fa", font=("Helvetica", 18, "bold"))

# 标题标签
title_label = ttk.Label(root, text="ASCII 翻译器", style='Title.TLabel')
title_label.pack(pady=20)

# 创建输入框架
input_frame = ttk.Frame(root, style='TFrame')
input_frame.pack(pady=20)

# ASCII 码输入
ascii_label = ttk.Label(input_frame, text="输入 ASCII 码:")
ascii_label.grid(row=0, column=0, padx=10, pady=5)
ascii_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
ascii_entry.grid(row=0, column=1, padx=10, pady=5)

# 字符输入
char_label = ttk.Label(input_frame, text="输入字符:")
char_label.grid(row=1, column=0, padx=10, pady=5)
char_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
char_entry.grid(row=1, column=1, padx=10, pady=5)

# 设置按钮样式
style.configure('TButton', font=("Helvetica", 12))
style.map('TButton',
          foreground=[('active', 'white'), ('!disabled', 'black')],
          background=[('active', '#0097a7'), ('!disabled', '#b2ebf2')])

# 创建按钮框架
button_frame = ttk.Frame(root, style='TFrame')
button_frame.pack(pady=20)

# 转换按钮
ascii_to_char_button = ttk.Button(button_frame, text="ASCII 码转字符", command=ascii_to_char)
ascii_to_char_button.grid(row=0, column=0, padx=10)
char_to_ascii_button = ttk.Button(button_frame, text="字符转 ASCII 码", command=char_to_ascii)
char_to_ascii_button.grid(row=0, column=1, padx=10)

# 添加复选框
check_var = tk.IntVar()
check_button = tk.Checkbutton(root, text="启用高级模式", variable=check_var, bg="#e0f7fa", font=("Helvetica", 12))
check_button.pack(pady=10)

# 添加下拉菜单
options = ["标准模式", "高级模式", "专家模式"]
combo_var = tk.StringVar()
combo_box = ttk.Combobox(root, textvariable=combo_var, values=options, font=("Helvetica", 12))
combo_box.set("标准模式")
combo_box.pack(pady=10)

# 添加滚动条和文本框
text_frame = ttk.Frame(root)
text_frame.pack(pady=10)

text_box = tk.Text(text_frame, height=10, width=40, font=("Helvetica", 12))
text_box.pack(side=tk.LEFT, fill=tk.Y)

scrollbar = ttk.Scrollbar(text_frame, command=text_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box.config(yscrollcommand=scrollbar.set)

# 创建结果标签
result_label = ttk.Label(root, text="", style='TLabel')
result_label.pack(pady=20)

# 运行主循环
root.mainloop()
    
