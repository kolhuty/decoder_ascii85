import sys
import base64

def encode():
    "Переводит байты в ASCII85 символы"
    data = sys.stdin.buffer.read()
    encoded_newline = b'\n'
    #Кодируем в ASCII85
    encoded_data = base64.a85encode(data)
    #Вывод
    sys.stdout.buffer.write(encoded_data + encoded_newline)
    sys.exit(0)

def decode():
    "Переводит символы ASCII85 в байты"
    data = sys.stdin.buffer.read()
    encoded_newline = b'\n'
    try:
        #Декодируем ASCII85
        decoded_bytes = base64.a85decode(data, adobe=False)
        #Вывод
        sys.stdout.buffer.write(decoded_bytes + encoded_newline)
        sys.exit(0)
    except ValueError:
        sys.stderr.write("Error: Enter characters that are in ASCII85 encoding")
        sys.exit(3)

def check_arg():
    #Разрешенные аргументы
    valid_args = {"-e", "-d", "--help"}
    args = sys.argv[1:]

    #Проверка на неизвестные элементы
    unknown_args = [arg for arg in args if arg not in valid_args]

    if unknown_args:
        sys.stderr.write(f"Error: Option does not exist. Call --help {' '.join(unknown_args)}\n")
        sys.exit(1)

    #Опция --help
    if "--help" in args:
        with open("help.txt", "rb") as f:
            sys.stdout.buffer.write(f.read())
        sys.exit(0)

    #Проверяем конфликт -e и -d
    if "-e" in args and "-d" in args:
        sys.stderr.write("Error: Cannot use options -e и -d at the same time\n")
        sys.exit(2)

    return "-d" in args

if __name__ == '__main__':
    #Определяем режим
    if check_arg():
        decode()
    else:
        encode()