import os
import subprocess
import datetime
import json
from colorama import Fore, Style

viod = ""

# Стандартные директории
directories = [
    "/storage/emulated/0/Download/解包",
    "/storage/emulated/0/Download/打包"
]

def gradient_text(text, start_color, end_color):
    """创建start_color到end_color的渐变文本."""
    start_rgb = [int(start_color[i:i + 2], 16) for i in (0, 2, 4)]
    end_rgb = [int(end_color[i:i + 2], 16) for i in (0, 2, 4)]

    gradient = ''
    for i in range(len(text)):
        ratio = i / len(text)
        rgb = [int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio) for j in range(3)]
        gradient += f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text[i]}"
    
    return gradient + Style.RESET_ALL

def get_current_datetime():
    """显示当前时间."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def print_main_menu():
print()
print(viod + gradient_text("▀█▀ █░█ █▀▀ █▀█ ▄▀█ █▄▀", "FF0000", "FF0000"))
print(viod + gradient_text("░█░ █▀█ ██▄ █▀▀ █▀█ █░█", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("--------------------------", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("[1]解包", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("[2]打包", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("[0]退出", "FFFFFF", "FFFFFF"))
print()

def print_unpack_menu():
    print()

def print_repack_menu():
    print()

def list_files_in_directory(directory, file_extension):
    """显示给扩展目录中的文件."""
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"找不到该目录: '{directory}'")

        files = os.listdir(directory)
        target_files = [file for file in files if file.endswith(file_extension)]

        if not target_files:
            print(gradient_text(f"如果file... {file_extension} в каталоге {directory}.", "FFFFFF", "FFFFFF"))
            return None

        print(gradient_text(f"发现了目录 {directory}: ", "FFFFFF", "FFFFFF"))
        for index, file_name in enumerate(target_files, start=1):
            print(gradient_text(f"{index}) {file_name}", "FFFFFF", "FFFFFF"))

        return target_files

    except FileNotFoundError as e:
        print(gradient_text(str(e), "FFFFFF", "FFFFFF"))
    except PermissionError:
        print(gradient_text(f"目录: '{directory}.", "FFFFFF", "FFFFFF"))
    except Exception as e:
        print(gradient_text(f"访问目录出错: {e}", "FFFFFF", "FFFFFF"))

    return None

def execute_command(command):
    """执行sh脚步出现了错误❌."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(gradient_text(result.stdout.strip(), "FFFFFF", "FFFFFF"))  # Вывод результата команды
    except subprocess.CalledProcessError as e:
        print(gradient_text(f"命令执行错误: {e}\n{e.stderr.strip()}", "FFFFFF", "FFFFFF"))

def main():
    subprocess.call("chmod +x quickbms", shell=True)

    while True:
        print_main_menu()
        choice = input(gradient_text("输入你的选项: ", "FFFFFF", "FFFFFF")).strip()


        if choice == '1':
            print_unpack_menu()
            directory = "/storage/emulated/0/Download/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("请输入要选择的数字: ", "FFFFFF", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("输入不能为空,请重新输入", "FFFFFF", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms chinaNB.bms \"{os.path.join(directory, files[index])}\" \"storage/emulated/0/Download/解包/\""
                        execute_command(command)
                    else:
                        print(gradient_text("选项无效.请重新选择", "FFFFFF", "FFFFFF"))
                except ValueError:
                    print(gradient_text("请输入一个有效的数字.", "FFFFFF", "FFFFFF"))

        elif choice == '2':
            print_repack_menu()
            directory = "/storage/emulated/0/Download/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("请输入选项的数字: ", "FFFFFF", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("选项不能为空,请重新尝试.", "FFFFFF", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms -g -w -r -r chinaNB.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/Download/打包/\""
                        execute_command(command)
                    else:
                        print(gradient_text("选项无效,请重新尝试.", "FFFFFF", "FFFFFF"))
                except ValueError:
                    print(gradient_text("请输入一个有效的数字.", "FFFFFF", "FFFFFF"))


        elif choice == '0':
            print(gradient_text("退出中...", "FFFFFF", "FFFFFF"))
            break

        else:
            print(gradient_text("无效选择,请重新输入.", "FFFFFF", "FFFFFF"))

if __name__ == "__main__":
    main()