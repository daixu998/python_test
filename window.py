import tkinter as tk
from tkinter import filedialog

def replace_texture_paths():
    # 获取旧路径和新路径
    old_path = entry_old_path.get()
    new_path = entry_new_path.get()

    # 打开文件选择对话框选择场景文件
    file_path = filedialog.askopenfilename(filetypes=[("Scene Files", "*.max")])

    if file_path:
        # 在此处编写读取并替换贴图路径的逻辑
        # 可以使用适合的库或3D Max的脚本接口来实现路径替换操作

        # 提示替换完成
        label_result.config(text="贴图路径替换完成！")

# 创建主窗口
window = tk.Tk()
window.title("贴图路径统一工具")

# 创建标签和输入框
label_old_path = tk.Label(window, text="旧路径：")
entry_old_path = tk.Entry(window)
label_new_path = tk.Label(window, text="新路径：")
entry_new_path = tk.Entry(window)

# 创建按钮
button_replace = tk.Button(window, text="替换路径", command=replace_texture_paths)

# 创建结果标签
label_result = tk.Label(window, text="")

# 设置布局
label_old_path.grid(row=0, column=0, sticky="e")
entry_old_path.grid(row=0, column=1)
label_new_path.grid(row=1, column=0, sticky="e")
entry_new_path.grid(row=1, column=1)
button_replace.grid(row=2, column=0, columnspan=2)
label_result.grid(row=3, column=0, columnspan=2)

# 运行窗口程序
window.mainloop()