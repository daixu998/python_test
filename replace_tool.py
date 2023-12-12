import fileinput

def replace_in_file(file_path, old_str, new_str):
    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(old_str, new_str), end='')

# 使用示例
replace_in_file('D:\Python\example.txt', 'asd', '111')