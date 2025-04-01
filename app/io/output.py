def print_text_to_console(text):
    """
    Функція для виведення тексту в консоль.
    """
    print(text)

def write_text_to_file_builtin(filepath, text):
    """
    Функція для запису тексту до файлу за допомогою вбудованих можливостей Python.
    """
    with open(filepath, 'w') as file:
        file.write(text)