import os
import json
import xml.etree.ElementTree as ET


# Функция для чтения содержимого файла
def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()


# Функция для записи содержимого в файл
def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w') as file:
        file.write(content)


# Функция для конвертации текстового содержимого в верхний регистр
def convert_to_uppercase(text: str) -> str:
    return text.upper()


# Функция для конвертации текстового содержимого в нижний регистр
def convert_to_lowercase(text: str) -> str:
    return text.lower()


# Функция для конвертации текстового содержимого в формат JSON
def convert_to_json(text: str) -> str:
    # Пример преобразования текста в JSON
    data = {"content": text}
    return json.dumps(data)


# Функция для конвертации текстового содержимого в формат XML
def convert_to_xml(text: str) -> str:
    # Пример преобразования текста в XML
    root = ET.Element("document")
    root.text = text
    return ET.tostring(root, encoding="unicode")


# Основная функция конвертации документа
def convert_document(file_path: str, conversion_func, output_dir="converted") -> None:
    # Создаем директорию для сохранения конвертированных файлов, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Чтение содержимого файла
    content = read_file(file_path)
    # Применение функции конвертации
    converted_content = conversion_func(content)

    # Определение пути для сохранения конвертированного файла
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))
    converted_file_path = os.path.join(output_dir, f"{file_name}_{conversion_func.__name__}{file_ext}")

    # Запись конвертированного содержимого в файл
    write_file(converted_file_path, converted_content)
    print(f"Файл сконвертирован и сохранен как '{converted_file_path}'")


if __name__ == "__main__":
    # Пример использования
    file_path = 'aqdoo.txt'
    # Конвертация в верхний регистр
    convert_document(file_path, convert_to_uppercase)
    # Конвертация в нижний регистр
    convert_document(file_path, convert_to_lowercase)
    # Конвертация в JSON
    convert_document(file_path, convert_to_json)
    # Конвертация в XML
    convert_document(file_path, convert_to_xml)
