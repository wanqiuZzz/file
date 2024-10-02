import os
import subprocess
import datetime
import json
from colorama import Fore, Style

viod = "              "

# Стандартные директории
directories = [
    "/storage/emulated/0/Download/解包",
    "/storage/emulated/0/Download/打包"
]

def gradient_text(text, start_color, end_color):
    """Создает градиентный текст от start_color до end_color."""
    start_rgb = [int(start_color[i:i + 2], 16) for i in (0, 2, 4)]
    end_rgb = [int(end_color[i:i + 2], 16) for i in (0, 2, 4)]

    gradient = ''
    for i in range(len(text)):
        ratio = i / len(text)
        rgb = [int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio) for j in range(3)]
        gradient += f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text[i]}"
    
    return gradient + Style.RESET_ALL

def get_current_datetime():
    """Возвращает текущую дату и время в отформатированной строке."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def print_main_menu():
    print()
print(viod + gradient_text("▀█▀ █░█ █▀▀ █▀█ ▄▀█ █▄▀", "FF0000", "FF0000"))
print(viod + gradient_text("░█░ █▀█ ██▄ █▀▀ █▀█ █░█", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("--------------------------------------------------", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("[1]解包", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("[2]打包", "FFFFFF", "FFFFFF"))
print(viod + gradient_text("[0]退出", "FFFFFF", "FFFFFF"))
print()

def print_unpack_menu():
    print()

def print_repack_menu():
    print()

def list_files_in_directory(directory, file_extension):
    """Показывает файлы в данном каталоге с заданным расширением."""
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Каталог не найден: '{directory}'")

        files = os.listdir(directory)
        target_files = [file for file in files if file.endswith(file_extension)]

        if not target_files:
            print(gradient_text(f"Не найдено файлов с расширением {file_extension} в каталоге {directory}.", "FF0000", "FFFFFF"))
            return None

        print(gradient_text(f"Файлы в каталоге {directory}: ", "00FF00", "FFFFFF"))
        for index, file_name in enumerate(target_files, start=1):
            print(gradient_text(f"{index}) {file_name}", "0000FF", "00FFFF"))

        return target_files

    except FileNotFoundError as e:
        print(gradient_text(str(e), "FF0000", "FFFFFF"))
    except PermissionError:
        print(gradient_text(f"Отказано в доступе к каталогу: '{directory}.", "FF0000", "FFFFFF"))
    except Exception as e:
        print(gradient_text(f"Ошибка доступа к каталогу: {e}", "FF0000", "FFFFFF"))

    return None

def execute_command(command):
    """Выполняет данную команду оболочки и выводит результат или ошибку."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(gradient_text(result.stdout.strip(), "00FF00", "FFFFFF"))  # Вывод результата команды
    except subprocess.CalledProcessError as e:
        print(gradient_text(f"Ошибка выполнения команды: {e}\n{e.stderr.strip()}", "FF0000", "FFFFFF"))

def main():
    subprocess.call("chmod +x quickbms", shell=True)

    while True:
        print_main_menu()
        choice = input(gradient_text("Введите ваш выбор: ", "00FF00", "FFFFFF")).strip()


        if choice == '1':
            print_unpack_menu()
            directory = "/storage/emulated/0/Download/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("Введите индекс файла для распаковки (или 0 для возврата): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("Ввод не может быть пустым. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms chinaNB.bms \"{os.path.join(directory, files[index])}\" \"storage/emulated/0/Download/解包/\""
                        execute_command(command)
                    else:
                        print(gradient_text("Недействительный индекс. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("Пожалуйста, введите действительное целое число.", "FF0000", "FFFFFF"))

        elif choice == '2':
            print_repack_menu()
            directory = "/storage/emulated/0/Download/"
            files = list_files_in_directory(directory, '.pak')
            if files:
                index_input = input(gradient_text("Введите индекс файла для упаковки (или 0 для возврата): ", "00FF00", "FFFFFF")).strip()
                if index_input == '0':
                    continue
                if not index_input:
                    print(gradient_text("Ввод не может быть пустым. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                    continue
                try:
                    index = int(index_input) - 1
                    if 0 <= index < len(files):
                        command = f"qemu-i386 quickbms -g -w -r -r chinaNB.bms \"{os.path.join(directory, files[index])}\" \"/storage/emulated/0/Download/打包/\""
                        execute_command(command)
                    else:
                        print(gradient_text("Недействительный индекс. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))
                except ValueError:
                    print(gradient_text("Пожалуйста, введите действительное целое число.", "FF0000", "FFFFFF"))


        elif choice == '0':
            print(gradient_text("退出中...", "FF0000", "FFFFFF"))
            break

        else:
            print(gradient_text("Недействительный выбор. Пожалуйста, попробуйте снова.", "FF0000", "FFFFFF"))

if __name__ == "__main__":
    main()