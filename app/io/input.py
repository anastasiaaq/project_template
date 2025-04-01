import pandas as pd


def get_text_from_console():
    """
    Функція для введення тексту з консолі
    """
    return input("Введіть текст: ")

def read_text_from_file_builtin(filepath):
    """
    Функція для зчитування тексту з файлу за допомогою вбудованих можливостей Python
    """
    with open(filepath, 'r') as file:
        return file.read()

def read_text_from_file_pandas(filepath):
    """
    Функція для зчитування тексту з файлу за допомогою бібліотеки pandas
    """
    df = pd.read_csv(filepath, header=None)
    return df.to_string(index=False, header=False)