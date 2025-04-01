from app.io.input import get_text_from_console, read_text_from_file_builtin, read_text_from_file_pandas
from app.io.output import print_text_to_console, write_text_to_file_builtin


def main():
    console_text = get_text_from_console()
    builtin_file_text = read_text_from_file_builtin("data/input_builtin.txt")
    pandas_file_text = read_text_from_file_pandas("data/input_pandas.txt")

    print("Text from console:")
    print_text_to_console(console_text)
    print("\nText from built-in file reading:")
    print_text_to_console(builtin_file_text)
    print("\nText from pandas file reading:")
    print_text_to_console(pandas_file_text)

    output_filepath = "data/output_builtin.txt"
    write_text_to_file_builtin(output_filepath, console_text + "\n" + builtin_file_text + "\n" + pandas_file_text)
    print(f"\nResults written to: {output_filepath}")
if __name__ == '__main__':
    main()