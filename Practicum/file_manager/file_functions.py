import os
import shutil
from ui_functions import *
import time

def list_directory(path):
    """Возвращает список файлов и директорий в указанной директории."""
    try:
        return os.listdir(path)
    except OSError as e:
        return [f"Ошибка при чтении директории: {e}"]

def change_directory(path):
    """Изменяет текущую рабочую директорию на указанную."""
    try:
        os.chdir(path)
        return f"Текущая директория изменена на {os.getcwd()}"
    except OSError as e:
        return f"Ошибка при изменении директории: {e}"

def create_directory(path):
    """Создаёт новую директорию по заданному пути."""
    try:
        os.mkdir(path)
        return f"Директория {path} создана успешно"
    except OSError as e:
        return f"Ошибка при создании директории: {e}"

def remove_directory(path):
    """Удаляет директорию."""
    try:
        os.rmdir(path)
        return f"Директория {path} удалена успешно"
    except OSError as e:
        return f"Ошибка при удалении директории: {e}"

def delete_file(path):
    """Удаляет файл."""
    try:
        os.remove(path)
        return f"Файл {path} удалён успешно"
    except OSError as e:
        return f"Ошибка при удалении файла: {e}"

def copy_file(source, destination):
    """Копирует файл из исходного местоположения в целевое."""
    try:
        shutil.copy(source, destination)
        return f"Файл {source} скопирован в {destination}"
    except IOError as e:
        return f"Ошибка при копировании файла: {e}"

def move_file(source, destination):
    """Перемещает файл из исходного местоположения в целевое."""
    try:
        shutil.move(source, destination)
        return f"Файл {source} перемещён в {destination}"
    except IOError as e:
        return f"Ошибка при перемещении файла: {e}"

def rename_file(old_name, new_name):
    """Переименовывает файл или директорию."""
    try:
        os.rename(old_name, new_name)
        return f"{old_name} переименован в {new_name}"
    except OSError as e:
        return f"Ошибка при переименовании: {e}"

def get_file_properties(path):
    """Возвращает свойства файла, такие как размер, дата создания и последнего изменения."""
    try:
        stats = os.stat(path)
        file_info = {
            'Размер': stats.st_size,
            'Дата создания': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stats.st_ctime)),
            'Дата последнего изменения': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stats.st_mtime))
        }
        return file_info
    except OSError as e:
        return f"Ошибка при получении свойств файла: {e}"

def open_file(path):
    """Открывает файл для чтения или редактирования."""
    try:
        with open(path, 'r') as file:
            return file.read()
    except IOError as e:
        return f"Ошибка при открытии файла: {e}"

def list_directory(path):
    """Возвращает список файлов и директорий в указанной директории."""
    try:
        contents = os.listdir(path)
        contents.insert(0, "..")  # Добавляем элемент для перехода на каталог выше
        return contents
    except OSError as e:
        return [f"Ошибка при чтении директории: {e}"]

